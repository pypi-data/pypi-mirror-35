from urlobject import URLObject
import requests
import json
from shortest_api_client.utils import getLogger
logger = getLogger()
logger.setLevel('DEBUG')

class SECHelper:
    def __init__(self, config_id: str) -> None:
        logger.info(f'SEC_ID: {config_id}\n')
        self._config_id = config_id

    def get_sec(self, host: str, access_token: str) -> dict:
        url = URLObject(host).add_path('api/metadata/script-execution-configurations/{}'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'GET SEC:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n')

        response = requests.get(url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code)
        logger.info(f'RESPONSE CONTENT: {response.content.decode()}\n')

        return json.loads(response.content)

    def get_content(self, host: str, access_token: str) -> bytes:
        url = URLObject(host).add_path('api/data/script-execution-configurations/{}/script/content'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'GET SCRIPT CONTENT:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n')

        response = requests.get(url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code)
        logger.info(f'RESPONSE CONTENT: {response.content.decode()}\n')

        return response.content
