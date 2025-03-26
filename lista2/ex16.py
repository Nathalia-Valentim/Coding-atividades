'''
Número no Intervalo (10 a 20):
Solicite um número e, se ele estiver entre 10 e 20 (inclusive), exiba
"Número no intervalo".
'''

# Solução
numero = float(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print("Número no intervalo")
else:
    print("Número fora do intervalo")