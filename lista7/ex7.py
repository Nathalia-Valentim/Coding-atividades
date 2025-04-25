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

'''
tarefas = []
n_tarefas = int(input("Quantas tarefas você tem hoje? "))

for _ in range(n_tarefas):
    tarefa = input("Qual a próxima tarefa? ")
    tarefas.append(tarefa)

contador = 1

for item in tarefas:
    print(f"{contador} - {item}")
    contador += 1
'''