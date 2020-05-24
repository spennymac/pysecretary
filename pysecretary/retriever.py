import os

from .exceptions import NotFoundError


class SecretRetriever:

    def get(self, key: str) -> str:
        """
           Retrieves the contents of *key*
           :param str key: key passed into pysecretary with the prefix stripped
        """
        raise NotImplementedError


class EnvironmentSecretRetriever(SecretRetriever):

    def get(self, key: str) -> str:
        value = os.environ.get(key)
        if value is None:
            raise NotFoundError(f'no environment variable found for key "{key}"')
        return value
