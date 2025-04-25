'''
Verificador de número primo
Peça um número e diga se ele é primo.
'''

# Solução
numero = int(input("Digite um número: "))

if numero < 2:
    print("Não é primo.")
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("Não é primo.")
            break
    else:
        print("É primo.")
