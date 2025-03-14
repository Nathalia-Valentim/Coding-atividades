'''
Verificação de Substring:
Crie um programa com a frase pré-definida “Coding for cybersecurity, do
curso de defesa cibernética na FIAP” e peça ao usuário digitar uma palavra.
Verifique se essa palavra está presente na frase (utilizando o operador in) e
informe o resultado. O texto deve ser encontrado mesmo se as maiúsculas ou
minúsculas do texto informado pelo usuário forem diferentes.
'''

# Solução
frase = "Coding for cybersecurity, do curso de defesa cibernética na FIAP".lower()
palavra = input("Digite uma palavra: ").lower()

print(palavra in frase)


frase = "Coding for cybersecurity, do curso de defesa cibernética na FIAP"
frase_minusculas = frase.lower()

palavra = input("Digite uma palavra: ")
palavra_minusculas = palavra.lower()

print(palavra_minusculas in frase_minusculas)