from fastapi import FastAPI, HTTPException # Importa framework FastAPI
from typing import List # Importa para tipado
import asyncio # para asincronia



app = FastAPI() # Objeto principal de la API

#  BASE DE DATOS SIMULADA

citas = [] # Variable global tipo lista alamacenar citas en memoria

# ENDOPINT RAIZ
@app.get("/") # Decorador propio de FastAPI para metodos GET



def home(): 
    return {"Mensaje": "API de citas con FastAPI"} # Retorna diccionario que se convierte en JSON automaticamente

# CREAR cita
@app.post("/citas") # Decorador para metodo POST
async def crear_cita(nombre_doctor: str, nombre_paciente: str): # Parametro recibido por query

    if nombre_doctor == "":
        raise HTTPException(status_code=400, detail="El nombre del doctor no puede estar vacio") # error HTTP
    
    if nombre_paciente == "":
        raise HTTPException(status_code=400, detail="El nombre del paciente no puede estar vacio") # error HTTP
    
    await asyncio.sleep(2) # Simula retraso de 2 segundo
    
    cita = {
        "id" : len(citas) + 1, # Generacion de ID
        "doctor" : nombre_doctor, # Asigna nombre del doctor
        "paciente" : nombre_paciente, #Nombre de paciente
        "estado" : "activa" # Estado inicial de la cita

    }

    citas.append(cita) # Agrega cita a lista global

    return cita # Devuelve cita creado

# LISTAR citas
@app.get("/citas", response_model = List[dict]) # Define tipo de respuesta
def listar_citas():
    #Validamos que exitan citas
    if not citas: # Si la lista esta vacia
        raise HTTPException(status_code=404, detail="No hay citas registrados") # error HTTP
    return citas 

# OBTENER cita POR nombre de cliente 
@app.get("/citas/{nombre_paciente}", response_model = List[dict]) # Ruta con parametros dinamicos
def obtener_cita(nombre_paciente : str): 
    # Validacion basica del nombre de cliente
    if not nombre_paciente: # Si no se proporciona nombre de cliente
        raise HTTPException(status_code=400, detail="El nombre de cliente es requerido") #error HTTP
    
    #Validamos que el nombre de cliente sea positivo
    if nombre_paciente == "": # Si el nombre de cliente esta vacio
        raise HTTPException(status_code=400, detail="El nombre de cliente no puede estar vacio") # error HTTP
    
    #Validamos que el nombre de cliente no sea mayor al numero de citas
    if nombre_paciente > len(citas):
        raise HTTPException(status_code=404, detail="cita no encontrado") #error HTTP
    
    response = [cita for cita in citas if cita["paciente"] == nombre_paciente] # Busca citas por nombre de cliente

    # Validacion que se encontraron citas
    if len(response) == 0: # Si no se encontraron citas
        raise HTTPException(status_code=404, detail="cita no encontrado") # error HTTP
    
    return response # Devuelve lista de citas encontradas

# CANCELAR cita 
@app.put("/citas/{cita_id}") # Decorador para metodo PUT
def cancelar_cita(cita_id : int):
    # Validacion que exita el id
    if not cita_id: # Si no se proporciona ID
        raise HTTPException(status_code=400, detail="El ID es requerido") #error HTTP
    #Validamos que el ID sea positivo
    if cita_id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero positivo") #error HTTP
    
    for cita in citas:
        if cita["id"] == cita_id and cita["estado"] != "cancelada": # Si se encuentra la cita y no esta cancelada
            cita["estado"] = "cancelada" # Cambia el estado de la cita a cancelada
            return {"mensaje" : "cita cancelada exitosamente"} 
    
    return {"error" : "cita no encontrado"} # errores

# ACTUALIZAR cita 
@app.put("/citas/{cita_id}") # Decorador para metodo PUT
def actualizar_cita(cita_id : int, nombre_paciente : str, nombre_medico : str): # Recibe ID y nuevo nombre_paciente
    # Validacion que exita el id
    if not cita_id: # Si no se proporciona ID
        raise HTTPException(status_code=400, detail="El ID es requerido") #error HTTP
    
    # ID sea positivo
    if cita_id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero positivo") # error HTTP
    
    for cita in citas:  
        if cita["id"] == cita_id:
            cita["doctor"] = nombre_doctor # Actualiza el nombre_doctor
            cita["paciente"] = nombre_paciente # Actualiza el nombre_paciente
            return cita # Devuelve cita actualizado
    
    return {"error" : "cita no encontrado"} # manejo basico de errores
