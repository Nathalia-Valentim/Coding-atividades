'''
with open("nome_arquivo.txt", "w") as arquivotexto:
    arquivotexto.write("Qualquer texto dentro do arquivo")
'''
import os

with open("comandos.txt", "r") as meuarquivo:
    conteudo_arquivo = meuarquivo.read()
    os.system(conteudo_arquivo)

'''
import os

with open("comandos.txt", "r") as meuarquivo:
    conteudo_arquivo = meuarquivo.read()
    os.system(conteudo_arquivo)
'''