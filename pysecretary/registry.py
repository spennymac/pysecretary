from typing import Callable

from .exceptions import InvalidPrefixError, UnsupportedPrefixError
from .prefix import VALID_PREFIX
from .retriever import SecretRetriever


class SecretRetrieverRegistry:

    def __init__(self):
        self._supported_prefixes = set()
        self._registry = dict()

    def register(self, prefix: str, retriever: SecretRetriever, force=False):
        if not VALID_PREFIX.match(prefix):
            raise InvalidPrefixError(
                f'prefix {prefix} is not valid, a prefix must be in the format of {VALID_PREFIX}.')

        if not isinstance(retriever, SecretRetriever):
            raise TypeError(f' "{type(retriever)}" is not a SecretRetriever')

        if prefix in self._supported_prefixes and not force:
            raise KeyError(
                f'prefix "{prefix}" already exists, use force=True if you want to overwrite'
            )

        self._supported_prefixes.add(prefix)
        self._registry[prefix] = retriever

    def is_supported(self, prefix: str) -> bool:
        if prefix not in self._supported_prefixes:
            return False
        return True

    def get(self, prefix: str) -> Callable[[str], str]:
        if not self.is_supported(prefix):
            raise UnsupportedPrefixError()
        return self._registry.get(prefix)
