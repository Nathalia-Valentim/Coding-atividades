'''
Alunos e Notas
- Pergunte quantos alunos existem na turma (m).
- Em um loop, leia m nomes para alunos e em outro leia m notas
(floats) para notas.
- No final, percorra os dois paralelamente e mostre como nesse
exemplo:
    Maria → 8.5
    Bruno → 7.0
'''

# Solução
alunos = []
notas = []

turma = int(input("Quantos alunos existem na turma M? "))

for _ in range(turma):
    alunos.append(input("Nome do aluno: "))

for _ in range(turma):
    notas.append(float(input("Nota do aluno: ")))

for nome, nota in zip(alunos, notas):
    print(f"{nome} -> {nota}")