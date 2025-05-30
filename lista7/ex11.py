'''
Fatiamento da Lista de Compras
- Com a lista compras (ex 6), exiba apenas os 3 primeiros itens
usando slicing.
'''

# Solução
compras = []
n = int(input("Quantos itens você deseja adicionar? "))

for _ in range(n):
    item = input("Digite o item que quer adicionar: ")
    compras.append(item)

print("=> Sua lista de compras <=")

for item in compras:
    print("- ", item)

print("Exibindo os 3 primeiros itens da lista:")

for item in compras[:3]:
  print('-', item)