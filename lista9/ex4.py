'''
Validação de senha numérica
Peça ao usuário uma senha que deve ser um número com exatamente 4 dígitos.
Mostre mensagem de erro se o valor for inválido (use len() e ValueError).
'''

# Solução ???????????????
try:
    senha = input("Digite sua senha (apenas 4 números): ")
    if len(senha) != 4 or not senha.isdigit():
        raise ValueError
    print("Senha válida!")

except ValueError:
    print("Erro: A senha deve conter exatamente 4 dígitos numéricos.")
