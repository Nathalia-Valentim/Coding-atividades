'''
Acesso com Documento:
Solicite a idade e se o usuário possui documento ("sim" ou "não"). Se a
idade for maior ou igual a 18 e a resposta for "sim", exiba "Acesso
permitido".
'''

# Solução
idade = int(input("Digite sua idade: "))
documento = input("Possui documento?: ").lower()

if idade >= 18 and documento == "sim":
    print("Acesso permitido")
else: 
    print("Acesso negado")