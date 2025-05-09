'''
Repetição do texto digitado
Peça para o usuário digitar um texto e mostre o texto digitado na tela (exemplo:
“Você digitou {texto}”). Repita essa operação enquanto o texto digitado
for diferente de “sair”.
'''

# Solução
frase = input("Dgite um texto: ").lower().strip()

while frase != "sair":
    print(f"Você digitou {frase}")
    frase = input("Dgite um texto: ").lower().strip()

'''
while True: 
    texto = input("Digite um texto: ").lower()
    print(f"Você digitou {texto}")

    if texto == "sair":
        break
'''