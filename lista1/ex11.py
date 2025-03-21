'''
Conversão de String para Número e Vice-Versa:
Peça para o usuário digitar um número em formato de string, converta-o para
inteiro e, depois, converta-o novamente para string. Exiba os dois resultados.
'''

# Solução
numero_usuario = input("Digite um número: ")

numero_int = int(numero_usuario)
numero_str = str(numero_int)

print(numero_int, numero_str)