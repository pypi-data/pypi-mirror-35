import requests
import json


class SyncConnector():
    def __init__(self, company_sub_domen, script_url, auth_custom_token=None):
        self._url = f'https://{company_sub_domen}.shtr.io/api/serving/{script_url}'
        self._auth_custom_token = auth_custom_token

    def send(self, msg):
        header = {}
        if self._auth_custom_token is not None:
            header = {'Auth-Custom-Token': self._auth_custom_token}

        r = requests.post('{}/iter'.format(self._url), json=msg, headers=header)
        if r.status_code != 200:
            raise Exception(r.status_code)
        return r.content.decode()

    def is_health(self):
        try:
            r = requests.get(f'{self._url}/healthz')
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False

    def is_ready(self):
        try:
            r = requests.get(f'{self._url}/readyz')
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False
