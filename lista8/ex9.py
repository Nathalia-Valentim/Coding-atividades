'''
Crie um dicionário com três frutas e seus preços. Peça ao usuário uma
fruta e informe o preço ou uma mensagem de erro se a fruta não estiver
cadastrada.
'''

# Solução
frutas = {"mamão": 4.0, "laranja": 0.50, "morango": 8.0}
fruta = input("Qual fruta deseja consultar? ")

if fruta in frutas:
    print(f"Preço: R$ {frutas[fruta]}")
else:
    print("Fruta não cadastrada.")