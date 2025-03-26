'''
Faixa de Temperatura:
Solicite a temperatura:
 - Acima de 30°C: "Muito quente"
 - Entre 15°C e 30°C: "Temperatura agradável"
 - Abaixo de 15°C: "Frio"
'''

# Solução
temperatura = float(input("Digite uma temperatura: "))

if temperatura > 30:
    print("Muito quente!")
elif temperatura >= 15:
    print("Temperatura agradável!")
else:
    print("Frio!")