'''
Soma de números pares em um intervalo
Peça dois números inteiros ao usuário. Mostre o resultado da soma de todos os
números pares neste intervalo (incluindo os números informados pelo usuário, se
forem pares). O script deve funcionar adequadamente mesmo que o usuário
informe primeiro um número maior que o segundo.
Exemplo: o usuário informa primeiro o número 80 e depois o número 20. Você
deve somar todos os pares entre 20 e 80, incluindo o 20 e o 80.
'''

# Solução
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

inicio = min(num1, num2)
fim = max(num1, num2)

soma = 0
for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

print(f"Soma dos pares entre {inicio} e {fim} = {soma}")


# Solução do professor
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))

# Vamos inicializar a variável que vai armazenar a soma de todos os valores
total = 0

# Se o num2 for maior que num1, vamos inverter os valores
# para atender à última parte do enunciado.
# Durante o script, vamos trabalhar com as variáveis 'inicio' e 'fim',
# e não com num1 e num2.
if num1 <= num2:
  inicio = num1
  fim = num2
else:
  inicio = num2
  fim = num1

# Vamos criar um loop de 'inicio' até 'fim' (inclusive), e acumular
# a soma na variável 'soma' se o número for par

for num in range(inicio, fim+1):
  
  if not num % 2:
    total += num

print(f"A soma dos números pares entre {inicio} e {fim} é {total}")