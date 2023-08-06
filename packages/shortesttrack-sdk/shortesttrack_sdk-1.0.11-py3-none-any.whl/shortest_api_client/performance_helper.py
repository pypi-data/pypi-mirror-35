from urlobject import URLObject
import requests
from shortest_api_client.utils import getLogger
logger = getLogger()
logger.setLevel('DEBUG')


class PerformanceHelper:
    def __init__(self, performance_id: str, config_id: str) -> None:

        logger.info(f'SEC_ID: {config_id}\n')
        self._config_id = config_id

        logger.info(f'PERFORMANCE_ID: {performance_id}\n')
        self._performance_id = performance_id


    def send_success(self, host: str, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(f'api/exec-scheduling/v1/sec/{self._config_id}/'
                                       f'performances/{self._performance_id}/success/')

        logger.info(f'SUCCESS:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'PERFORMANCE_ID: {self._performance_id}\n')

        response = requests.post(url=url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code)

    def send_failed(self, host: str, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(f'api/exec-scheduling/v1/sec/{self._config_id}/'
                                       f'performances/{self._performance_id}/failed/')

        logger.info(f'FAILED:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'PERFORMANCE_ID: {self._performance_id}\n')

        response = requests.post(url=url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 200:
            raise Exception(response.status_code)



    def write_parameter(self, parameter_id: str, parameter_value: str, host: str, access_token: str) -> None:

        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(f'api/execution-metadata/v2'
                                       f'/performances/{self._performance_id}/output-parameters/{parameter_id}/value/')
        body = {
            'value': parameter_value
        }
        logger.info(f'WRITE PARAMETER:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'PARAMETER_ID: {parameter_id}\n'
                    f'PARAMETER_VALUE: {parameter_value}\n'
                    f'PERFORMANCE_ID: {self._performance_id}\n')

        response = requests.post(url=url, json=body, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}\n')

        if response.status_code != 201:
            raise Exception(response.status_code)



