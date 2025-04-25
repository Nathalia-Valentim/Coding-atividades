'''
Contar vogais, consoantes, maiúsculas e minúsculas em uma string
Peça uma frase ao usuário e informe a quantidade de vogais, consoantes,
caracteres maiúsculos e minúsculos. Repare que números ou caracteres
especiais não podem ser classificados em maiúscula, minúscula, vogal ou
consoante. Portanto, desconsidere esses caracteres.
'''

# Solução
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

cont_vogais = 0
cont_consoantes = 0
cont_maiusculas = 0
cont_minusculas = 0

for char in frase:
    if char.isalpha():
        if char in vogais:
            cont_vogais += 1
        elif char in consoantes:
            cont_consoantes += 1
        if char.isupper():
            cont_maiusculas += 1
        elif char.islower():
            cont_minusculas += 1

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
print(f"Maiúsculas: {cont_maiusculas}")
print(f"Minúsculas: {cont_minusculas}")