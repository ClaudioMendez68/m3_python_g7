import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print(response)

if response.status_code == 200:
    print(response.text)
    respuesta = json.loads(response.text)
    print(type(respuesta))
    
    #for clave, valor in respuesta.items():
    #    print(f'{clave} - {valor}')
else:
    print('Error en la solicitud', response.status_code)
        
results = json.loads(response.text)

# print(results)
# print(type(results))
# print(results[0].keys())
# print(results[0]['userId'])
# print(results[0]['title'])

# print([post['title'] for post in results])