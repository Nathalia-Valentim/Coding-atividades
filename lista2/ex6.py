'''
Par ou Ímpar:
Solicite um número inteiro. Se o número for par, exiba "Par"; caso
contrário, exiba "Ímpar".
'''

# Solução
num = int(input("Digigte um número inteiro: "))

if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")