'''
Acesso a Caractere Específico:
Peça para o usuário digitar uma palavra e um número (índice) e mostre o
caractere da palavra na posição indicada.
'''

# Solução
palavra = input("digite uma palavra: ")
numero = int(input("Digite um número: "))

print(f"O caractere na posição {n} é: {palavra[numero]}")


palavra = input("digite uma palavra: ")
numero = int(input("Digite um número: "))

numero_int = int(numero)
caractere = palavra[numero_int]

print(caractere)

"""
if 0 <= n < len(palavra):
    print(f"O caractere na posição {n} é: {palavra[n]}")
else:
    print("Índice fora do intervalo válido.")
"""