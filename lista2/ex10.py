'''
Texto Vazio ou Não:
Solicite ao usuário que digite um texto. Se o usuário não digitar nada, exiba
"Nenhum texto digitado"; caso contrário, "Texto recebido".
'''

# Solução
texto = input("digite um texto: ")

if not texto:
    print("Nenhum texto digitado")
else:
    print("Texto recebido")