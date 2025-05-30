'''
16.Vogais vs. Consoantes
- Peça uma frase ao usuário, transforme em lista de caracteres.
- Conte, em dois contadores, quantas vogais (aeiouAEIOU) e quantas
consoantes (letras alfabeticamente mas não vogais) existem.
- Exiba:
    Vogais: 10, Consoantes: 15
'''

# Solução
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

cont_vogais = 0
cont_consoantes = 0

for letra in frase:
    if letra in vogais:
        cont_vogais += 1
    elif letra in consoantes:
        cont_consoantes += 1

print(f"Vogais: {cont_vogais}, Consoantes: {cont_consoantes}")