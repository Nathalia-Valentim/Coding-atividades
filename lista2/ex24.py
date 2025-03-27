'''
Recuperação ou Reprovação:
Solicite a nota e a frequência. Se a nota for menor que 6 e a frequência for
maior ou igual a 75, exiba "Faça a recuperação"; se a nota for menor que 6
e a frequência for menor que 75, exiba "Reprovado". Se a nota for maior
que 6 e a frequência maior que 75, exiba “Aprovado”.
'''

# Solução
nota = int(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência: "))

if nota < 6 and frequencia >= 75:
    print("Faça a recuperação")
elif nota < 6 and frequencia < 75:
    print("Repreovado")
else:
    print("Aprovado")