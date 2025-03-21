'''
Validação de Senha:
Peça uma senha ao usuário e compare com uma senha pré-definida (por
exemplo, "seguro123"). Se for igual, exiba "Acesso concedido!"; senão,
"Acesso negado!".
'''

# Solução
senha_definida = "senhasegura123"
senha_digitada = input("Digite uma senha: ")

if senha_definida == senha_digitada:
    print("Acesso concedido!")
else: 
    print("Acesso negado!")