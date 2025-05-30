'''
Número secreto com dica
Escolha um número entre 1 e 100 e atribua-o a uma variável. O usuário tenta
adivinhar e recebe dicas se deve tentar maior ou menor. O script termina somente
quando o usuário acertar o número ou digitar “desisto”. Se o usuário digitar
“desisto”, mostre qual era o número que ele deveria ter acertado.
'''

# Solução
numero_correto = "13"
numero_digitado = 0

while numero_digitado != "desisto":
    numero_digitado = input("Tente adivinhar oo número: ")

    if numero_digitado == "desisto":
        print(f"Você desistiu. O número era {numero_correto}")
        break

    elif numero_digitado < numero_correto:
        print("Tente um número maior")

    elif numero_digitado > numero_correto:
        print("Tente um número menor")

    else:
        print("Você acertou!")
        break


# Solução do professor
valor_correto = 45
valor = 0

while valor != valor_correto:
  valor = input("Tente adivinhar o número: ")
  
  if valor == "desisto":
    break
  
  valor = int(valor)
  
  if valor_correto > valor:
    print("Tente um valor maior")
  elif valor_correto < valor:
    print("Tente um valor menor")
else:
  print("Você acertou!")