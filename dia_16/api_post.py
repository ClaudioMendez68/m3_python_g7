import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
  "userId": 1,
  "title": "titulo de ejemplo",
  "body": "Esto es un ejemplo de Body"
}

response = requests.post(url, json = payload)

if response.status_code == 201:
    print('Inserción exitosa')
    print(response.text)
else:
    print("Error en la creación del Post")
