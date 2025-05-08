'''
Script com menu de opções
Mostre um menu de opções para o usuário e peça para ele escolher uma das
alternativas. Depois que o usuário informa a opção escolhida, realize a operação
indicada no menu.
Caso o usuário digite uma opção inválida, deve ser exibida uma mensagem
“Opção inválida”.
Este é o menu que deve ser exibido ao usuário:
Opções:
1) Somar dois números
2) Subtrair dois números
3) Multiplicar dois números
4) Dividir dois números
5) Verificar se um número informado é par
6) Calcular a idade de um usuário a partir do seu ano de nascimento
7) Calcular a idade média de 3 pessoas, a partir dos seus anos de
nascimento
8) Descubra se um número está entre 20 e 100
9) Identifique se o aluno foi aprovado, com base na nota (mínimo 7) e
na frequência (mínimo 75)
10) Verifique se a senha informada é forte (mínimo 10 caracteres,
incluindo !, @, #, $ ou %)
Escolha uma opção:
'''

# Solução
print('''
Escolha uma opção:
1) Somar dois números
2) Subtrair dois números
3) Multiplicar dois números
4) Dividir dois números
5) Verificar se um número informado é par
6) Calcular a idade de um usuário a partir do seu ano de nascimento
7) Calcular a idade média de 3 pessoas, a partir dos seus anos de nascimento
8) Descubra se um número está entre 20 e 100
9) Identifique se o aluno foi aprovado, com base na nota (mínimo 7) e na frequência (mínimo 75)
10) Verifique se a senha informada é forte (mínimo 10 caracteres incluindo !, @, #, $ ou %)
''')

def somar_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma do {num1} com {num2} é {soma}")

def subtrair_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    subtracao = num1 - num2
    print(f"A subtração do {num1} com {num2} é {subtracao}")

def multiplicar_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    multiplcacao = num1 * num2
    print(f"A multiplicação de {num1} por {num2} é {multiplicacao}")

def dividir_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    divisao = num1 / num2
    print(f"A divisão de {num1} por {num2} é {divisao}")

def numero_par():
    numero_par = int(input("Digite um número: "))
    if numero_par % 2 == 0:
        print(f"{numero_par} é par")
    else:
        print(f"{numero_par} é ímpar")

def calcular_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = 2025 - ano_nascimento
    print(f"Você tem {idade} anos")

def calcular_idade_media():
    ano1 = int(input("Digite o ano de nascimento da primeira pessoa: "))
    ano2 = int(input("Digite o ano de nascimento da segunda pessoa: "))
    ano3 = int(input("Digite o ano de nascimento da terceira pessoa: "))

    idade1 = 2025 - ano1
    idade2 = 2025 - ano2
    idade3 = 2025 - ano3

    idade_media = (idade1 + idade2 + idade3) / 3
    print(f"A idade média das três pessoas é {idade_media} anos")

def numero_entre():
    numero = float(input("Digite um número: "))
    if numero >= 20 and numero <= 100:
        print(f"{numero} está entre 20 e 100")
    else:
        print(f"{numero} não está entre 20 e 100")

def aprovacao():
    nota = float(input("Digite sua nota: "))
    frequencia = float(input("Digite sua frequência: "))
    if  nota >= 7 and frequencia >= 75:
        print("Aprovado")
    else:
        print("Reprovado")

def senha_forte():
    senha = input("Digite a senha: ")
    if ("!" in senha or "@" in senha or "#" in senha or "$" in senha or "%" in senha) and len(senha) > 10:
        print("Senha forte")
    else:
        print("Senha fraca")

opcao = input("Digite a opção desejada: ")

match opcao :
    case "1":
        somar_dois_numeros()

    case "2":
        subtrair_dois_numeros()

    case "3":
        multiplicar_dois_numeros()

    case "4":
        dividir_dois_numeros()

    case "5":
        numero_par()

    case "6":
        calcular_idade()

    case "7":
        calcular_idade_media()
        
    case "8":
        numero_entre()

    case "9":
        aprovacao()

    case "10":
        senha_forte()
            
    case _:
        print("Opção inválida")