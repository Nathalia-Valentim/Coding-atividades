'''
Clima do Dia:
Peça ao usuário para informar o tempo (ex.: "ensolarado", "nublado",
"chuvoso") e exiba uma mensagem específica para cada caso usando elif.
(Exemplo: se "ensolarado", exiba "Dia perfeito para sair"; se "chuvoso",
"Leve um guarda-chuva"; senão, "Aproveite o dia!")
'''

# Solução
tempo = input("Informe como está o tempo: ").lower()

if tempo == "ensolarado":
    print("Dia perfeito para sair")
elif tempo == "chuvoso":
    print("Leve um guarda-chuva")
else: 
    print("Aproveite o dia!")