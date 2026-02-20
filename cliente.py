
import socket

cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 5000))

mensaje = cliente.recv(1024)
print("estudiante: ", mensaje.decode())

cliente.close()
