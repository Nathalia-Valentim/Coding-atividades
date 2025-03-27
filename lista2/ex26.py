'''
Acesso ao Sistema:
Solicite o login e a senha. Se o login for "admin" e a senha for "1234", exiba
"Acesso liberado"; senão, exiba "Acesso negado".
'''

# Solução
login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

if login == "admin" and senha == "1234":
    print("Acesso liberado")
else:
    print("Acesso negado")