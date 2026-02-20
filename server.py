import socket

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

print("servidor esperando conexion...")

conn, addr = server.accept()
print("estudiante conectado:", addr)

conn.sendall(b"hola juan felipe")
conn.close()

