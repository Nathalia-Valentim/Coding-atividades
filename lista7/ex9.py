'''
Remover Item por Nome
- Usando a lista compras do exercício 6, peça ao usuário um item para
remover.
- Se existir, chame remove() e exiba “Item removido.”; senão, exiba
“Item não encontrado.”
- Mostre a lista atualizada.
'''

# Solução
compras = []
n = int(input("Quantos itens você vai comprar? "))

for _ in range(n):
  item = input("Qual o nome do item que você vai comprar? ")
  compras.append(item)

print("=> Sua lista de compras <=")

for item in compras:
  print("- ", item)

## Até aqui o código é idêntico ao exercício 6.
## Daqui pra frente vamos mostrar a opção de remover um item da lista.

print("=> Removendo um item <=")

item_remover = input("Qual item você quer remover? ")

if item_remover in compras:
  compras.remove(item_remover)
else:
  print("Item não encontrado.")

print("Lista de compras atual: ")
for item in compras:
  print("- ", item)