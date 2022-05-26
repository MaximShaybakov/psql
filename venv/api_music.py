#API VK
import requests
import json
from pprint import pprint

class API_VK():

    def __init__(self):
        self.url = 'https://api.vk.com/method/'

    def _token(self):
        with open('t.txt') as file:
            TOKEN = file.readline().strip()
            return TOKEN


    def _get_params(self):
        return {
            'access_token': f'{self._token()}',
            'user_id': '',
            'extended': 1,
            'filter': 'admin,groups,publics',
            'count': 5,
            'v': '5.131',
        }

    def resp(self):
        response = requests.get(url=self.url + 'groups.get', params=self._get_params(), timeout=5)
        pprint(response.status_code)
        pprint(response.json()['response']['items'])
        return response.json

if __name__ == '__main__':
    User1 = API_VK()
    User1.resp()
