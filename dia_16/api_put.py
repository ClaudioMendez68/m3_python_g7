import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "userId": 1,
  "title": "titulo de ejemplo 2",
  "body": "Esto es otro ejemplo de Body"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("PUT", "/posts/1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))