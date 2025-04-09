'''
Adivinhe o Número:
Escolha um número fixo (ex.: 7) e peça ao usuário para adivinhar. Enquanto a
resposta estiver errada, continue pedindo a adivinhação.
'''

# Solução
numero_fixo = 7
numero_escolhido = -1

while numero_escolhido != numero_fixo:
    numero_escolhido = int(input("Tente adivinhar o número: "))

    if numero_escolhido == numero_fixo:
        print("Acertou")
    else:
        print("Errou, tente novamente")