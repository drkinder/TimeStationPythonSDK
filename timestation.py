from client import Client
from departments import Departments
from employees import Employees
from reports import Reports
from shifts import Shifts


class TimeStation:

    def __init__(self, bearer_token):

        headers = {
            'authorization': f"Bearer {bearer_token}"
        }
        self.client = Client(headers=headers)
        self.employees = Employees(self.client)
        self.departments = Departments(self.client)
        self.shifts = Shifts(self.client)
        self.reports = Reports(self.client)
