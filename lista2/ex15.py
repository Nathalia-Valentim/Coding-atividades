'''
Classificação Etária:
Solicite a idade e classifique:
 - Menor que 12: "Criança"
 - Entre 12 e 17: "Adolescente"
 - Entre 18 e 64: "Adulto"
 - 65 ou mais: "Idoso"
'''

# Solução
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso")