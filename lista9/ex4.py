'''
Validação de senha numérica
Peça ao usuário uma senha que deve ser um número com exatamente 4 dígitos.
Mostre mensagem de erro se o valor for inválido (use len() e ValueError).
'''

# Solução
senha = input("Digite sua senha: ")

if len(senha) != 4:
    print("A senha tem 4 dígitos")
else:
    try:
        senha = int(senha)
        print("Senha válida")
    except ValueError:
        print("Digite apenas números")
        

###
'''
senha = input("Digite sua senha: ")

if senha.isnumeric() and len(senha) == 4:
    print("Senha válida")
else:
    print("Senha inválida")
'''

###
'''
try:
    senha = input("Digite sua senha: ")
    if len(senha) != 4 or not senha.isdigit():
        raise ValueError
    print("Senha válida!")

except ValueError:
    print("Erro: A senha deve conter exatamente 4 dígitos numéricos.")
'''