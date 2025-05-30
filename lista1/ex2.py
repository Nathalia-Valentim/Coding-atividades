'''
Contagem de Caracteres:
Solicite que o usuário digite uma frase, remova os espaços extras no início e
fim com .strip() e mostre o tamanho da frase usando len().
'''

# Solução
frase = input("Digite uma frase: ")
print(len(frase.strip()))


# Solução do professor
frase = input("Digite uma frase: ")
frase_sem_espaco = frase.strip()

caracteres = len(frase_sem_espaco)
print(caracteres)