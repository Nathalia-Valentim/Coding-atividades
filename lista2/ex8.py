'''
Maior ou Menor de Idade:
Solicite o ano de nascimento do usuário. Se o usuário tiver 18 anos ou
mais, exiba "Maior de idade"; caso contrário, "Menor de idade".
'''

# Solução
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2025 - ano_nascimento

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")