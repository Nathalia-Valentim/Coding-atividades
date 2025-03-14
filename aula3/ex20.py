'''
Relatório de Operações:
Peça ao usuário digitar dois números e, utilizando f-strings, exiba uma
mensagem formatada mostrando o resultado de:
● Soma
● Subtração
● Multiplicação
● Divisão inteira (//)
● Resto da divisão (%)
'''

# Solução
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao_inteira = num1 // num2
resto_divisao = num1 % num2

print(f"A soma entre os dois números é igual: {soma}")
print(f"A subtração entre os dois números é igual: {subtracao}")
print(f"A multiplicação entre os dois números é igual: {multiplicacao}")
print(f"A divisão inteira entre os dois números é igual: {divisao_inteira}")
print(f"O resto da divisão entre os dois números é igual: {resto_divisao}")