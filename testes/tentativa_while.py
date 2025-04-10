# contar quantas vezes conta a palavra 'caminhão'
palavra_correta = "caminhão"
palavra_inserida = ""

total = 0

while palavra_inserida != "sair":
    palavra_inserida = input("Digite uma palavra: ").lower().strip()

    if palavra_inserida == palavra_correta:
        total += 1
    elif palavra_inserida == "sair":
        print(f"O total de vezes que você digitou caminhão é {total}")