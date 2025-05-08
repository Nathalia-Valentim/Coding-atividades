'''
Conversão de texto para inteiro
Peça ao usuário que digite um número inteiro. Se ele digitar texto ou número com
ponto, mostre uma mensagem de erro amigável usando ValueError.
'''

# Solução
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou: {numero}")
    
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido (sem letras ou pontos).")