'''
Crie um dicionário com o nome de três alunos e suas respectivas notas.
Depois, calcule a média geral.
'''

# Solução
notas = {"Lukas": 8.5, "Scarlett": 9.0, "Olive": 10.0}
media = sum(notas.values()) / len(notas)

print(f"Média geral: {media:.2f}")