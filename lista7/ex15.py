'''
Mesclando listas de convidados de dois eventos
Você está organizando dois workshops e tem duas listas de convidados
separadas.
    1. Peça ao usuário quantos convidados vão ao Workshop A (nA), em
seguida leia nA nomes (um por vez) e armazene na lista convidados_A.
    2. Peça ao usuário quantos convidados vão ao Workshop B (nB),
depois leia nB nomes e armazene em convidados_B.
    3. Crie uma nova lista todos_convidados que contenha todos os
nomes de convidados_A seguidos dos nomes de convidados_B,
usando o método extend().
    4. Exiba a lista todos_convidados, numerando cada participante:
'''

# Solução
convidados_A = []
convidados_B = []

nA = int(input("Quantos conivdados vão ao Workshop A?: "))
for _ in range(nA):
    convidadoA = input("Nomes dos convidados A: ")
    convidados_A.append(convidadoA)

nB = int(input("Quantos conivdados vão ao Workshop B?: "))
for _ in range(nB):
    convidadoB = input("Nomes dos convidados A: ")
    convidados_B.append(convidadoB)

todos_convidados = []
todos_convidados.extend(convidados_A)
todos_convidados.extend(convidados_B)

for i, nome in enumerate(todos_convidados, 1):
    print(f"{i}. {nome}")