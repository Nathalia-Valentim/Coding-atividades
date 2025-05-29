print('''
Escolha uma opção
1) Somar dois números
2) Subtrair dois números
3) Multiplicar dois números
''')

opcao = input("Digite a opção desejada: ")

match opcao:
    case "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma de {num1} com {num2} é {soma}")
    case "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        subtracao = num1 - num2
        print(f"A subtração de {num1} por {num2} é {subtracao}")
    case "3":
        print("Eslheu a opção 3")
    case _:
        print("Opção inválida")

print(f"Opção digitada: {opcao}")

'''
if opcao == "1" or opcao == "um":
    print("Eslheu a opção 1")
elif opcao == "2" or opcao == "dois":
    print("Escolheu a opção 2")
elif opcao == "3" or opcao == "três": 
    print("Escolheu a opção 3")
else:
    print("Opção inválida")
'''