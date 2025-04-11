'''
Repetição de uma frase
Peça para o usuário digitar uma frase e um número inteiro, que representa a
quantidade de vezes que essa frase deverá ser exibida na tela. Exiba a frase que o
usuário digitou na tela, o número de vezes que ele informou.
'''

# Solução
frase = input("Digite a frase: ")
qnt_vezes = int(input("Quantas vezes: "))

for contador in range(0, qnt_vezes):
    print(frase)