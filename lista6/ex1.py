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

for letra in frase:
    if letra in vogais or letra in vogais.upper():
        n_vogais += 1
  
    if letra in consoantes or letra in consoantes.upper():
        n_consoantes += 1
    
    if letra.islower():
        n_minusculas += 1
    
    if letra.isupper():
        n_maiusculas += 1

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
print(f"Maiúsculas: {cont_maiusculas}")
print(f"Minúsculas: {cont_minusculas}")