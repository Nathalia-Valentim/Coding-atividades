'''
Contagem Regressiva:
Peça ao usuário para informar um número inteiro positivo e realize uma contagem
regressiva até 0.
'''

# Solução
numero = int(input("Digite um número inteiro para a contagem regressiva: "))

while numero >= 0:
    print(numero)
    numero -= 1