

class Departments:

    def __init__(self, client):
        self.client = client
        self.url = self.client.options.get('base_url')

    def list_departments(self, params={}, **options):
        """

        :param dict params:
        :return: list of dictionaries with all department information
        """
        url = f"{self.url}/departments"
        if response := self.client.get(url, params, **options):
            return response

    def single_department(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        department_id = params.get('department_id')
        url = f"{self.url}/departments/{department_id}"
        if response := self.client.get(url, params, **options):
            return response

    def create_department(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        url = f"{self.url}/departments"
        if response := self.client.post(url, params, **options):
            return response

    def update_department(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        department_id = params.pop('department_id')
        url = f"{self.url}/departments/{department_id}"
        if response := self.client.put(url, params, **options):
            return response

    def delete_department(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        department_id = params.pop('department_id')
        url = f"{self.url}/departments/{department_id}"
        if response := self.client.delete(url, **options):
            return response
