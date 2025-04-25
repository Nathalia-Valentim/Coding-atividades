'''
Lista de Compras
- Pergunte quantos itens o usuário quer adicionar (variável n).
- Em um for, peça ao usuário n vezes para digitar um item e faça
append() em compras.
- Ao final, exiba compras.
'''

# Solução
compras = []
n = int(input("Quantos itens deseja adicionar? "))

for _ in range(n):
    item = input("Digite o item: ")
    compras.append(item)

print("## Sua lista de compras ##")

for item in compras:
    print("- ", item)