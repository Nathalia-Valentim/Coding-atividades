'''
Contador com break:
Escreva um programa que conta de 1 até 10, mas para imediatamente se o
número for 7, usando break.
'''

# Solução
cont = 1

while cont <= 10:
  print(cont)
  cont +=1
  
  if cont == 7:
    break