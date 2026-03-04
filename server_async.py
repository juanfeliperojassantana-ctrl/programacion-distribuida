import asyncio  #importa la libreria para programacion asincrona 

#funcion que maneja cada cliente (coroutine) 
async def handle_client(reader, writer):
	#espera datos del cliente (maximo 1024 bytes)
	data = await reader.read(1024)
	
	#convierte los bytes recibidos en texto
	name = data.decode()

	#construye el mensaje de respuesta
	response = f"hola {name}"
	# envia la respuesta al cliente (en bytes)
	writer.write(response.encode())
	# espera a que los datos se envien completamente
	await writer.drain()
	# cierra la conexion con el cliente
	writer.close()


#funcion principal del servidor 
async def main():
	#crea el servidor en la ip 0.0.0.0 y puerto 5000
	# handle_client sera ejecutado por cada nueva conexion
	server = await asyncio.start_server(
	    handle_client, "0.0.0.0", 5000
	)

	#mantiene el servidor activo 
	async with server:
	    #el servidor queda escuchando indefinidamente 	
	    await server.serve_forever()


#ejecuta el event loop principal 
asyncio.run(main())  
