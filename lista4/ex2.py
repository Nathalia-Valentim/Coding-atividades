'''
Repetir Até Acertar uma Palavra:
Peça ao usuário para digitar a palavra "seguro". Enquanto o usuário não digitar
exatamente essa palavra, continue pedindo.
'''

# Solução
palavra_correta = "seguro"
entrada = ""

while entrada != palavra_correta:
    entrada = input("Digite a palavra 'seguro': ").lower()
