"""
Cliente para comunicação através de socket.

Este é um exemplo rudimentar dos princípios de comunicação
através de sockets TCP em Python. Está longe de ser um 
código pronto para produção.
"""
import socket

# Cria um socket para o cliente, com as mesmas características
# do servidor
# socket.AF_INET = IPv4
# socket.SOCK_STREAM = TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Especifica o IP e porta onde o cliente vai se conectar
ip_servidor = "127.0.0.1"
porta_servidor = 8080

# Tenta estabelecer uma conexão com o servidor
cliente.connect( (ip_servidor, porta_servidor) )

text = ""

while text.lower() != "desconectar":
  text = input("> ")
  
  # Envia o que o usuário digitou para o servidor, através
  # do socket estabelecido na variável 'cliente'.
  # A comunicação via rede exige a conversão do texto para
  # binário, e é isso que o método .encode() faz.
  cliente.send(text.encode())