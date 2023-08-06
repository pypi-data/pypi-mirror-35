
import urllib3
import requests
import json

from .kpi_client_exception import KpiClientException


class Dot4ClientConfig(object):
    def __init__(self, dot4_mandant, dot4_user, dot4_password, dot4_api_url=None):
        self.dot4_mandant = dot4_mandant
        self.dot4_user = dot4_user
        self.dot4_password = dot4_password
        if dot4_api_url is None:
            self.dot4_api_url = 'https://api.dot4.de'
        else:
            self.dot4_api_url = dot4_api_url


class Dot4Client(object):
    def __init__(self, config):
        self.__config = config

    def create_kpi_repository_apikey(self, apikey_name, apikey_expire_date):
        dot4AccessToken = self.__get_dot4_access_token()
        url = self.__config.dot4_api_url + '/api/apiKey'

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "authorization": 'Bearer ' + dot4AccessToken
        }

        payload = {
            "name": apikey_name,
            "expireDate": apikey_expire_date,
            "apiType": 1
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)

        if response.status_code != 200:
            message = 'HTTP Errorcode: ' + str(response.status_code) + '\n' + 'POST Error: ' + response.text
            raise KpiClientException(response.status_code, message)

        return json.loads(response.text)

    def __get_dot4_access_token(self):
        url = self.__config.dot4_api_url + '/token'
        username = 'Dot4\\' + self.__config.dot4_mandant + '\\' + self.__config.dot4_user
        payload = {
            'grant_type': 'password',
            'username': username,
            'password': self.__config.dot4_password
        }

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)

        if response.status_code != 200:
            message = 'HTTP Errorcode: ' + str(response.status_code) + '\n' + 'POST Error: ' + response.text
            raise KpiClientException(response.status_code, message)

        json_data = json.loads(response.content)
        return json_data.get('access_token')
