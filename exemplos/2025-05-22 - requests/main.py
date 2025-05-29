import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(r.status_code)

# import calculos

# resultado = calculos.soma(1, 2)

# print(resultado)


# import json

# json.ola_json()

# dicionario = {"RM1234": 10}

# with open('cadastro.json', 'w') as arquivo_cadastro:
#     json.dump(dicionario, arquivo_cadastro)





    # dicionario_str = str(dicionario)
    # cadastro.write(dicionario_str)
