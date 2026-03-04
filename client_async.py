import asyncio  #libreria para programacion asincrona
import time     # libreria para medir tiempo

async def main() :
	#abre conexion con el servidor 
	reader, writer = await asyncio.open_connection(
	   "127.0.0.1", 5000
	)

	#solicita el nombre al usuario
	name = input("ingresa tu nombre: ")
	
	#guarda el tiempo inicial
	start_time = time.time())
	
	#envia el nombre al servidor
	writer.write(name.encode())
	
	#asegura que el mensaje se envie completamente
	await writer.drain()
	
	#espera respuesta del servidor
	data = await reader.read(1024)
	
	#guarda el tiempo final
	end_time = time.time()

	#muestra respuesta
	print(data.decode())
	
	#calcula el tiempo total de atencion
	print(f"tiempo de atencion: {round(end_time - start_time, 2)} segundos")
	
	#cierra la conexion
	writer.close()
	await writer.wait_closed()


#ejecuta el cliente
asyncio.run(main())
