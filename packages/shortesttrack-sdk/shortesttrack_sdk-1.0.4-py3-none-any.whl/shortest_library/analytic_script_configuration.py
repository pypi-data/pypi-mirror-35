import os

from shortest_api_client.auth_helper import AuthHelper
from shortest_api_client.isasec_helper import ISASECHelper
from shortest_api_client.iss_connector import ISSConnector


class ISSConnectionInfo:
    def __init__(self, info: dict) -> None:
        self.url = info.get('url')
        self.auth_custom_token = info.get('auth_custom_token')


class AnalyticScriptConfiguration:
    def __init__(self) -> None:
        self._aisc_id = os.getenv('AISC_ID')
        self._host = os.getenv('HOST', 'https://shortesttrack.com')
        self._refresh_token = os.getenv('SEC_REFRESH_TOKEN')
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)

    def get_iss_connection_info(self) -> list:
        isasec = ISASECHelper(self._aisc_id).get_isasec(self._host, self._access_token.get())
        result = []
        for info in isasec['relations']:
            result.append(ISSConnectionInfo(info))
        return result

    def get_iss_connector(self, connection_info: ISSConnectionInfo) -> ISSConnector:
        connector = ISSConnector(url=connection_info.url,
                                 auth_custom_token=connection_info.auth_custom_token)

        return connector
