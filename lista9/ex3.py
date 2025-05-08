'''
Soma de dois números com validação
Solicite dois números do usuário e mostre a soma. Caso o usuário digite qualquer
coisa que não seja um número, mostre um aviso e peça novamente.
'''

# Solução
while True:
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Soma: {a + b}")
        break

    except ValueError:
        print("Erro: Digite apenas números válidos.")