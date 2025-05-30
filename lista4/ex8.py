'''
Repetição de uma Frase:
Solicite ao usuário que digite uma frase e, em seguida, pergunte quantas vezes ele
deseja ver essa frase. Use while para exibir a frase o número de vezes solicitado.
'''

# Solução
frase = input("Digite uma frase: ")
vezes = int(input("Quantas vezes você deseja ver a frase? "))
 
repetir = 0
 
while repetir < vezes:
    print(frase)
    repetir = repetir + 1


# Solução do professor
frase = input("Digite uma frase: ")
vezes = int(input("Quantas vezes você deseja ver a frase? "))

while vezes > 0:
    print(frase)
    vezes = vezes - 1
