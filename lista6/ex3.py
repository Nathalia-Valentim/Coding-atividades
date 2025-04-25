'''
Senha com número limitado de tentativas
O usuário tem 3 tentativas para acertar a senha “fiap2025”. Após isso, exiba
“Acesso bloqueado”.
'''

# Solução
senha_correta = "fiap2025"

for tentativa in range(3):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido.")
        break
else:
    print("Acesso bloqueado.")