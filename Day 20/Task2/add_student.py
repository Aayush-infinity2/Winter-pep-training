import requests
import json
url = "http://127.0.0.1:8000/api/Students/"

data = {
    'name': 'Aayush',
    'age': 22,
    'course':'Machine Learning'
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(json.dumps(response.json(),indent=2))
