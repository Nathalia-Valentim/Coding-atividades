'''
Mostre cada letra da string "Coding for Security" em uma linha usando while
'''

frase = "Coding for Security"
total_letras = len(frase)

posicao_atual = 0

while posicao_atual < total_letras:
    print( frase[posicao_atual] )
    posicao_atual += 1

print("")


'''
frase = input("Digite uma frase: ")

for letra in frase:
    print(letra)
'''


frase = "Aula sobre loop"
vezes_a = 0

for letra in frase:
    if letra.lower() == "a":
        vezes_a += 1

print(f"A letra 'A' aparece {vezes_a} vez(es)")





'''
or - 
and - 
'''