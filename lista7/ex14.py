'''
Contar Ocorrências
- Peça ao usuário uma palavra e use list(palavra) para transformá-
la em lista de caracteres.
- Conte quantas vezes aparece a letra 'a' (maiúscula ou minúscula)
usando um loop e count manual (não método .count()).
'''

# Solução
palavra = input("Digite uma palavra: ").lower()
lista = list(palavra)
contador = 0

for letra in lista:
    if letra.lower() == 'a':
        contador += 1

print(f"Ocorrências da letra 'a': {contador}")