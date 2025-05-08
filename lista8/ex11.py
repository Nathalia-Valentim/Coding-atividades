'''
Peça ao usuário para informar o nome de uma pessoa e uma cidade.
Armazene essas informações em um dicionário. Permita que ele atualize
a cidade, se desejar.
'''

# Solução
nome = input("Digite seu nome: ")
cidade = int(input("Digite sua cidade: "))

dados = {"nome": nome, "cidade": cidade}

atualizar = input("Deseja atualizar a cidade?(s/n) ")

if atualizar.lower() == "sim" or atualizar == "s":
    dados["cidade"] = input("Nova cidade: ")

print(dados)