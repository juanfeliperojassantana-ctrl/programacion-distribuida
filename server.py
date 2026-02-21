import socket
import threading
import time 

contador_clientes = 0 #recurso compartido
lock = threading.Lock()

def handle_client(conn, addr):
	global contador_clientes

	name=  conn.recv(1024).decode()
	time.sleep(50)
	#seccion critica protegida
	#incremento del contador
	with lock:
		contador_clientes += 1
		numero = contador_clientes

	print(f"cliente {contador_clientes} atendido desde {addr}")

	response = f"hola {name}, eres el cliente numero {contador_clientes}"
	conn.sendall(response.encode())

	conn.close()

	#try:
	#    name = conn.recv(1024).decode()
	 #   response = f"hola {name}, estas conectado a un servidor concurrente!"
	  #  conn.sendall(response.encode())
	#except Exception as e:
	 #   print(f"error con {addr}: {e}")
	#finally:
	 #   conn.close()
	  #  print(f"conexion cerrada con {addr}")

#crear servidor socket
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()

print("servidor concurrente con contador y lock...")

while True:
   conn, addr= server.accept()

   #crear a thread per client
   cliente_thread = threading.Thread(
	target=handle_client,
	args=(conn, addr)
   )
   cliente_thread.start()


conn, addr = server.accept()
print("estudiante conectado:", addr)

conn.sendall(b"hola juan felipe")
conn.close()

