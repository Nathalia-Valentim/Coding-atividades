'''
Verificação de Resposta Sim/Não:
Peça ao usuário que responda a uma pergunta (ex.: "Você gosta de Python?") e
aceite apenas as respostas "sim" ou "não". Enquanto a resposta for diferente
dessas opções, continue perguntando.
'''

# Solução
resposta = ""

while resposta != "sim" or resposta != "não":
    resposta = input("Você gosta de Python? (sim/não): ").lower().strip().replace("ã", "a")

    if resposta == "sim":
        print("Ótimo")
        break
    elif resposta == "não":
        print("Que pena")
        break


# Solução do professor
while resposta != "sim" and resposta != "não":
    resposta = input("Você gosta de Python? (sim/não): ").lower().strip().replace("ã", "a")



while resposta not in ["sim", "não"]:
    resposta = input("Você gosta de Python? (sim/não): ")
    print(f"Você respondeu: {resposta}")