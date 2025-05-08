'''
Mesclar Listas de Dois Usuários
- Cada usuário cria sua lista de compras (como no ex 6).
- Ao final, una as duas em compras_totais com + ou extend() e
exiba.
- A lista final não deve ter itens repetidos J.
'''

# Solução
compras1 = []
compras2 = []

for _ in range(int(input("Quantos itens na lista 1? "))):
    compras1.append(input("Item: "))

for _ in range(int(input("Quantos itens na lista 2? "))):
    compras2.append(input("Item: "))

compras_totais = list(set(compras1 + compras2))
print("Lista final:", compras_totais)