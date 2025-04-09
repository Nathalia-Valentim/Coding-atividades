'''
Repetição do texto digitado
Peça para o usuário digitar um texto e mostre o texto digitado na tela (exemplo:
“Você digitou {texto}”). Repita essa operação enquanto o texto digitado
for diferente de “sair”.
'''

# Solução
while True: 
    texto = input("Digite um texto: ").lower()
    print(f"Você digitou {texto}")

    if texto == "sair":
        break