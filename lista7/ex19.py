'''
Mesclar Listas de Dois Usuários
- Cada usuário cria sua lista de compras (como no ex 6).
- Ao final, una as duas em compras_totais com + ou extend() e
exiba.
- A lista final não deve ter itens repetidos J.
'''

# Solução
lista1 = []
lista2 = []

# Lendo itens da lista 1
n = int(input("Quantos itens você vai comprar na lista 1? "))

for _ in range(n):
  item = input("Qual o nome do item que você vai comprar? ")
  lista1.append(item)
  
print('\n\n')

# Lendo itens da lista 2
n = int(input("Quantos itens você vai comprar na lista 2? "))

for _ in range(n):
  item = input("Qual o nome do item que você vai comprar? ")
  lista2.append(item)
  
# Mesclando as listas e removendo duplicatas
compras_totais = []
for item in lista1 + lista2:
  if item not in compras_totais:
    compras_totais.append(item)

print("\nLista final de compras (sem duplicatas):")
print(compras_totais)