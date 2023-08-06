
import os
import logging

import python_http_client

from .types import *


logger = logging.getLogger("paggcerto")


try:
    API_USER = os.environ["PAGGCERTO_API_USER"]
    API_PASSWORD = os.environ["PAGGCERTO_API_PASSWORD"]
    API_USE_SANDBOX = os.environ.get("PAGGCERTO_API_USE_SANDBOX", True)
except KeyError:
    raise Exception(
        "Required environment variables PAGGCERTO_API_USER and PAGGCERTO_API_PASSWORD"
    )


PRODUCTION_HOST = 'https://api-recorrencia.paggcerto.com.br/v1/'
SANDBOX_HOST = 'https://sandbox-recorrencia.paggcerto.com.br/v1/'


class Auth:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def request_authorization_header(self, client):
        try:
            response = client.core.auth.post(request_body={
                'username': self.user,
                'pass': self.password
            })
            token = response.to_dict['token']
            return {
                "Authorization": f"Bearer {token}"
            }
        except python_http_client.HTTPError as e:
            logger.exception(f"error on auth {e.to_dict}")
            raise


class NoAuth(Auth):
    def __init__(self):
        pass

    def request_authorization_header(self, client):
        return {}


class PaggcertoAPIClient:

    def __init__(self, auth=None, use_sandbox=API_USE_SANDBOX):
        self._auth = auth or Auth(API_USER, API_PASSWORD)
        self._use_sandbox = use_sandbox

        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = python_http_client.Client(
                host=SANDBOX_HOST if self._use_sandbox else PRODUCTION_HOST
            )

            self._client.request_headers = self._auth.request_authorization_header(self._client)

        return self._client
