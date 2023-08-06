import asyncio
import socket
from functools import partial
from typing import Callable, Tuple, Optional, Iterable

from . import aitertools
from . import resolver
from .stagger import staggered_race
from .typing import AddrInfoType, HostType, PortType

__all__ = ['create_connected_sock', 'create_connection', 'open_connection']

_DEFAULT_DELAY = 0.3
_DEFAULT_LIMIT = 2 ** 16


async def _connect_sock(
        addr_info: AddrInfoType,
        local_addr_info: AddrInfoType = None,
        *,
        loop: asyncio.AbstractEventLoop = None
) -> socket.socket:
    """Create, bind and connect one socket."""
    loop = loop or asyncio.get_event_loop()
    family, type_, proto, _, address = addr_info
    sock = socket.socket(family=family, type=type_, proto=proto)
    try:
        sock.setblocking(False)
        if local_addr_info is not None:
            laddr = local_addr_info[4]
            try:
                sock.bind(laddr)
            except OSError as e:
                raise OSError(
                    e.errno,
                    f'error while attempting to bind on address {laddr!r}: '
                    f'{e.strerror.lower()}')
        await loop.sock_connect(sock, address)
        return sock
    except:
        sock.close()
        raise


async def create_connected_sock(
        host: HostType,
        port: PortType,
        *,
        family: int = 0,
        proto: int = 0,
        flags: int = 0,
        local_addr: Tuple = None,
        local_addrs: Iterable[Tuple] = None,
        delay: Optional[float] = _DEFAULT_DELAY,
        interleave: int = 1,
        loop: asyncio.AbstractEventLoop = None,
) -> socket.socket:
    """Connect to *(host, port)* and return a connected socket.

    This function implements :rfc:`6555` Happy Eyeballs and some features of
    :rfc:`8305` Happy Eyeballs v2. When a host name resolves to multiple IP
    addresses, connection attempts are made in parallel with staggered start
    times, and the one completing fastest is used. The resolved addresses can
    be interleaved by address family, so even if network connectivity for one
    address family is broken (when IPv6 fails, for example), connections
    still complete quickly.

    (Some fancier features specified in RFC8305, like asynchronous DNS
    queries, statefulness, and features related to NAT64 and DNS64 are not
    implemented. Destination address sorting is left for the operating
    system; it is assumed that the addresses returned by
    :func:`~asyncio.AbstractEventLoop.getaddrinfo` is already sorted
    according to OS's preferences.)

    Most of the arguments should be familiar from the various :mod:`socket` and
    :mod:`asyncio` methods.
    *delay* and *interleave* control Happy Eyeballs-specific behavior.
    *local_addrs* is a new argument providing new features not specific to
    Happy Eyeballs.

    Args:
        host: Host name to connect to. Unlike
            :func:`asyncio.create_connection`
            there is no default, but it's still possible to manually specify
            *None* here.

        port: Port number to connect to. Similar to **host**, *None* can be
            specified here as well.

        family: Address family.
            Specify :data:`socket.AF_INET` or :data:`socket.AF_INET6` here
            to limit the type of addresses used. See documentation on the
            :mod:`socket` module for details.

        proto: Socket protocol. Since the socket type is always
            :data:`socket.SOCK_STREAM`, proto can usually be left unspecified.

        flags: Flags passed to :func:`~asyncio.AbstractEventLoop.getaddrinfo`.
            See documentation on :func:`socket.getaddrinfo` for details.

        local_addr: *(local_host, local_port)* tuple used to bind the socket to
            locally. The *local_host* and *local_port* are looked up using
            :func:`~asyncio.AbstractEventLoop.getaddrinfo` if necessary,
            similar to *host* and *port*.

        local_addrs: An iterable of (local_host, local_port) tuples, all of
            which are candidates for locally binding the socket to. This allows
            e.g. providing one IPv4 and one IPv6 address. Addresses are looked
            up using :func:`~asyncio.AbstractEventLoop.getaddrinfo`
            if necessary.

        delay: Amount of time to wait before making connections to different
            addresses. This is the "Connect Attempt Delay" as defined in
            :rfc:`8305`.

        interleave: Whether to interleave addresses returned by
            :func:`~asyncio.AbstractEventLoop.getaddrinfo` by address family.
            0 means not to interleave and simply use the returned order.
            An integer >= 1 is interpreted as
            "First Address Family Count" defined in :rfc:`8305`,
            i.e. the reordered list will have this many addresses for the
            first address family,
            and the rest will be interleaved one to one.

        loop: Event loop to use.

    Returns:
        The connected :class:`socket.socket` object.


    .. versionadded:: v0.1.3
       the *local_addrs* parameter.
    """
    loop = loop or asyncio.get_event_loop()

    if local_addr is not None and local_addrs is not None:
        raise ValueError(
            'local_addr and local_addrs cannot be specified at the same time')

    remote_addrinfo_aiter = resolver.builtin_resolver(
        host, port, family=family, type_=socket.SOCK_STREAM, proto=proto,
        flags=flags, first_addr_family_count=interleave, loop=loop)

    if local_addrs is None and local_addr is not None:
        local_addrs = [local_addr]
    if local_addrs is not None:
        local_addrinfo_aiter = resolver.ensure_multiple_addrs_resolved(
            local_addrs, family=family, type_=socket.SOCK_STREAM,
            proto=proto, flags=flags, loop=loop)
    else:
        local_addrinfo_aiter = aitertools.aiter_from_iter((None,))

    # Yay for async comprehensions!
    connect_tasks = (
        partial(_connect_sock, ai, lai, loop=loop)
        async for ai, lai in aitertools.product(
            remote_addrinfo_aiter, local_addrinfo_aiter
        )
    )

    # Use a separate task for each (remote_addr, local_addr) pair. When
    # multiple local addresses are specified, this depends on the OS quickly
    # failing address combinations that don't work (e.g. an IPv6 remote
    # address with an IPv4 local address). If your OS can't figure that out,
    # it's probably time to get a better OS.
    winner_socket, _, exceptions = await staggered_race(
        connect_tasks, delay, loop=loop)
    if winner_socket:
        return winner_socket
    if len(exceptions) == 1:
        raise exceptions[0]
    else:
        # If they all have the same str(), raise one.
        model = str(exceptions[0])
        if all(str(exc) == model for exc in exceptions):
            raise exceptions[0]
        # Raise a combined exception so the user can see all
        # the various error messages.
        raise OSError('Multiple exceptions: {}'.format(
            ', '.join(str(exc) for exc in exceptions)))


async def create_connection(
        protocol_factory: Callable[[], asyncio.Protocol],
        host: HostType,
        port: PortType,
        *,
        ssl=None,
        family: int = 0,
        proto: int = 0,
        flags: int = 0,
        local_addr: Tuple = None,
        local_addrs: Iterable[Tuple] = None,
        server_hostname=None,
        ssl_handshake_timeout=None,
        delay: Optional[float] = _DEFAULT_DELAY,
        interleave: int = 1,
        loop: asyncio.AbstractEventLoop = None,
) -> Tuple[asyncio.Transport, asyncio.Protocol]:
    """Connect to *(host, port)* and return *(transport, protocol)*.

    This function does the same thing as
    :meth:`asyncio.AbstractEventLoop.create_connection`,
    only more awesome with Happy Eyeballs.
    Refer to that function's documentation for
    explanations of these arguments: *protocol_factory*, *ssl*, and
    *server_hostname*. Refer to :func:`~async_stagger.create_connected_sock`
    for all other arguments.

    Returns:
        *(transport, protocol)*, the same as
        :meth:`asyncio.AbstractEventLoop.create_connection`.
    """
    loop = loop or asyncio.get_event_loop()
    # These checks are copied from BaseEventLoop.create_connection()
    if server_hostname is not None and not ssl:
        raise ValueError('server_hostname is only meaningful with ssl')
    if server_hostname is None and ssl:
        server_hostname = host
    if ssl_handshake_timeout is not None and not ssl:
        raise ValueError('ssl_handshake_timeout is only meaningful with ssl')

    sock = await create_connected_sock(
        host, port, family=family, proto=proto, flags=flags,
        local_addr=local_addr, local_addrs=local_addrs,
        delay=delay, interleave=interleave, loop=loop)

    try:
        # Defer to the event loop to create transport and protocol
        return await loop.create_connection(
            protocol_factory, ssl=ssl, sock=sock,
            server_hostname=server_hostname)
    except:
        sock.close()
        raise


async def open_connection(
        host: HostType,
        port: PortType,
        *,
        limit: int = _DEFAULT_LIMIT,
        loop: asyncio.AbstractEventLoop = None,
        **kwargs,
) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    """Connect to (host, port) and return (reader, writer).

    This function does the same thing as :func:`asyncio.open_connection`, with
    added awesomeness of Happy Eyeballs. Refer to the documentation of that
    function for what *limit* does, and refer to
    :func:`~async_stagger.create_connection` and
    :func:`~async_stagger.create_connected_sock` for everything else.

    Returns:
        *(reader, writer)*, the same as :func:`asyncio.open_connection`.
    """
    loop = loop or asyncio.get_event_loop()
    reader = asyncio.StreamReader(limit=limit, loop=loop)
    protocol = asyncio.StreamReaderProtocol(reader, loop=loop)
    transport, _ = await create_connection(
        lambda: protocol, host, port, loop=loop, **kwargs)
    writer = asyncio.StreamWriter(transport, protocol, reader, loop)
    return reader, writer
