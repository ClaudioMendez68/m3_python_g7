import requests
# import json

url = "https://jsonplaceholder.typicode.com/posts"

"""
payload = json.dumps({
    "userId": 1,
    "title": "titulo de ejemplo",
    "body": "Esto es un ejemplo de Body"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
"""
payload = {
    "userId": 1,
    "title": "titulo de ejemplo",
    "body": "Esto es un ejemplo de Body"
}

response = requests.post(url, data = payload)

print(response)
print(response.text)