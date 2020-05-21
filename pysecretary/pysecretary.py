import os
import re
from typing import Tuple, Callable

from pysecretary.exceptions import InvalidPrefixError, UnsupportedPrefixError, NotFoundError, PysecretaryError


class NotFound:
    pass
NOT_FOUND = NotFound()




class PrefixDispatchRegistry:
    PREFIX_PATTERN = re.compile(r"(^(\w+):\/\/)")

    def __init__(self):
        self._supported_prefixes = set()
        self._registry = dict()

    def register(self, prefix: str, f: Callable[[str], str], force=False):
        if not callable(f):
            raise TypeError(f' "{type(f)}" is not callable')

        if prefix in self._supported_prefixes and not force:
            raise KeyError(
                f'prefix "{prefix}" already exists, use force=True if you want to overwrite'
            )

        self._supported_prefixes.add(prefix)
        self._registry[prefix] = f

    def is_supported(self, prefix: str) -> bool:
        if prefix not in self._supported_prefixes:
            return False
        return True

    def get(self, prefix: str) -> Callable[[str], str]:
        return self._registry.get(prefix)


def _parse(v: str) -> Tuple[str, str]:
    vals = re.split(PrefixDispatchRegistry.PREFIX_PATTERN, v, maxsplit=1)
    if len(vals) == 4:
        prefix = vals[2].casefold()
        value = vals[3]

        if not _registry.is_supported(prefix):
            raise UnsupportedPrefixError(prefix)

        return prefix, value

    raise InvalidPrefixError(v)


def _get_env(v: str) -> str:
    prefix, k = _parse(v)
    value = os.environ.get(k)
    if value is None:
        raise NotFoundError(f'no environment variable found for key "{k}"')
    return value


def get(env: str, default=NOT_FOUND) -> str:
    try:
        prefix, value = _parse(env)
        f = _registry.get(prefix)
        return f(env)
    except PysecretaryError:
        if default is NOT_FOUND:
            raise
        return default


def register(prefix: str, f: Callable[[str, str], str], force=False):
    _registry.register(prefix, f, force)


_registry = PrefixDispatchRegistry()
_registry.register("env", _get_env)
