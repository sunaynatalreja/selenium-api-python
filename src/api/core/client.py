import requests
from src.api.constants import constants

class Client:
    def __init__(self):
        self.url = constants.API_URL

    def get(self,url):
        return requests.get(url)

    def get_with_query_parameters(self,params):
        return requests.get(self.url,params=params)

    def get_with_path_parameters(self,resource_id,param):
        url = f"{self.url}/{resource_id}/{param}"
        return requests.get(url)

    def post(self,url,request_json,headers=None):
        default_headers = {'content-type': 'application/json','x-api-key': 'reqres-free-v1'}
        final_headers = default_headers if headers is None else headers
        return requests.post(url,json=request_json,headers=final_headers)

    def put(self,data_json):
        return requests.put(self.url,json=data_json)

    def delete(self,url,headers=None):
        default_headers = {'content-type': 'application/json', 'x-api-key': 'reqres-free-v1'}
        final_headers = default_headers if headers is None else headers
        return requests.delete(url,headers=final_headers)

    def patch(self):
        return requests.patch(self.url)