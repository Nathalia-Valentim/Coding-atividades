'''
Verificador de número primo
Peça um número e diga se ele é primo.
'''

# Solução
numero = int(input("Digite um número: "))

# Um número será primo se ele for divisível APENAS por 1 e por ele mesmo.
# Vamos fazer um loop do número informado até 1 e ver se o valor informado
# é divisível por algum outro número.

for i in range(numero-1, 1, -1):
  
  if numero % i == 0:
    print(f"O número {numero} NÃO é primo.")
    break
  
else:
  # Se o for concluir sem ser interrompido pelo break, significa que não foi
  # encontrado nenhum outro número cujo resto da divisão resultasse em 0.
  print(f"O número {numero} é primo!")