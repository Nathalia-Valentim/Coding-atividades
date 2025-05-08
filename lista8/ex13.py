'''
Crie um dicionário com o nome de três usuários e seus perfis (ex: “admin”,
“convidado”, etc). Liste apenas os nomes que são do tipo “admin”.
'''

# Solução
usuarios = {"Galalol": "admin", "CapMafioso": "convidado", "CEO": "admin"}

for nome, perfil in usuarios.items():
    if perfil == "admin":
        print(nome)