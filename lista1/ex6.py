'''
Arredondamento:
Peça para o usuário digitar um número decimal (float) e exiba esse número
arredondado para uma casa decimal usando a função round().
'''

# Solução
numero = float(input("Digite um número decimal: "))
print(round(numero))


# Solução do professor
numero_str = input("Digite um número decimal: ")

numero_float = float(numero_str)
numero_round = round(numero_float, 1)
print(numero_round)