import json
import requests

import requests

url = "http://127.0.0.1:8000/employees-apiemployees/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

employees_data = json.loads(response.text)
print(employees_data)

salaries_lst = []

for employee in employees_data:
    salaries_lst += ([employee['salary']])
print(salaries_lst)

number_of_salaies = 0
total_salaries = 0

for salary in salaries_lst:
    number_of_salaies += 1
    total_salaries += salary

print(number_of_salaies)
print(total_salaries)

average_salary = total_salaries / number_of_salaies

print(average_salary)

import datetime

hire_dates_list = []

for employee in employees_data:
    hire_dates_list += (employee['first_name'], employee['hire_date'])

print(hire_dates_list)


today_date = datetime.date.today()
print(today_date)

