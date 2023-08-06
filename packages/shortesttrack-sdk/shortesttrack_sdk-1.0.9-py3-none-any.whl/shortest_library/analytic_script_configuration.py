import os

from shortest_api_client.auth_helper import AuthHelper
from shortest_api_client.isasec_helper import ISASECHelper
from shortest_api_client.iss_connector import ISSConnector
from shortest_library.script_configuration import ScriptConfiguration

class ISSConnectionInfo:
    def __init__(self, info: dict) -> None:
        self.url = info.get('url')
        self.auth_custom_token = info.get('auth_custom_token')


class AnalyticScriptConfiguration(ScriptConfiguration):
    def __init__(self, isasec_id: str = os.getenv('ISASEC_ID'),
                 host: str = os.getenv('HOST', 'https://shortesttrack.com'),
                 refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')) -> None:

        self._isasec_id = isasec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._isasec = ISASECHelper(self._isasec_id).get_isasec(self._host, self._access_token.get())
        super().__init__(self._isasec['configuration_id'], host, refresh_token)

    def get_iss_connection_info(self) -> list:
        result = []
        for info in self._isasec['relations']:
            result.append(ISSConnectionInfo(info))
        return result

    def get_iss_connector(self, connection_info: ISSConnectionInfo) -> ISSConnector:
        connector = ISSConnector(url=connection_info.url,
                                 auth_custom_token=connection_info.auth_custom_token)

        return connector
