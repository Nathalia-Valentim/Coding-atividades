'''
Crie um dicionário onde as chaves são nomes de produtos e os valores são
quantidades em estoque. Permita que o usuário "compre" um produto
(diminua o estoque), se ele existir.
'''

# Solução
estoque = {"arroz": 10, "feijão": 17, "macarrão": 8}

produto = input("Produto a comprar: ")

if produto in estoque and estoque[produto] > 0:
    estoque[produto] -= 1
    print(f"Compra realizada. Estoque restante de {produto}: {estoque[produto]}")
else:
    print("Produto não disponível.")