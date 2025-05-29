import json

def ola_json():
    print('Olá json')

dicionario = {"RM1234": 10}

with open('cadastro.json', 'w') as arquivo_cadastro:
    json.dump(dicionario, arquivo_cadastro)