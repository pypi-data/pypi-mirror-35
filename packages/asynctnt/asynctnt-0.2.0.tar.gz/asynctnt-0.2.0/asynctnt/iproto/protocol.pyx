cimport cython
cimport cpython.dict

import asyncio
import enum

from asynctnt.exceptions import \
    TarantoolSchemaError, TarantoolNotConnectedError

include "const.pxi"

include "unicode.pyx"
include "buffer.pyx"
include "rbuffer.pyx"
include "request.pyx"
include "response.pyx"
include "schema.pyx"
include "db.pyx"

include "coreproto.pyx"


class Iterator(enum.IntEnum):
    """
        Available Iterator types
    """
    EQ = 0
    REQ = 1
    ALL = 2
    LT = 3
    LE = 4
    GE = 5
    GT = 6
    BITS_ALL_SET = 7
    BITS_ANY_SET = 8
    BITS_ALL_NOT_SET = 9
    OVERLAPS = 10
    NEIGHBOR = 11


cdef class BaseProtocol(CoreProtocol):
    def __init__(self, host, port,
                 username, password,
                 fetch_schema,
                 auto_refetch_schema,
                 connected_fut,
                 on_connection_made, on_connection_lost,
                 loop,
                 request_timeout=None,
                 encoding=None,
                 tuple_as_dict=False,
                 initial_read_buffer_size=None):
        CoreProtocol.__init__(self, host, port, encoding,
                              initial_read_buffer_size)

        self.loop = loop

        self.username = username
        self.password = password
        self.fetch_schema = fetch_schema
        self.auto_refetch_schema = auto_refetch_schema

        if tuple_as_dict is None:
            tuple_as_dict = False
        self.tuple_as_dict = tuple_as_dict

        self.request_timeout = request_timeout or 0

        self.connected_fut = connected_fut
        self.on_connection_made_cb = on_connection_made
        self.on_connection_lost_cb = on_connection_lost
        self._closing = False

        self._on_request_completed_cb = self._on_request_completed
        self._on_request_timeout_cb = self._on_request_timeout

        self._reqs = {}
        self._sync = 0
        self._schema_id = -1
        self._schema = Schema.new(self._schema_id)
        self._db = self._create_db()

        try:
            self.create_future = self.loop.create_future
        except AttributeError:
            self.create_future = self._create_future_fallback

    def _create_future_fallback(self):  # pragma: nocover
        return asyncio.Future(loop=self.loop)

    @property
    def schema(self):
        return self._schema

    @property
    def schema_id(self):
        return self._schema_id

    cdef void _set_connection_ready(self):
        if not self.connected_fut.done():
            self.connected_fut.set_result(True)
            self.con_state = CONNECTION_FULL

    cdef void _set_connection_error(self, e):
        if not self.connected_fut.done():
            self.connected_fut.set_exception(e)
            self.con_state = CONNECTION_BAD

    cdef void _on_greeting_received(self):
        if self.username and self.password:
            self._do_auth(self.username, self.password)
        elif self.fetch_schema:
            self._do_fetch_schema(None)
        else:
            self._set_connection_ready()

    cdef void _on_response_received(self, const char *buf, uint32_t buf_len):
        cdef:
            PyObject *req_p
            Request req
            Response resp
            object waiter
            object sync_obj
            object err

            ssize_t l
        resp = Response.new(self.encoding)
        l = response_parse_header(buf, buf_len, resp)
        buf_len -= l
        buf = &buf[l]  # skip header

        sync_obj = <object>resp._sync

        req_p = cpython.dict.PyDict_GetItem(self._reqs, sync_obj)
        if req_p is NULL:
            logger.warning('sync %d not found', resp._sync)
            return

        req = <Request>req_p
        resp._req = req

        cpython.dict.PyDict_DelItem(self._reqs, sync_obj)

        err = None
        try:
            l = response_parse_body(buf, buf_len, resp)
        except Exception as e:
            err = e

        buf_len -= l
        buf = &buf[l]

        waiter = req.waiter
        if waiter is not None \
                and not waiter.done():
            if err is not None:
                waiter.set_exception(err)
            else:
                if resp.is_error():
                    waiter.set_exception(
                        TarantoolDatabaseError(resp._return_code,
                                               resp._errmsg))
                else:
                    waiter.set_result(resp)

    cdef void _do_auth(self, str username, str password):
        # No extra error handling from Db.execute
        fut = self.execute(
            self._db._auth(self.salt, username, password),
            0
        )

        def on_authorized(f):
            if f.cancelled():
                self._set_connection_error(asyncio.futures.CancelledError())
                return
            e = f.exception()
            if not e:
                logger.debug('Tarantool[%s:%s] Authorized successfully',
                             self.host, self.port)

                if self.fetch_schema:
                    self._do_fetch_schema(None)
                else:
                    self._set_connection_ready()
            else:
                logger.error('Tarantool[%s:%s] Authorization failed: %s',
                             self.host, self.port, str(e))
                self._set_connection_error(e)

        fut.add_done_callback(on_authorized)

    cdef void _do_fetch_schema(self, object fut):
        def on_fetch(f):
            if f.cancelled():
                self._set_connection_error(asyncio.futures.CancelledError())
                return
            e = f.exception()
            if not e:
                spaces, indexes = f.result()
                logger.debug('Tarantool[%s:%s] Schema fetch succeeded. '
                             'Spaces: %d, Indexes: %d.',
                             self.host, self.port,
                             len(spaces.body), len(indexes.body))
                try:
                    self._schema = Schema.parse(spaces.schema_id,
                                                spaces.body, indexes.body)
                except Exception as e:
                    logger.exception(e)
                    logger.error('Error happened while parsing schema. '
                                 'Space, fields and index names currently '
                                 'not working. Please file an issue at '
                                 'https://github.com/igorcoding/asynctnt')
                    self.auto_refetch_schema = False
                    self.fetch_schema = False
                    self._schema_id = -1
                    self._set_connection_ready()
                    if fut is not None:
                        fut.set_result(None)
                    return

                if self.auto_refetch_schema:
                    # if no refetch, them we should not
                    # send schema_id at all (leave it -1)
                    self._schema_id = self._schema.id
                else:
                    self._schema_id = -1
                self._set_connection_ready()
                if fut is not None:
                    fut.set_result(self._schema)
            else:
                logger.error('Tarantool[%s:%s] Schema fetch failed: %s',
                             self.host, self.port, str(e))
                if isinstance(e, asyncio.TimeoutError):
                    e = asyncio.TimeoutError('Schema fetch timeout')
                self._set_connection_error(e)
                if fut is not None:
                    fut.set_exception(e)

        self._schema_id = -1
        fut_vspace = self._db.select(SPACE_VSPACE,
                                     timeout=0,
                                     tuple_as_dict=False)
        fut_vindex = self._db.select(SPACE_VINDEX,
                                     timeout=0,
                                     tuple_as_dict=False)
        gather_fut = asyncio.gather(fut_vspace, fut_vindex,
                                    return_exceptions=False,
                                    loop=self.loop)
        gather_fut.add_done_callback(on_fetch)

    cdef void _on_connection_made(self):
        CoreProtocol._on_connection_made(self)

        if self.on_connection_made_cb:
            self.on_connection_made_cb()

    cdef void _on_connection_lost(self, exc):
        cdef:
            Request req
            PyObject *pkey
            PyObject *pvalue
            object key, value
            Py_ssize_t pos

        if self._closing:
            return

        self._closing = True

        pos = 0
        while cpython.dict.PyDict_Next(self._reqs, &pos, &pkey, &pvalue):
            sync = <uint64_t><object>pkey
            req = <Request>pvalue

            waiter = req.waiter
            if waiter and not waiter.done():
                if exc is None:
                    waiter.set_exception(
                        TarantoolNotConnectedError(
                            'Lost connection to Tarantool')
                    )
                else:
                    waiter.set_exception(exc)

        if self.on_connection_lost_cb:
            self.on_connection_lost_cb(exc)

    cdef uint64_t next_sync(self):
        self._sync += 1
        return self._sync

    cdef bint is_closing(self):
        return self._closing

    def _on_request_timeout(self, waiter):
        cdef Request req

        if waiter.done():
            return

        req = waiter._req
        req.timeout_handle.cancel()
        req.timeout_handle = None
        waiter.set_exception(
            asyncio.TimeoutError(
                '{} exceeded timeout'.format(req.__class__.__name__))
        )

    def _on_request_completed(self, fut):
        cdef Request req = fut._req
        fut._req = None

        if req.timeout_handle is not None:
            req.timeout_handle.cancel()
            req.timeout_handle = None

    cdef object _new_waiter_for_request(self, Request req, float timeout):
        fut = self.create_future()
        fut._req = req  # to be able to retrieve request after done()
        req.waiter = fut

        if timeout < 0:
            timeout = self.request_timeout
        if timeout is not None and timeout > 0:
            req.timeout_handle = \
                self.loop.call_later(timeout,
                                     self._on_request_timeout_cb, fut)
            fut.add_done_callback(self._on_request_completed_cb)
        return fut

    cdef Db _create_db(self):
        return Db.new(self)

    def create_db(self):
        return self._create_db()

    def get_common_db(self):
        return self._db

    cdef object execute(self, Request req, float timeout):
        if self.con_state == CONNECTION_BAD:
            raise TarantoolNotConnectedError('Tarantool is not connected')

        cpython.dict.PyDict_SetItem(self._reqs, req.sync, req)
        self._write(req.buf)

        return self._new_waiter_for_request(req, timeout)

    cdef uint32_t transform_iterator(self, iterator) except *:
        if isinstance(iterator, int):
            return iterator
        if isinstance(iterator, Iterator):
            return iterator.value
        if isinstance(iterator, str):
            return Iterator[iterator]
        else:
            raise TypeError('Iterator is of unsupported type '
                            '(asynctnt.Iterator, int, str)')

    def refetch_schema(self):
        fut = self.create_future()
        self._do_fetch_schema(fut)
        return fut


class Protocol(BaseProtocol, asyncio.Protocol):
    pass
