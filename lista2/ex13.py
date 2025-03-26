'''
Desempenho do Aluno:
Solicite uma pontuação (0 a 100):
 - Pontuação ≥ 85: "Excelente"
 - Entre 70 e 84: "Bom"
 - Entre 50 e 69: "Regular"
 - Abaixo de 50: "Insuficiente"
'''

# Solução
pontuacao = int(input("Digite sua pontuação: "))

if pontuacao >= 85:
    print("Pontuação Excelente")
elif pontuacao >= 70:
    print("Pontuação Boa")
elif pontuacao >= 50:
    print("Regular")
else:
    print("Insuficiente")