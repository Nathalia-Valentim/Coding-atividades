'''
Ano Bissexto:
Solicite um ano e, se ele for divisível por 4 e (não divisível por 100 ou
divisível por 400), exiba "Ano bissexto".
(Utilize parênteses para deixar clara a precedência dos operadores.)
'''

# Solução
ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (not ano % 100 == 0 or ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é bissexto")


# Solução do professor
ano = int(input("Informe uma ano para saber se ele é bissexto:"))

divisivel_por_4 = ano % 4 == 0
divisivel_por_100 = ano % 100 == 0
divisivel_por_400 = ano % 400 == 0

if divisivel_por_4 and (not divisivel_por_100 or divisivel_por_400):
    print("Ano bissexto")
else:
    print("Não é bissexto")