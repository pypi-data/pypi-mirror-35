from urlobject import URLObject
import requests
from requests.auth import HTTPBasicAuth

from shortest_api_client.access_token import AccessToken
from shortest_api_client.utils import getLogger
logger = getLogger()
logger.setLevel('DEBUG')


class AuthHelper:
    def __init__(self, host: str) -> None:
        self._host = host
        logger.info(f'AUTH -> HOST:{host}\n')

    def get_access_token_from_username(self, username: str, password: str, company_id: str) -> AccessToken:
        f_root = [
            ('grant_type', 'password'), ('username', username),
            ('password', password), ('company_id', company_id)
        ]
        url = URLObject(self._host).add_path('/api/uaa/authenticate')

        req = requests.Request('POST', url, data=f_root).prepare()

        return AccessToken(req)

    def get_access_token_from_refresh_token(self, refresh_token: str) -> AccessToken:
        data = 'grant_type=refresh_token&client_id=script&refresh_token={}'.format(refresh_token)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        logger.info(f'GET ACCESS TOKEN:\n'
                    f'DATA: {data}\n'
                    f'HEADERS: {str(headers)}\n')
        req = requests.Request('POST', URLObject(self._host).add_path('/oauth/token'),
                               data=data, headers=headers,
                               auth=HTTPBasicAuth('script', 'noMatter', )).prepare()

        return AccessToken(req)
