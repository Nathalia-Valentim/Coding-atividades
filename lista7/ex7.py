'''
Lista de Tarefas
- Pergunte quantas tarefas o usuário tem hoje.
- Num loop, leia cada tarefa e adicione a tarefas.
- Depois, imprima todas as tarefas numeradas:
    1. Lavar a louça
    2. Estudar Python
'''

# Solução
tarefas = []
n_tarefas = int(input("Quantas tarefas você tem hoje? "))

for _ in range(n_tarefas):
    tarefa = input("Qual a próxima tarefa? ")
    tarefas.append(tarefa)

for pos, item in enumerate(tarefas):
    print(f"{pos+1} - {item}")


# Solução do professor
tarefas = []
n_tarefas = int(input("Quantas tarefas você tem hoje? "))

for _ in range(n_tarefas):
  tarefa = input("Qual a próxima tarefa? ")
  tarefas.append(tarefa)

for pos, item in enumerate(tarefas, start = 1):
  print(f"{pos} - {item}")