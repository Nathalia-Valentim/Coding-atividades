'''
Número Positivo e Par:
Peça um número e, se ele for positivo e par, exiba "Número positivo e par".
'''

# Solução

numero = int(input("Digite um numero inteiro: "))

if numero > 0 and numero % 2 == 0:
    print("Número positivo e par")
elif numero < 0:
    print("Número negativo")
elif numero % 2 == 1:
    print("Número ímpar")