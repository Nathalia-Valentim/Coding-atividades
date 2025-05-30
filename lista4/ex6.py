'''
Soma de Números:
Solicite que o usuário digite números repetidamente e, enquanto o número
digitado for diferente de 0, some os valores. Ao digitar 0, o loop encerra e a soma
total é exibida.
'''

# Solução
total = 0
numero = ""

while numero != 0:
    numero = int(input("Digite um número inteiro: "))
    #total = total + numero 
    total += numero
else:
    print(f"Total: {total}")


# Solução do professor
total = 0
num = -1

while num != 0:
  num = int(input("Informe um número para ser somado: "))
  total += num
  
print(f"Total: {total}")