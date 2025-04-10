'''
Repetidor de palavras com break e continue:
Crie um programa que peça ao usuário para digitar palavras. O programa deve
funcionar da seguinte forma:
• Se a palavra for vazia, use continue para pular para a próxima interação sem
fazer nada.
• Se a palavra for "fim" (em minúsculas), use break para encerrar o
programa.
• Caso contrário, exiba a palavra digitada em maiúsculas.
'''

# Solução
while True:
    palavra = input("Digite uma palavra: ")
 
    if palavra == "":
        continue
    elif palavra == "fim":
        break
    else:
        print(palavra.upper())