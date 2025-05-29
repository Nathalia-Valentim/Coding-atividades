import requests

URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(URL)

if 200 <= response.status_code < 300:
  usuarios = response.json()
  
  for usuario in usuarios:
    print('-', usuario['name'] )
  
else:
  print('Erro na requisição', response.status_code)