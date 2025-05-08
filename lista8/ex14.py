'''
Crie um sistema de cadastro simples que armazena informações de várias
pessoas usando um dicionário com listas como valores (ex: "nomes": [],
"idades": [], etc.).
'''

# Solução
cadastro = {"nomes": [], "idades": [], "cidades": []}

for _ in range(3):
    cadastro["nomes"].append(input("Nome: "))
    cadastro["idades"].append(int(input("Idade: ")))
    cadastro["cidades"].append(input("Cidade: "))

print(cadastro)