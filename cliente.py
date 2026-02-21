
import socket

cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 5000))

name = input("ingresa tu nombre: ")
cliente.sendall(name.encode())

response = cliente.recv(1024).decode()
print(response)

cliente.close()
