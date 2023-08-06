
import urllib3
import requests
import json

from .kpi_client_exception import KpiClientException
from .kpi_definition import KpiDefinition
from .kpi_values import KpiValues, KpiValuesEncoder
from .kpi_client_exception import KpiClientException
from .service import Service


class KpiRepositoryClient(object):
    def __init__(self, apikey, dot4_mandant=None, kpi_repository_url=None):
        if kpi_repository_url is not None:
            self.__kpi_repository_url = kpi_repository_url
        elif dot4_mandant is not None:
            self.__kpi_repository_url = 'https://ai.dot4.de/saasqMain/' + dot4_mandant + '/kpirepository'
        else:
            raise KpiClientException(0, 'Parameter dot4_mandant must be specified.')

        self.__apikey = apikey
        self.__access_token = self.__getKpiRepositoryAccessToken()

    def create_kpi_definition(self, kpi_definition):
        json_data = self.create_kpi_definition_from_dict(kpi_definition.to_json())
        return KpiDefinition(json_data)

    def create_kpi_definition_from_dict(self, kpi_definition_dict):
        response = self.__retry_request('POST', '/api/kpi-definition/', kpi_definition_dict)
        json_response = json.loads(response.content)
        return json_response["data"]

    def delete_kpi_definition(self, uuid):
        self.__retry_request('DELETE', '/api/kpi-definition/' + uuid)

    def get_all_kpi_definitions(self):
        response = self.__retry_request('GET', '/api/kpi-definition')
        json_response = json.loads(response.content)
        json_data = json_response["data"]
        return [KpiDefinition(d) for d in json_data]

    def get_kpi_definition(self, uuid):
        response = self.__retry_request('GET', '/api/kpi-definition/' + uuid)
        json_response = json.loads(response.content)
        json_data = json_response["data"]
        return KpiDefinition(json_data)

    def add_kpi_values(self, service_uid, values):
        dataDict = dict(values)
        dataDict['serviceUid'] = service_uid
        self.add_kpi_values_from_dict(json.dumps(dataDict))

    def add_kpi_values_from_dict(self, values_dict):
        self.__retry_request('POST', '/api/service/customkpi', values_dict)

    def import_kpi_values(self, service_uid, import_values):
        data = json.dumps({'serviceUid': service_uid, 'kpis': import_values}, cls=KpiValuesEncoder)
        self.import_kpi_values_from_dict(data)

    def import_kpi_values_from_dict(self, import_values_dict):
        self.__retry_request('POST', '/api/service/customkpi-collection', import_values_dict)

    def get_all_services(self):
        response = self.__retry_request('GET', '/api/service')
        json_response = json.loads(response.content)
        json_data = json_response["data"]
        return [Service(d) for d in json_data]

    def __retry_request(self, mode, url_suffix, data=None):
        url = self.__kpi_repository_url + url_suffix

        newAcccessToken = False
        if self.__access_token is None:
            self.__access_token = self.__getKpiRepositoryAccessToken()
            newAcccessToken = True

        headers = {
            'content-type': 'application/json',
            'authorization': 'Bearer ' + self.__access_token
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request(mode, url, data=data, headers=headers, verify=False)
        if response.status_code == 200:
            return response

        if newAcccessToken or (response.status_code != 400 and response.status_code != 401):
            KpiRepositoryClient.__throwResponseException(response, mode)

        self.__access_token = self.__getKpiRepositoryAccessToken()
        headers['authorization'] = 'Bearer ' + self.__access_token
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request(mode, url, data=data, headers=headers, verify=False)
        if(response.status_code != 200):
            self.__access_token = None
            KpiRepositoryClient.__throwResponseException(response, mode)

        return response

    def __getKpiRepositoryAccessToken(self):
        url = self.__kpi_repository_url + '/api/get-token'
        payload = {
            "apiKey": self.__apikey
        }

        headers = {
            "content-type": 'application/json'
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)

        if response.status_code != 200:
            message = 'HTTP Errorcode: ' + str(response.status_code) + '\n' + 'POST Error: ' + response.text
            raise KpiClientException(response.status_code, message)

        json_response = json.loads(response.content)
        json_data = json_response["data"]
        return json_data.get("access_token")

    @classmethod
    def __throwResponseException(cls, response, mode):
        message = 'HTTP Errorcode: ' + str(response.status_code) + '\n' + mode + ' Error: ' + response.text
        raise KpiClientException(response.status_code, message)
