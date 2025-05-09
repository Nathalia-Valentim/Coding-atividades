'''
Crie uma tupla com cinco nomes e verifique se um nome digitado pelo
usuário está presente na tupla.
'''

# Solução
nomes = ("Fred", "Daphne", "Velma", "Salsicha", "Scooby")
busca = input("Digite um nome e descubra se está na lista: ")

if busca in nomes:
    print(f"Nome {busca} encontrado")
else:
    print(f"Nome {busca} não encontrado")