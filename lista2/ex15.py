'''
Classificação Etária:
Solicite a idade e classifique:
 - Menor que 12: "Criança"
 - Entre 12 e 17: "Adolescente"
 - Entre 18 e 64: "Adulto"
 - 65 ou mais: "Idoso"
'''

# Solução
idade = int(input("Informe a idade: "))

if idade >= 0 and idade < 12:
  print("Criança")
elif idade >=12 and idade < 18:
  print("Adolescente")
elif idade >=18 and idade < 65:
  print("Adulto")
elif idade >= 65:
  print("Idoso")
else:
  print("Que idade é essa??")