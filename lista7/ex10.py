'''
Remover Item por Índice
- Usando a lista tarefas do exercício 7, peça um índice ao usuário.
- Use pop() para remover e imprimir o item removido (ou exiba
mensagem de erro se o índice for inválido).
'''

# Solução
tarefas = []
n_tarefas = int(input("Quantas tarefas você tem hoje? "))

for _ in range(n_tarefas):
    tarefa = input("Qual a próxima tarefa? ")
    tarefas.append(tarefa)

for pos, item in enumerate(tarefas):
    print(f"{pos+1} - {item}")

indice = int(input("Digite o índice da tarefa que deseja remover: ")) -1

if 0 <= indice < len(tarefas):
    t_removida = tarefas.pop(indice)
    print(f"Tarefa removida: {t_removida}")
else: 
    print("Inválido")