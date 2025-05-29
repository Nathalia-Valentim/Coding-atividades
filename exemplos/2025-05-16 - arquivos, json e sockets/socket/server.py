"""
Servidor para comunicação através de socket.

Este é um exemplo rudimentar dos princípios de comunicação
através de sockets TCP em Python. Está longe de ser um 
código pronto para produção.

Referências úteis:
- https://docs.python.org/3.13/howto/sockets.html
- https://www.datacamp.com/pt/tutorial/a-complete-guide-to-socket-programming-in-python
"""
import socket

# Cria um socket para o servidor
# socket.AF_INET = IPv4
# socket.SOCK_STREAM = TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
porta = 8080

# Associa o IP e porta ao servidor, definindo em qual 
# porta o servidor vai "escutar"
servidor.bind( (ip, porta) )

servidor.listen()
print(f'Servidor escutando no ip {ip}:{porta}')

# servidor.accept() fica esperando algum cliente conectar
# na porta definida em servidor.bind().
# Quando um cliente conecta, o canal de comunicação entre
# cliente e servidor é armazenado na variável server_socket
server_socket, endereco_cliente = servidor.accept()

print(f"Socket estabelecido com o cliente {endereco_cliente}")

while True:
  # Fica esperando o recebimento de um pacote de até 1024 bytes
  msg_cliente = server_socket.recv(1024)

  # O dado recebido pelo socket vem em formato binário.
  # Por isso é necessário decodificar usando decode()
  print(msg_cliente.decode())