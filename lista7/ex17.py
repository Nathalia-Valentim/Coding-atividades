'''
Ordenar e Inverter Lista de Números
- Pergunte ao usuário quantos números (k) e leia-os em nums.
- Use sort() para ordenar e imprima.
- Depois use reverse() e imprima novamente.
'''

# Solução
numeros = []
k = int(input("Quantos números deseja inserir? "))

for _ in range(k):
    numeros.append(int(input("Digite um número: ")))

numeros.sort()
print("Ordenado:", numeros)

numeros.reverse()
print("Invertido:", numeros)


# Solução do professor
k = int(input("Quantos números você vai digitar? "))
nums = []

for _ in range(k):
  nums.append(int(input("Informe um número")))

print("Esses são os números informados:", nums)

# O .reverse() altera a lista original
nums.reverse()

print("Esses são os números informados ao contrário:", nums)