'''
Autorização para Votar:
Solicite a idade e se o usuário possui impedimento para votar ("sim" ou
"não"). Se a idade for maior ou igual a 16 e a resposta for "não", exiba "Pode
votar".
'''

# Solução
idade = int(input("Digite sua idade: "))
impedimento = input("Possui impedimento para votar?: ").lower()

if idade >= 16 and impedimento == "não":
    print("Pode votar")
else:
    print("Não pode votar")