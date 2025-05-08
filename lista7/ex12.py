'''
Iterar com Índice
- Para a lista tarefas (ex 7), use for i in range(len(tarefas)): e
imprima a lista de tarefas como no exemplo:
    Tarefa 1: lavar a louça
    Tarefa 2: estudar Python
'''

# Solução
tarefas = []
n_tarefas = int(input("Quantas tarefas você tem hoje? "))

for _ in range(n_tarefas):
    tarefa = input("Qual a próxima tarefa? ")
    tarefas.append(tarefa)

for i in range(len(tarefas)):
    print(f"Tarefa {i + 1}: {tarefas[i]}")