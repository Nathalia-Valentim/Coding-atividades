print('''S para solteiro
C para casado
D para divorciado
V para viúvo''')

estado_civil = input("Digite a letra que corresponda ao seu estado civil: ").upper().strip()

if estado_civil == "S":
    print("Você é solteiro")
elif estado_civil == "C":
    print("Você é casado")
elif estado_civil == "D":
    print("Você é divorciado")
elif estado_civil == "V":
    print("Você é viúvo")
else:
    print("Opção inválida")