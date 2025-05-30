'''
Validação de Senha (Tentativas):
Peça ao usuário para digitar uma senha correta (por exemplo, "abc123").
Enquanto a senha estiver incorreta, continue pedindo a senha. Ao acertar, exiba
"Senha correta!".
'''


senha_correta = "abcd1234"
senha_inserida = ""

while senha_inserida != senha_correta:
    senha_inserida = input("Digite a senha: ")

    if senha_inserida == senha_correta:
        print("Senha correta!")
    else: 
        print("Senha incorreta")


# Solução do professor
senha_correta = "abc123"
senha_informada = input("Qual a senha? ")

while senha_informada != senha_correta:
  senha_informada = input("Qual a senha? ")