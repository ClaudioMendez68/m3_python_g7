import requests, json
from string import Template

def get_request (url):
    return json.loads(requests.get(url).text)

response = get_request('https://jsonplaceholder.typicode.com/photos')[: 5]
print(len(response))

# print(response[0].keys())
# print(response[0])

image_template = Template('<img src = "$url">')
"""
imagen = image_template.substitute(url = 'Hola Mundo')
print(imagen)
"""
html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html''')

lista_url = []
for elemento in response:
    lista_url.append(elemento['url'])    
# print(lista_url)

# lista_url = [elemento['url'] for elemento in response]

texto_img = ''
for url in lista_url:
    texto_img+= image_template.substitute(url = url)+'\n'
    
print(texto_img)