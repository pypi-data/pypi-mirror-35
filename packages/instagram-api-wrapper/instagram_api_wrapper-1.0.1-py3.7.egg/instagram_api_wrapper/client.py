import json

import requests

from instagram_api_wrapper.exceptions import InstagramApiError


class InstagramApi:
    host = 'https://api.instagram.com/v1'

    class ApiEndpoints(object):
        user_info = '/users/self'
        user_media = '/users/self/media/recent'

    def __init__(self, access_token=None):
        self.access_token = access_token

    def get_user_info(self):
        return self._send_request(url=self.ApiEndpoints.user_info, params=self._prepare_data())

    def get_user_media(self, data=None):
        return self._send_request(url=self.ApiEndpoints.user_media, params=self._prepare_data(data))

    def _send_request(self, url, params=None):
        params = params or {}
        request_url = self._prepare_url(url=url)
        response = requests.get(request_url, params=params)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise InstagramApiError("Request error. Status code {}".format(response.status_code))

    def _prepare_url(self, url):
        return '{}/{}'.format(self.host.rstrip('/'), url.lstrip('/'))

    def _prepare_data(self, data=None):
        data = data or {}
        data['access_token'] = self.access_token
        return data
