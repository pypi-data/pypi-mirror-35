import os

from shortest_api_client.auth_helper import AuthHelper
from shortest_api_client.sec_helper import SECHelper
from shortest_api_client.perfomance_helper import PerfomanceHelper

class ScriptConfiguration:
    def __init__(self,
                 sec_id: str = os.getenv('CONFIGURATION_ID'),
                 host: str = os.getenv('HOST', 'https://shortesttrack.com'),
                 refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')) -> None:

        self._sec_id = sec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._sec = SECHelper(self._sec_id).get_sec(self._host, self._access_token.get())

    def read_parameters(self):
        result = {}
        params = self._sec['parameters']
        for p in params:
            result[p['id']] = p['value']

        return result

    def write_parameter(self, parameter_id, parameter_value):
        perfomance = PerfomanceHelper(config_id=self._sec_id,
                                      perfomance_id=os.getenv('PERFOMANCE_ID'))

        perfomance.write_parameter(parameter_id=parameter_id,
                                   parameter_value=parameter_value,
                                   host=self._host,
                                   access_token=self._access_token.get())

