'''
Tamanho da Lista
- Peça ao usuário para digitar nomes de alunos e armazene esses
nomes em uma lista chamada nomes. Quando o usuário pressionar
enter sem informar um nome, exiba quantos nomes foram digitados
e uma lista numerada com esses nomes.
'''

# Solução
nomes = []

aluno = input("Digite o nome do aluno (ou entre para sair): ")

while aluno != "":
    nomes.append(aluno)
    aluno = input("Digite o nome do aluno (ou entre para sair): ")

print(f"Foram digitados {len(nomes)} nomes")

pos = 1

for elem in nomes:
    print(f"{pos} - {elem}")
    pos += 1