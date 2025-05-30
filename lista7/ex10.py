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

for pos, item in enumerate(tarefas, start = 1):
  print(f"{pos} - {item}")
  
## Até aqui o código é idêntico ao exercício 7.

indice_remover = int(input("Informe o número da tarefa a ser removida: "))

# O número da tarefa é sempre o índice mais um, portanto vamos remover um
# do item da lista para remover o item correto.

indice_remover -= 1

# O índice informado será inválido se for maior ou igual ao tamaho da lista
# ou se for negativo.
if indice_remover >= len(tarefas) or indice_remover < 0:
  print("Informe um índice válido.")
else:
  removido = tarefas.pop(indice_remover)
  print("Item removido: ", removido)