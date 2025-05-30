'''
Substituição de Elemento
- Em frutas = ['maçã', 'banana', 'laranja'], substitua 'banana'
por 'uva' e exiba a lista atualizada.
'''

# Solução
frutas = ['maçã', 'banana', 'laranja']

frutas[1] = 'uva'
print(frutas)


# Solução do professor
frutas = ['maçã', 'banana', 'laranja']

indice = frutas.index("banana")
frutas[indice] = 'uva'
print(frutas)