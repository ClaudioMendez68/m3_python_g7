import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {} # Cuando enviemos datos (post o put), aquí agregaremos los datos que enviaremos
headers = {} # Aquí irían el formato o tipos de datos que enviaríamos

# response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url)
print(response)

if response.status_code == 200:
    # print(response.text)
    print(response.json())
    respuesta = response.json()
    print('')
    print(respuesta['title'])
    print('')
    for clave, valor in respuesta.items():
        print(f'{clave} - {valor}')
else:
    print('Error en la solicitud', response.status_code)
        
results = json.loads(response.text)

# print(results)
# print(type(results))
# print(results[0].keys())
# print(results[0]['userId'])
# print(results[0]['title'])

# print([post['title'] for post in results])