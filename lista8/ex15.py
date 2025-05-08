'''
Peça para o usuário digitar 3 nomes e 3 idades, salve os dados em um
dicionário e, ao final, mostre quem é o mais velho e quem é o mais novo.
'''

# Solução
dados = {"nomes": [], "idades": []}

for _ in range(3):
    dados["nomes"].append(input("Nome: "))
    dados["idades"].append(int(input("Idade: ")))

mais_velho = dados["nomes"][dados["idades"].index(max(dados["idades"]))]
mais_novo = dados["nomes"][dados["idades"].index(min(dados["idades"]))]

print(f"Mais velho: {mais_velho}")
print(f"Mais novo: {mais_novo}")