

class Employees:

    def __init__(self, client):
        self.client = client
        self.url = self.client.options.get('base_url')

    def list_employees(self, params={}, **options):
        """

        :param dict params:
        :return: list of dictionaries with all employee information
        """
        url = f"{self.url}/employees"
        if response := self.client.get(url, params, **options):
            return response

    def single_employee(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        employee_id = params.pop('employee_id')
        url = f"{self.url}/employees/{employee_id}"
        if response := self.client.get(url, params, **options):
            return response

    def create_employee(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        url = f"{self.url}/employees"
        if response := self.client.post(url, params, **options):
            return response

    def update_employee(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        employee_id = params.pop('employee_id')
        url = f"{self.url}/employees/{employee_id}"
        if response := self.client.put(url, params, **options):
            return response

    def checkout_employee(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        employee_id = params.pop('employee_id')
        url = f"{self.url}/employees/{employee_id}/check-out"
        if response := self.client.put(url, params, **options):
            return response

    def delete_employee(self, params={}, **options):
        """

        :param dict params:
        :return:
        """
        employee_id = params.pop('employee_id')
        url = f"{self.url}/employees/{employee_id}"
        if response := self.client.delete(url, **options):
            return response


