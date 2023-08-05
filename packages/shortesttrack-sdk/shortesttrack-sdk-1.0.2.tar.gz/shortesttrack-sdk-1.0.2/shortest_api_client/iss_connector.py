import requests
import json


class ISSConnector:
    def __init__(self, url: str, auth_custom_token: str = None) -> None:
        self._url = url
        self._auth_custom_token = auth_custom_token

    def send(self, msg: dict) -> bytes:
        header = {}
        if self._auth_custom_token is not None:
            header = {'Auth-Custom-Token': self._auth_custom_token}

        r = requests.post('{}/iter'.format(self._url), json=msg, headers=header)
        if r.status_code != 200:
            raise Exception(r.status_code)

        return r.content

    def is_health(self) -> bool:
        try:
            r = requests.get(f'{self._url}/healthz')
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False

    def is_ready(self) -> bool:
        try:
            r = requests.get(f'{self._url}/readyz')
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False
