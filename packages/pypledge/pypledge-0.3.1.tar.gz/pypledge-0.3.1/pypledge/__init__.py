"""Binding for the pledge(2) system call on OpenBSD. Allows restricting
   process functionality for correctness and security."""
import ctypes
import os
from typing import Iterable, Optional


def _iterable_to_bytes(data: Optional[Iterable[str]]) -> Optional[bytes]:
    if isinstance(data, str):
        return bytes(data, 'ascii')
    elif data is not None:
        return bytes(' '.join(data), 'ascii')

    return None


def pledge(promises: Optional[Iterable[str]] = None,
           execpromises: Optional[Iterable[str]] = None) -> None:
    """Restrict the current process to the functionality defined in a
       list of promises, as defined by pledge(2)."""
    try:
        libc = ctypes.CDLL('libc.so', use_errno=True)
        _pledge = libc.pledge
        _pledge.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        _pledge.restype = ctypes.c_int
    except (OSError, AttributeError) as err:
        raise OSError('pledge() not supported') from err

    result = _pledge(_iterable_to_bytes(promises),
                     _iterable_to_bytes(execpromises))
    if result < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
