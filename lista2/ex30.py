'''
Bolsa de Estudos:
Solicite a média do aluno, a renda familiar e se participa de atividades
extracurriculares ("sim" ou "não"). Condições para ser elegível para bolsa:
 - média for maior ou igual a 8 e renda for menor que 3000
 - média for maior ou igual a 7 e participação for "sim"
Se o aluno atende a qualquer um desses dois critérios, exiba "Elegível para
a bolsa". Caso contrário exiba "Não elegível para bolsa"
'''

# Solução
media_aluno = float(input("Digite sua média: "))
renda_familiar = float(input("Informe sua renda familiar: "))
extracurriculares = input("Participa de alguma atividade extracurricular: ")

if (media_aluno >= 8 and renda_familiar < 3000) or (media_aluno >= 7 and extracurriculares == "sim"):
    print("Elegível para a bolsa")
else:
    print("Não elegível para a bolsa")