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
qtd_alunos = int(input("Quantos alunos há na turma? "))
nomes = []
notas = []

for i in range(qtd_alunos):
  nome = input("Informe o nome do aluno: ")
  nota = float(input(f"Informe a nota do aluno {nome}: "))
  
  nomes.append(nome)
  notas.append(nota)

for i in range(qtd_alunos):
  print(f"{nomes[i]} -> {notas[i]}")