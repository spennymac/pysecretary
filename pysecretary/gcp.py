from google.cloud.secretmanager_v1 import SecretManagerServiceClient

from pysecretary.retriever import SecretRetriever


class GCPSecretRetriever(SecretRetriever):
    def __init__(self, client: SecretManagerServiceClient):
        self._client = client

    def get(self, key: str):
        request = {
            "name": key
        }
        response = self._client.access_secret_version(request=request)
        return response.payload.data.decode("UTF-8")
