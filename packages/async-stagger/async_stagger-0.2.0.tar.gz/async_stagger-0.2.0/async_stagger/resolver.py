"""Code related to resolving host names to IP addresses.

A resolver is a callable with signature
*resolver(host, port, *, family=0, type=0, proto=0, flags=0)*
(and more optional arguments if necessary)
that returns an async iterable of 5-tuples
*(family, type, proto, canonname, sockaddr)*.
They are intended to be used by :func:`happy_eyeballs.create_connected_sock`,
and to be more or less interchangeable.
"""

import asyncio
import collections
import itertools
import socket
from typing import AsyncIterator, Tuple, Iterable, List, Optional

from .typing import AddrInfoType, HostType, PortType


_HAS_IPv6 = hasattr(socket, 'AF_INET6')


async def _getaddrinfo_raise_on_empty(
        host: HostType,
        port: PortType,
        *,
        family: int = 0,
        type_: int = 0,
        proto: int = 0,
        flags: int = 0,
        loop: asyncio.AbstractEventLoop = None,
) -> List[AddrInfoType]:
    # DRY at work.
    loop = loop or asyncio.get_event_loop()
    addrinfos = await loop.getaddrinfo(
        host, port, family=family, type=type_, proto=proto, flags=flags)
    if not addrinfos:
        raise OSError(
            f'getaddrinfo({host!r}, {port!r}, family={family!r}, '
            f'type={type_!r}, proto={proto!r}, flags={flags!r}) '
            f'returned empty list')
    return addrinfos


def _ipaddr_info(
        host: HostType,
        port: PortType,
        family: int,
        type_: int,
        proto: int,
) -> Optional[AddrInfoType]:
    # This function is copied from asyncio/base_events.py with minimal
    # modifications.

    # Try to skip getaddrinfo if "host" is already an IP. Users might have
    # handled name resolution in their own code and pass in resolved IPs.
    if not hasattr(socket, 'inet_pton'):
        return

    if proto not in {0, socket.IPPROTO_TCP, socket.IPPROTO_UDP} or \
            host is None:
        return None

    if type_ == socket.SOCK_STREAM:
        # Linux only:
        #    getaddrinfo() can raise when socket.type is a bit mask.
        #    So if socket.type is a bit mask of SOCK_STREAM, and say
        #    SOCK_NONBLOCK, we simply return None, which will trigger
        #    a call to getaddrinfo() letting it process this request.
        proto = socket.IPPROTO_TCP
    elif type_ == socket.SOCK_DGRAM:
        proto = socket.IPPROTO_UDP
    else:
        return None

    if port is None:
        port = 0
    elif isinstance(port, bytes) and port == b'':
        port = 0
    elif isinstance(port, str) and port == '':
        port = 0
    else:
        # If port's a service name like "http", don't skip getaddrinfo.
        try:
            port = int(port)
        except (TypeError, ValueError):
            return None

    if family == socket.AF_UNSPEC:
        afs = [socket.AF_INET]
        if _HAS_IPv6:
            afs.append(socket.AF_INET6)
    else:
        afs = [family]

    if isinstance(host, bytes):
        host = host.decode('idna')
    if '%' in host:
        # Linux's inet_pton doesn't accept an IPv6 zone index after host,
        # like '::1%lo0'.
        return None

    for af in afs:
        try:
            socket.inet_pton(af, host)
            # The host has already been resolved.
            if _HAS_IPv6 and af == socket.AF_INET6:
                return af, type_, proto, '', (host, port, 0, 0)
            else:
                return af, type_, proto, '', (host, port)
        except OSError:
            pass

    # "host" is not an IP address.
    return None


async def _ensure_resolved(
        address: Tuple,
        *,
        family: int = 0,
        type_: int = socket.SOCK_STREAM,
        proto: int = 0,
        flags: int = 0,
        loop: asyncio.AbstractEventLoop = None,
) -> List[AddrInfoType]:
    # This function is adapted from asyncio/base_events.py.
    loop = loop or asyncio.get_event_loop()
    host, port = address[:2]
    info = _ipaddr_info(host, port, family, type_, proto)
    if info is not None:
        # "host" is already a resolved IP.
        return [info]
    else:
        return await _getaddrinfo_raise_on_empty(
            host, port, family=family, type_=type_,
            proto=proto, flags=flags, loop=loop)


def _interleave_addrinfos(
        addrinfos: Iterable[AddrInfoType],
        first_address_family_count: int = 1,
) -> List[AddrInfoType]:
    """Interleave list of addrinfo tuples by family."""
    # Group addresses by family
    addrinfos_by_family = collections.OrderedDict()
    for addr in addrinfos:
        family = addr[0]
        if family not in addrinfos_by_family:
            addrinfos_by_family[family] = []
        addrinfos_by_family[family].append(addr)
    addrinfos_lists = list(addrinfos_by_family.values())

    reordered = []
    if first_address_family_count > 1:
        reordered.extend(addrinfos_lists[0][:first_address_family_count - 1])
        del addrinfos_lists[0][:first_address_family_count - 1]
    reordered.extend(
        a for a in itertools.chain.from_iterable(
            itertools.zip_longest(*addrinfos_lists)
        ) if a is not None
    )
    return reordered


async def builtin_resolver(
        host,
        port,
        *,
        family: int = 0,
        type_: int = 0,
        proto: int = 0,
        flags: int = 0,
        first_addr_family_count: int = 1,
        loop: asyncio.AbstractEventLoop = None,
) -> AsyncIterator[AddrInfoType]:
    """Resolver using built-in getaddrinfo().

    Interleaves addresses by family if required, and yield results as an
    async iterable. Nothing spectacular.
    """
    loop = loop or asyncio.get_event_loop()
    addrinfos = await _getaddrinfo_raise_on_empty(
        host, port, family=family, type_=type_,
        proto=proto, flags=flags, loop=loop)
    addrinfos = _interleave_addrinfos(addrinfos, first_addr_family_count)
    # it would be nice if "yield from addrinfos" worked, but alas,
    # https://www.python.org/dev/peps/pep-0525/#asynchronous-yield-from
    for ai in addrinfos:
        yield ai


async def ensure_multiple_addrs_resolved(
        addresses: List[Tuple],
        family: int = 0,
        type_: int = socket.SOCK_STREAM,
        proto: int = 0,
        flags: int = 0,
        loop: asyncio.AbstractEventLoop = None,
) -> AsyncIterator[AddrInfoType]:
    """Ensure all addresses in *addresses* are resolved.

    This is for resolving multiple local bind addresses. All addresses are
    resolved before yielding any of them, in case some of them raise
    exceptions when resolving.
    """
    loop = loop or asyncio.get_event_loop()
    results = await asyncio.gather(*(
        _ensure_resolved(
            addr, family=family, type_=type_, proto=proto,
            flags=flags, loop=loop
        )
        for addr in addresses
    ))
    for addrinfo in itertools.chain.from_iterable(results):
        yield addrinfo
