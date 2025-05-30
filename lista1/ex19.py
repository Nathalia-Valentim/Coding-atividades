'''
Comprimento do Nome:
Peça para o usuário digitar seu nome e utilize a função len() para exibir
quantos caracteres esse nome possui.
'''

# Solução
nome = input("Digite seu nome: ").strip()
comprimento_nome = len(nome)

print(f"O nome {nome} possui {comprimento_nome} caracteres.")