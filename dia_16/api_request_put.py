import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = json.dumps({
    "userId": 1,
    "title": "titulo de ejemplo 2",
    "body": "Esto es otro ejemplo de Body"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response)
print(response.text)