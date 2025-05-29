import requests

payload = {"title": "aaaaa", "body": "asdfadsfasdf"}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

if 200 <= response.status_code < 300:
  print(response.json())
else:
  print('Ocorreu um erro.', response.status_code)