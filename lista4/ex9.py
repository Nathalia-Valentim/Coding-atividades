'''
Contador com break:
Escreva um programa que conta de 1 até 10, mas para imediatamente se o
número for 7, usando break.
'''

# Solução
while True:
    numero = int(input("Digite um número: "))
    
    if numero < 1 or numero > 10:
        print("Por favor, digite um número entre 1 e 10.")
        continue
   
    elif numero == 7:
        print("Encerrando o programa.")
        break
 
    print(f"Você digitou: {numero}")