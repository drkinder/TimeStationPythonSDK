# TimeStationPythonSDK

A python API wrapper for mytimestation.com, making it very easy to get up and running sending requests without having to spend much time learning the API.

## Installation

Not yet available via pip. Fork this repository to access.

## Usage

All method parameters can be found at the official mytimestation API documentation.
Pass the required parameters via a dictionary to the desired endpoints.

```python
from TimeStationPythonSDK import timestation 

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxx'
ts = TimeStation(API_KEY)

# All Employees Endpoints
ts.employees.list_employees()
ts.employees.single_employee(params={'employee_id': 'emp_ekj8x0q7p4'})
ts.employees.create_employee(params)
ts.employees.update_employee(params)
ts.employees.checkout_employee(params)
ts.employees.delete_employee(params)

# All Departments Endpoints
ts.departments.list_departments()
ts.departments.single_department(params={'employee_id': 'emp_ekj8x0q7p4'})
ts.departments.create_department(params)
ts.departments.update_department(params)
ts.departments.delete_department(params)

# All Shifts Endpoints
ts.shifts.list_shifts()
ts.shifts.single_shift(params={'employee_id': 'emp_ekj8x0q7p4'})
ts.shifts.create_shift(params)
ts.shifts.update_shift(params)
ts.shifts.close_shift(params)
ts.shifts.delete_shift(params)

# All Reports Endpoints
ts.reports.get_report(params) # Not yet implemented!
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2021 Dylan Kinder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
