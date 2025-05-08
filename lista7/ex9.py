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
itens = int(input("Quantos itens você deseja adicionar? "))

for _ in range(itens):
    item = input("Digite o item que quer adicionar: ")
    compras.append(item)

print("=> Sua lista de compras <=")

for pos, item in enumerate(compras):
    print(f"{pos+1} - {item}")

item = input("Digite o item que deseja remover: ")

if item in compras:
    compras.remove(item)
    print("Item removido.")
else:
    print("Item não encontrado.")
    
print(compras)