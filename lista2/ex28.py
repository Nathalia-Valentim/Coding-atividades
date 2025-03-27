'''
Promoção de Produto:
Solicite o preço do produto e se ele está em estoque ("sim" ou "não"). Se o
preço for menor que 50 e o produto estiver em estoque, exiba "Produto em
promoção".
'''

# Solução
preco = float(input("Digite o preço do produto: "))
produto_estoque = input("O produto está em estoque: ").lower()

if preco < 50 and produto_estoque == "sim":
    print("Produto em promoção")