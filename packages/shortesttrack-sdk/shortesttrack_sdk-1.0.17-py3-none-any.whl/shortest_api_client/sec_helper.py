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

    def get_matrix(self, matrix_id: str, host: str, access_token: str):
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(f'/api/data/script-execution-configurations/{self._config_id}'
                                       f'/matrices/{matrix_id}/data')

        logger.info(f'READ MATRIX:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'MATRIX_ID: {matrix_id}\n')

        response = requests.get(url=url,  headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code, response.content)

        response = json.loads(response.content.decode())
        fields = response['schema']['fields']

        matrix = []
        if None is not response.get('rows'):
            for f in response['rows']:
                row = []
                for v in f['f']:
                    row.append(v.get('v'))
                matrix.append(row)

        return {'fields': fields, 'matrix': matrix}

    def insert_matrix(self, matrix_id: str, matrix: dict, host: str, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(f'/api/data/script-execution-configurations/{self._config_id}'
                                       f'/matrices/{matrix_id}/insert')

        logger.info(f'INSERT MATRIX:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'MATRIX_ID: {matrix_id}\n')

        insert_rows = []
        for row in matrix.get('matrix'):
            tmp = {}
            for k, v in zip(matrix['fields'], row):
                tmp[k['name']] = v
            insert_rows.append({"json": tmp})

        body = {'rows': insert_rows}
        response = requests.post(url=url, json=body, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code, response.content)
