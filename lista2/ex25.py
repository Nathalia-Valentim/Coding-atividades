'''
Aposentadoria:
Solicite o ano de nascimento e o tempo de contribuição. Condições para
aposentadoria:
 - Se a idade for maior ou igual a 65
 - Idade for maior ou igual a 60 e tempo de contribuição for maior ou
igual a 30)
Exiba "Pode se aposentar" se uma dessas condições for satisfeita.
'''

# Solução
ano_nascimento = int(input("Informe o ano de nascimento: "))
idade = 2025 - ano_nascimento

if idade >= 65:
    print("Aposentadoria concedida por idade")
    exit()

contribuicao = int(input("Informe o tempo de contribuição: "))

if idade >= 60 and contribuicao >= 30:
    print("Aposentadoria concedida por tempo de contribuição")
else:
    print("Não pode se aposentar")