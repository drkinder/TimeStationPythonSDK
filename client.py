import requests

from local.secrets import TIMESTATION_API_KEY


class Client:

    DEFAULT_OPTIONS = {
        'base_url': 'https://api.mytimestation.com/v1.1/',
    }

    def __init__(self, session=None, auth=None, **options):

        self.session = session or requests.Session()
        self.auth = auth
        self.headers = options.pop('headers', {})
        self.options = self._merge(self.DEFAULT_OPTIONS, options)

    def get(self, url, params={}, **options):
        """

        :param str url:
        :param dict params:
        :return:
        """
        response = requests.get(url, params, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.handle_http_error(response)

    def post(self, url, params={}, **options):
        """

        :param str url:
        :param dict params:
        :return dict:
        """
        response = requests.post(url, params, headers=self.headers)
        if response.status_code == 201:
            return response.json()
        else:
            self.handle_http_error(response)

    def put(self, url, params={}, **options):
        """

        :param str url:
        :param dict params:
        :return dict:
        """
        response = requests.put(url, params, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.handle_http_error(response)

    def delete(self, url, **options):
        """

        :param str url:
        :param dict params:
        :return dict:
        """
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.handle_http_error(response)

    @staticmethod
    def handle_http_error(response):
        error_message = response.json().get('error', {}).get('error_text', 'Unknown Error')
        raise KeyError(f"HTTP.Error.{response.status_code}: {error_message}")

    @staticmethod
    def _merge(*dicts):
        merged = {}
        for d in dicts:
            merged.update(d)
        return merged


if __name__ == '__main__':
    pass
