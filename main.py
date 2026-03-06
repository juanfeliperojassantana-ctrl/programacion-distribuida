from fastapi import FastAPI, HTTPException #import propio del framework FastApi
from typing import List # import estandar de python para tipado
from asyncio #importa standar python para asincronia


# creacion de la app

app = FastAPI() #objeto principal de la APi (instancia del framework) 

#base de datos simulada

clientes = [] #variable global tipo lista para almacenar clientes en memoria
contador_clientes = 0 #variable global para el conteo de clientes

@app.get("/") #decorador propio de fastapi para metodo get
def home():   # funcion normal ( no asincrona por simplicidad)
    return {"mensaje" : " API del banco funcionando"}

@app.post("/clientes") #decorador para metodo post
async def crear_cliente(nombre: str = None):

    global contador_clientes

    if not nombre or nombre.strip() == "":
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

    await asyncio.sleep(5) #simula retraso de 5 segundo

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre.strip()
    }

    clientes.append(cliente)

    return {
        "cliente": cliente,
    }

@app.get("/clientes", response_model=List[dict])  #define tipo de respuesta
def listar_clientes():
    if nor nombre or nombre.strip() =="":
	raise HTTPException(status_code=400, detail="El nombre no puede estar vacio")

    return clientes  #devuelve lista completa

@app.get("/clientes/{cliente_id}") #ruta con parametro dinamico
def obtener_cliente(cliente_id: int): #tipo entero
    
    if not nombre or nombre.strip() == "":
	raise HTTPException(status_code=400, detail="EL nombre no puede estar vacio")

    if cliente_id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero positivo") # Lanza error HTTP

    #Validamos que el ID no sea mayor al numero de clientes
    if cliente_id > len(clientes):
        raise HTTPException(status_code=404, detail="Cliente no encontrado") # Lanza error HTTP

    for cliente in clientes:  #recorre lista
        if cliente ["id"] == cliente_id:
            return cliente #retorna si encuentra


@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    if not nombre or nombre.strip() == "":
       raise HTTPException(status_code=400, detail="El nombre no puede estar vacio")

    if cliente_id <= 0:
       raise HTTPException(status_code=400, detail="El ID debe ser un numero positivo")


    for i, cliente in enumerate(clientes):
        if cliente["id"] == cliente_id:
            clientes.pop(i) # elimina un elemento y te lo devuelve .pop
            return {"mensaje": "Cliente eliminado"}

    return {"error" : "Cliente no encontrado"} 


@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, nombre: str= None):
    if not nombre or nombre.strip() == "": 
       raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

     #Validamos que el ID sea positivo
    if cliente_id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero positivo") 

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nombre"] = nombre # actualiza el campo
        return cliente  # devuelve el cliente actualizado")


    return { "error": "cliente no encontrado"} #manejo basico de error


@app.get("/contador")
def contador():
	return{"cliente creado": contador_clientes}
