'''
Média de Notas
- Dada a lista notas (ex 8), use um for para calcular a média e exibir
“Média das notas: X”.
'''

# Solução ???????????????????
alunos = []
notas = []

turma = int(input("Quantos alunos existem na turma M? "))

for _ in range(turma):
    alunos.append(input("Nome do aluno: "))

for _ in range(turma):
    notas.append(float(input("Nota do aluno: ")))

for nome, nota in zip(alunos, notas):
    print(f"{nome} -> {nota}")

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média das notas: {media}")