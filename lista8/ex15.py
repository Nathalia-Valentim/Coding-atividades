'''
Peça para o usuário digitar 3 nomes e 3 idades, salve os dados em um
dicionário e, ao final, mostre quem é o mais velho e quem é o mais novo.
'''

# Solução
pessoas = {}

for _ in range(0, 3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoas[nome] = idade

idade_mais_novo = 120
idade_mais_velho = 0
nome_mais_novo = nome_mais_velho = ""

for nome_pessoa in pessoas:
    idade_pessoa = pessoas[nome_pessoa]

    if idade_pessoa < idade_mais_novo:
        nome_mais_novo = nome_pessoa
        idade_mais_novo = idade_pessoa
    elif idade_pessoa > idade_mais_velho:
        nome_mais_velho = nome_pessoa
        idade_mais_velho = idade_pessoa

print(f"A pessoa mais nova é {nome_mais_novo} com {idade_mais_novo} anos")
print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velho} anos")

###
'''
dados = {"nomes": [], "idades": []}

for _ in range(3):
    dados["nomes"].append(input("Nome: "))
    dados["idades"].append(int(input("Idade: ")))

mais_velho = dados["nomes"][dados["idades"].index(max(dados["idades"]))]
mais_novo = dados["nomes"][dados["idades"].index(min(dados["idades"]))]

print(f"Mais velho: {mais_velho}")
print(f"Mais novo: {mais_novo}")
'''