'''
Verificação de Caracteres na Senha:
Solicite uma senha e, se ela contiver pelo menos um dos caracteres "!",
"@" ou "#" e além disso tiver mais de 10 caracteres exiba "Senha forte".
'''

# Solução
senha = input("Digite uma senha: ")

if "!" in senha or "@" in senha or "#" in senha and len(senha) > 10:
    print("Senha forte")
else: 
    print("Senha fraca")