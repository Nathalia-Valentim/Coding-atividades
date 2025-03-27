'''
Aprovação do Aluno:
Solicite a nota e a frequência (em porcentagem) do aluno. Se a nota for
maior ou igual a 6 e a frequência for maior ou igual a 75, exiba "Aprovado".
'''

# Solução
nota = int(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência: "))

if nota >= 6 and frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")