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
