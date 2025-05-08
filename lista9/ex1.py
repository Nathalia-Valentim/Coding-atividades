'''
Divisão segura
Peça dois números ao usuário e mostre o resultado da divisão. Use try/except
para evitar divisão por zero.
'''

# Solução
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")