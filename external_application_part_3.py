import json
import requests

import requests

url = "http://127.0.0.1:8000/employees-apiemployees/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

