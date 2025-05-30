'''
Substituição de Palavras:
Crie um programa que receba uma frase e substitua todas as ocorrências da
palavra "JavaScript" por "Python" usando o método .replace().
'''

# Solução
frase = input("Digite alguma coisa com JavaScript: ")
print(f"{frase}".replace("JavaScript", "Python"))


# Solução do professor
frase = input("Digite uma frase: ")

frase_sem_javascript = frase.replace("JavaScript", "Python")
print(frase_sem_javascript)