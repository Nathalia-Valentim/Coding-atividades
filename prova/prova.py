#ex. 1
'''
for contagem_pares in range(2, 21, 2):
    print(contagem_pares)
'''

#ex. 2
'''
num = ""
while not num:
    try:
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
        if numero >= 1 and numero <= 10:
            print(f"Você digitou {numero}.")
            break
        else: 
            print(f"Você digitou {numero}, este número está fora do intervalo.")

    except ValueError:
        print("Você deve informar um número válido.")
'''

#ex. 3
'''
numeros = []

for i in range(5):
    calculo = int(input("Digite 5 números inteiros: "))
    numeros.append(calculo)
print(numeros)

soma = 0
for calculo in numeros:
    soma += calculo
print(f"Soma total: {soma}")

maior = max(numeros)
print(f"Maior valor: {maior}")

negativos = 0
for calculo in numeros:
    if calculo < 0:
        negativos += 1
print(f"Quantidade de números negativos: {negativos}")
'''

#ex. 4
'''
cores = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")

try:
    busca = int(input("Digite um número inteiro até 6: ")) 
    print(cores[busca])
except IndexError:
    print("Número fora do intervalo.")
except ValueError:
    print("Digite um número inteiro.")
'''

#ex. 5
'''
numeros = []
par_impar = {"pares": 0, "ímpares": 0}

try:
    for i in range(10):
        numeros.append(int(input("Digite um número: ")))
    print(numeros)

    for n in numeros:
        if n % 2 == 0:
            par_impar["pares"] += 1
        else:
            par_impar["ímpares"] += 1
    print(par_impar)

except ValueError:
    print("Digite um númro inteiro.")
'''

#ex. 6
'''
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")
    
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except ValueError:
    print("Digite um número.")
'''

#ex. 7
'''
numeros = []

while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ").strip()
    if entrada.lower() == "sair":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)

    except ValueError:
        print("Digite somente números")

if numeros:
    soma = sum(numeros)
    print(f"Soma: {soma}")

    media = soma / len(numeros)
    print(f"Média: {media}")
else:
    print("Nenhum número foi inserido.")
'''


#ex. 8
'''
estoque = {"caneta": 50, "caderno": 30, "borracha": 45}
produto = input("Qual produto deseja consultar? ").lower()

if produto in estoque:
    print(f"Estoque {estoque[produto]}")
else:
    print("Produto não cadastrada.")
'''