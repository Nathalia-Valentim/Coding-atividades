'''
Classificação de Notas:
Peça a nota do aluno e classifique:
 - Nota ≥ 90: "Conceito A"
 - Nota ≥ 80: "Conceito B"
 - Nota ≥ 70: "Conceito C"
 - Abaixo de 70: "Conceito D"
'''

# Solução
nota = float(input("Digite sua nota: "))

if nota >= 90 and nota <= 100:
  print("Sua nota é A")
elif nota >= 80 and nota < 90:
  print("Sua nota é B")
elif nota >= 70 and nota < 80:
  print("Sua nota é C")
elif nota < 70 and nota > 0: 
  print("Sua nota é D")
else:
  print("Não é possível reconhecer esse valor")


# Solução do professor
nota = int(input("Qual a nota do aluno? "))

if nota >= 90:
  print("Conceito A")
elif nota >= 80:
  print("Conceito B")
elif nota >= 70:
  print("Conceito C")
else:
  print("Conceito D")