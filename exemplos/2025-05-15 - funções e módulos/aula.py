from calculos import calcular_idade
import os
from datetime import datetime

cumprimentar("Elvis", dia_semana = "sexta")

cumprimentar("Elvis", "Coding for security")
somar_dois_numeros(1, 2)

os.system("cls")

print(f"Hoje é {datetime.now()}")

nascimento = int(input("Qual seu ano de nascimento? "))
idade = calcular_idade(nascimento)

print(f"Idade: {idade}")