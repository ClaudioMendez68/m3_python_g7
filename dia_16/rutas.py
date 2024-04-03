from req import request_get

data = request_get('https://jsonplaceholder.typicode.com/photos') [0: 10]

for foto in data:
    print(foto)