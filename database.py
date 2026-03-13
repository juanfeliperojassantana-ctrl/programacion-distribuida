#IMPORTACIONES

import aiomysql #libreria async para mysql, aiomysql permite ejecutar consultas sin bloquear 
                #el servidor 

#configuracion de conexion

DB_CONFIG  = {
	"host": "localhost",
	"port": 3306,
	"user": "root",
	"password": "",
	"db": "citas_db"
}


#funcion de conexion

async def get_connection():
	"""
	crea una conexion async con la base de datos
	"""
	return await aiomysql.connect(**DB_CONFIG)


