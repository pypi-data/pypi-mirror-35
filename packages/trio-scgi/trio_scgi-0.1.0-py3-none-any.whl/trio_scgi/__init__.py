import trio

from multidict import CIMultiDict, CIMultiDictProxy
from typing import Tuple, Union


class ProtocolError(Exception):
    """
    Raised if the SCGI protocol is violated somehow.
    """


class ScgiStream:
    """
    Implementation of the SCGI protocol.

    Normal workflow is:

    * Instantiate the object from a connected ``Stream``.
    * Call ``receive_headers``.
    * Validate the headers, e.g. recognized HTTP method or path.
    * Call ``receive_body`` until EOF.
    * Call ``send_header`` with the HTTP response header.
    * On the underlying ``Stream``, send your HTTP response body with ``send_all``.
    * Close the underlying ``Stream``.
    """

    def __init__(self, stream: trio.abc.Stream):
        self.stream = stream

    async def receive_headers(self, maxsize: int) -> CIMultiDictProxy:
        """
        Receive HTTP headers.

        Args:
            maxsize: Maximum length of HTTP header in bytes

        Returns:
            The HTTP headers as a CIMultiDictProxy.

        Raises:
            ValueError: Bad parameter passed
            ProtocolError: Something is wrong with the data received.
            EOFError: EOF before whole netstring could be read.
            RuntimeError: Header already received.
        """

        if maxsize <= 0:
            raise ValueError('maxsize must be positive.')

        if hasattr(self, 'headers'):
            raise RuntimeError('Headers already received.')

        netstr, body_chunk = await self._read_netstring(maxsize)

        # Each key and each value is terminated with \x00. Split should therefore yield an odd number of items,
        # where the last one is empty.
        kv_sequence = netstr.split(b'\x00')
        if len(kv_sequence) % 2 != 1:
            raise ProtocolError('Odd number of elements in keyvalue sequence.')
        if kv_sequence[-1]:
            raise ProtocolError('keyvalue sequence not terminated by \\x00.')

        # Decode headers as latin1. They are supposed to be ASCII only (or some MIME encodings).
        # For other encodings, re-encode as latin1 and decode with the other encoding.
        # Latin1 in python (at least cpython and pypy) directly decodes bytes to chars with the same code point
        # even if a byte is in one of the latin1 gaps.
        it = (kv.decode('latin1') for kv in kv_sequence)

        # SCGI specs forbids duplicate headers. But reality has them.
        # E.g. there are often multiple Cookie: headers.
        self._headers = CIMultiDict(zip(it, it))
        self._body_remaining = self.content_length
        self._body_chunk = body_chunk

        return self.headers

    async def receive_body(self, max_bytes: int) -> bytes:
        """
        Receive part of the HTTP request body.

        This method should be called until it returns ``b""``.

        Args:
            max_bytes: The maximum number of bytes to return.

        Returns:
            Some bytes or ``b""`` if everything was received.

        Raises:
            ValueError: Bad parameter passed
            EOFError: Client closed the connection
        """
        if max_bytes < 0:
            raise ValueError('max_bytes must be non-negative.')

        if self._body_chunk:
            await trio.sleep(0)
            buf = bytes(self._body_chunk[:max_bytes])
            del self._body_chunk[:len(buf)]
        elif self._body_remaining > 0:
            buf = await self.stream.receive_some(max_bytes)
        else:
            await trio.sleep(0)
            buf = b''

        self._body_remaining -= len(buf)
        if self._body_remaining < 0:
            raise ProtocolError('Too much input.')

        if max_bytes and self._body_remaining and not buf:
            raise EOFError('Not enough input.')

        return buf

    async def send_header(self, code: int, reason: str, headers: Union[dict, CIMultiDict]):
        """
        Send the HTTP response header.

        Args:
            code: HTTP status code, e.g. 200
            reason: HTTP reason phrase, e.g. "OK"
            headers: Dictionary with HTTP headers
        """

        buf = bytearray()
        buf.extend('Status: {} {}\r\n'.format(code, reason).encode())

        for k, v in headers.items():
            buf.extend('{}: {}\r\n'.format(k, v).encode())

        buf.extend(b'\r\n')

        await self.stream.send_all(buf)

    async def _read_netstring(self, maxsize: int) -> Tuple[bytearray, bytearray]:
        """
        Read a netstring from the stream.

        A netstring looks like ``11:SomePayload,``, optionally followed by more data (HTTP request body).

        Args:
            maxsize: The maximum length of the netstring payload.

        Returns:
            The netstring payload and the (possibly empty) first part of the body.

        Raises:
            ProtocolError: Something is wrong with the data received.
            EOFError: EOF before whole netstring could be read.

        """

        # Read the <length> ":" part of the netstring. <length> Must have 10 or fewer decimal digits to prevent a
        # theoretical DoS (send lots of data without a ':').
        # This limits the total size of the HTTP header to a few Gigabytes. If you have a real application that
        # needs to receive larger **headers**, I'd love to hear about it :-)
        ns = bytearray()

        while len(ns) <= 10 and b':' not in ns:
            tmp = await self.stream.receive_some(4096)
            if not tmp:
                raise EOFError
            ns.extend(tmp)

        try:
            idx = ns.index(b':')
        except ValueError as ex:
            raise ProtocolError('Length delimiter not found after first 10 chars.') from ex

        if idx > 10:
            raise ProtocolError('Too many digits in length.')

        if idx < 2:
            raise ProtocolError('Need at least two decimal digits in length.')

        if ns[0] == ord('0'):
            raise ProtocolError('Leading zeros in length are forbidden.')

        try:
            size = int(ns[:idx])
        except ValueError as ex:
            raise ProtocolError(str(ex)) from ex

        del ns[:idx + 1]

        if size > maxsize:
            raise ProtocolError('Size of netstring exceeds limit: {} > {}'.format(size, maxsize))

        # Read the payload and the trailing ","
        while len(ns) <= size:
            tmp = await self.stream.receive_some(4096)
            if not tmp:
                raise EOFError
            ns.extend(tmp)

        if ns[size] != ord(','):
            raise ProtocolError("Netstring doesn't end with a comma.")

        # Split the netstring from any trailing HTTP body
        body_chunk = ns[size + 1:]
        del ns[size:]

        return ns, body_chunk

    @property
    def content_length(self) -> int:
        """
        Get the HTTP body length.

        Returns:
            HTTP body length in bytes.

        Raises:
            ProtocolError: Header missing or badly coded.
        """
        try:
            return int(self.headers['CONTENT_LENGTH'])
        except (KeyError, ValueError) as ex:
            raise ProtocolError(str(ex)) from ex

    @property
    def headers(self) -> CIMultiDictProxy:
        """
        Get HTTP headers. Only works after receive_headers was called.

        Returns:
            The HTTP headers as a CIMultiDictProxy.

        Raises:
            AttributeError: receive_headers was not called.
        """
        return CIMultiDictProxy(self._headers)
