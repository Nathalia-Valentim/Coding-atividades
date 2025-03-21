'''
Contém a Letra 'a':
Solicite uma palavra e, se ela contiver a letra "a" (maiúscula ou minúscula),
exiba "Contém a letra a!".
'''

# Solução
palavra = input("Digite uma palavra: ")

if 'a' in palavra.lower() or 'a' in palavra.upper():
    print("Contém a letra a!")
else:
    print("Não contém a letra a!")