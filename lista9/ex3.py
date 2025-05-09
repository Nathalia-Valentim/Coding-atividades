'''
Soma de dois números com validação
Solicite dois números do usuário e mostre a soma. Caso o usuário digite qualquer
coisa que não seja um número, mostre um aviso e peça novamente.
'''

# Solução
num1 = num2 = ""

while not num1 or not num2:
  try:
    num1 = float(input("Informe um número para somar: "))
    num2 = float(input("Informe outro número para somar: "))
  except ValueError:
    print("Você deve informar um número válido. Tente novamente.")
else:
  print(f"{num1} + {num2} = {num1+num2}")
