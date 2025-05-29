'''
def mostra_ola_mundo():
    print("Olá Mundo!")

mostra_ola_mundo()
'''

##

def cumprimentar(nome_usuario, nome_disciplina = "Coding", dia_semana = "sexta"):
    print(f"Bom dia, {nome_usuario}!")
    print(f"Seja bem vindo(a) à aula de {nome_disciplina}")
    print(f"Hoje é {dia_semana}")

cumprimentar("Love", dia_semana = "terça")

##

def somar_dois_numeros(num1, num2):
    print(num1+num2)

somar_dois_numeros(1, 2)

##

def calcular_idade(ano_nascimento):
    print(2025-ano_nascimento)

calcular_idade(
    int(input("Digite o ano que nasceu: "))
)

##

def calcular_idade(ano_nascimento):
    return 2025-ano_nascimento

idade = calcular_idade(2000)
print(f"Idade: {idade}")

##
