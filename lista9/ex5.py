'''
Loop com validação até valor correto
Crie um loop que só termina quando o usuário digitar um número inteiro válido.
Use while + try/except.
'''

# Solução
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou: {numero}")
        break
    
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
