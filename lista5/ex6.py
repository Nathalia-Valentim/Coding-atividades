'''
Letras maiúsculas e minúsculas
Peça para o usuário digitar uma palavra e conte quantas letras maiúsculas e
quantas letras minúsculas existem no texto informado.
'''

# Solução
palavra = input("Digite uma palavra: ")
maiusculas = 0
minusculas = 0

for letra in palavra:
    if letra.isupper():
        maiusculas += 1
    elif letra.islower():
        minusculas += 1

print(f"Maiúsculas: {maiusculas}")
print(f"Minúsculas: {minusculas}")
