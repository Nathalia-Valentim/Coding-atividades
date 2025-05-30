'''
Imprimir apenas números pares de 1 a 50
Exiba os números pares entre 1 e 50 (inclusive). Use continue para ignorar os
ímpares.
'''

# Solução
for imprimir in range(1, 51):
    if imprimir % 2 != 0:
        continue
    print(imprimir)


# Solução do professor
for i in range(1, 51):
    if i % 2:
        continue
    print(i)