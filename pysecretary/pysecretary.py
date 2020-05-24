from .exceptions import PysecretaryError
from .prefix import parse
from .registry import SecretRetrieverRegistry
from .retriever import SecretRetriever, EnvironmentSecretRetriever


class NotFound:
    pass


NOT_FOUND = NotFound()


def get(v: str, default=NOT_FOUND) -> str:
    try:
        prefix, value = parse(v)
        retriever: SecretRetriever = _registry.get(prefix)
        return retriever.get(value)
    except PysecretaryError:
        if default is NOT_FOUND:
            raise
        return default


def register(prefix: str, retriever: SecretRetriever, force=False):
    _registry.register(prefix, retriever, force)


_registry = SecretRetrieverRegistry()
_registry.register("env", EnvironmentSecretRetriever())
