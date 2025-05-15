import calculos
import os
import datetime

os.system("cls")
print(f"Hoje é {datetime.datetime.now()}")

nascimento = int(input("Qual seu ano de nascimento? "))
idade = calculos.calcular_idade(nascimento)

print(f"Idade: {idade}")

'''
from calculos import calcular_idade

nascimento = int(input("Qual seu ano de nascimento? "))
idade = calcular_idade(nascimento)

print(f"Idade: {idade}")
'''