'''
Converter para String CSV
- Peça ao usuário quantos itens (n) e depois n valores em itens.
- Construa uma única string separada por vírgulas sem usar join():
em um loop, acrescente item + ',' e no final remova a vírgula
extra.
- Exiba algo como:
banana,leite,ovos,manteiga
'''

# Solução
numero = int(input("Quantos itens deseja inserir? "))
itens = []

for _ in range(numero):
    itens.append(input("Digite um item: "))

csv = ""
for item in itens:
    csv += item + ","
csv = csv[:-1]

print(csv)