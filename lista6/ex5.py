'''
Tabuada personalizada
Peça um número e mostre a tabuada de multiplicação de 1 a 10 do valor
informado.
'''

# Solução
numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")