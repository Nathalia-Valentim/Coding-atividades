'''
Média de Notas
- Dada a lista notas (ex 8), use um for para calcular a média e exibir
“Média das notas: X”.
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
  
soma = 0

for nota in notas:
  soma += nota

media = soma / len(notas)

print(f"Média das notas: {media}")