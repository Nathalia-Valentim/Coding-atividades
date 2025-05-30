'''
Participação em Sorteio:
Solicite a idade e se o usuário já participou de um sorteio ("sim" ou "não").
Se a idade for maior ou igual a 18 e a resposta for "não", exiba "Pode
participar do sorteio".
'''

# Solução
idade = int(input("Digite sua idade: "))
sorteio = input("Já participou de um sorteio: ").lower()

if idade >= 18 and sorteio == "não":
    print("Pode participar do sorteio")
else:
    print("Não pode participar do sorteio")