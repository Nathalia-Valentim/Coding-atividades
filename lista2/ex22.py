'''
Número Dentro do Intervalo (1 a 100) com Not:
Solicite um número e, se não for menor que 1 e não for maior que 100,
exiba "Número dentro do intervalo de 1 a 100". Utilize o operador not para
simplificar a condição.
'''

# Solução
numero = float(input("Digite um número: "))

if not numero < 1 and not numero > 100:
    print("Número dentro do intervalo de 1 a 100")
else:
    print("Número fora do intervalo de 1 a 100")