import os

nomes = ["João", "Maria", "Antônio"]

# Verifica se o arquivo existe antes de ler
if os.path.exists('exemplo_aula.txt'):
  
  texto = input("Digite algo para ser salvo no arquivo: \n> ")

  while texto.lower() != 'salvar':
    
    with open('exemplo_aula.txt', 'a') as arquivo:
      # Abre o arquivo para leitura
      arquivo.write(texto + '\n')
      
    texto = input("Digite algo para ser salvo no arquivo: \n> ")
      

else:
  print('Arquivo NÃO existe')
  