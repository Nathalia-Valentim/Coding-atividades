'''
Desconto para Idosos ou Clientes com Cartão:
Solicite a idade e se o cliente possui cartão de desconto ("sim" ou "não").
Se a idade for 65 ou mais ou se o cliente tiver o cartão, exiba "Desconto
aplicado".
'''

# Solução
idade = int(input("Digite sua idade: "))
cartao = input("Possui cartão de desconto?: ").lower()

if idade >= 65 or cartao == "sim":
    print("Desconto aplicado")
else:
    print("Não foi possível aplicar o desconto")