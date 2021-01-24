

class Shifts:

    def __init__(self, client):
        self.client = client
        self.url = self.client.options.get('base_url')

    def list_shifts(self, params={}, **options):
        """

        :param dict params:
        :return: list of dictionaries with all shift information
        """
        url = f"{self.url}/shifts"
        if response := self.client.get(url, params, **options):
            return response

    def single_shift(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        department_id = params.get('shift_id')
        url = f"{self.url}/shifts/{department_id}"
        if response := self.client.get(url, params, **options):
            return response

    def create_shift(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        url = f"{self.url}/shifts"
        if response := self.client.post(url, params, **options):
            return response

    def update_shift(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        shift_id = params.pop('shift_id')
        url = f"{self.url}/shifts/{shift_id}"
        if response := self.client.put(url, params, **options):
            return response

    def close_shift(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        shift_id = params.pop('shift_id')
        url = f"{self.url}/shifts/{shift_id}/close"
        if response := self.client.put(url, params, **options):
            return response

    def delete_shift(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        shift_id = params.pop('shift_id')
        url = f"{self.url}/shifts/{shift_id}"
        if response := self.client.delete(url, **options):
            return response
