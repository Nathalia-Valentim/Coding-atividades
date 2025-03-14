'''
Operações Básicas:
Solicite dois números ao usuário e exiba, utilizando operações básicas, a
soma, subtração, multiplicação e divisão inteira dos números.
'''

# Solução
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao_inteira = int(num1) // int(num2)

print(f"A soma entre {num1} e {num2} é igual a: {soma}")
print(f"A subtração entre {num1} e {num2} é igual a: {subtracao}")
print(f"A multiplicação entre {num1} e {num2} é igual a: {multiplicacao}")
print(f"A dvisão entre {num1} e {num2} é igual a: {divisao_inteira}")