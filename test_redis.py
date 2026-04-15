from fastapi import FastAPI, HTTPException
import redis


app = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

#@app.post("/crear_cita")
#def crear_cita():

#	lock = r.set("cita_10am", "ocupado", nx=True, ex=10)

#	if not lock:
#		raise HTTPException(status_code=400, detail="cita ocupada")
#	return {"mensaje": "cita reservada correctamente"}

# ENDPOINT 1: CREAR CITA
@app.post("/crear_cita")
def crear_cita(hora: str, paciente: str, medico: str):
    # Intentar bloquear el horario de forma PERMANENTE
    # setnx = "set if not exists" - solo funciona si la key NO existe
    lock = r.set(f"lock_horario_{hora}", "ocupado", nx=True, ex=300)
    
    if not lock:
        raise HTTPException(status_code=400, detail="Ese horario ya está ocupado")
    
    # Crear la cita
    cita_id = r.incr("contador_citas")
    
    # Guardar los datos de la cita
    r.hset(f"cita:{cita_id}", "hora", hora)
    r.hset(f"cita:{cita_id}", "paciente", paciente)
    r.hset(f"cita:{cita_id}", "medico", medico)
    r.hset(f"cita:{cita_id}", "estado", "activa")
    
    # Guardar también qué cita tiene este lock (por si necesitas referencia)
    r.set(f"lock_horario_{hora}_cita_id", cita_id)
    
    return {"mensaje": "Cita reservada correctamente", "cita_id": cita_id}

# ENDPOINT 2: VER CITA
@app.get("/ver_cita")
def ver_cita(cita_id: int):
    # Verificar si la cita existe
    if not r.exists(f"cita:{cita_id}"):
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    # Obtener los datos de la cita
    hora = r.hget(f"cita:{cita_id}", "hora")
    paciente = r.hget(f"cita:{cita_id}", "paciente")
    medico = r.hget(f"cita:{cita_id}", "medico")
    estado = r.hget(f"cita:{cita_id}", "estado")
    
    return {
        "cita_id": cita_id,
        "hora": hora,
        "paciente": paciente,
        "medico": medico,
        "estado": estado
    }

# ENDPOINT 3: CANCELAR CITA
@app.delete("/cancelar_cita")
def cancelar_cita(cita_id: int):
    # Verificar si la cita existe
    if not r.exists(f"cita:{cita_id}"):
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    # Obtener la hora
    hora = r.hget(f"cita:{cita_id}", "hora")
    
    # Verificar que el lock existe y pertenece a esta cita
    lock_exists = r.exists(f"lock_horario_{hora}")
    
    if lock_exists:
        # Liberar el bloqueo del horario
        r.delete(f"lock_horario_{hora}")
        r.delete(f"lock_horario_{hora}_cita_id")
    
    # Cambiar estado o eliminar la cita
    r.hset(f"cita:{cita_id}", "estado", "cancelada")
       
    return {"mensaje": "Cita cancelada correctamente"}

# Endpoint para ver qué horarios están ocupados
@app.get("/horarios_ocupados")
def horarios_ocupados():
    # Buscar todos los locks de horarios
    locks = r.keys("lock_horario_*")
    horarios = []
    for lock in locks:
        if not lock.endswith("_cita_id"):  # Ignorar las keys secundarias
            hora = lock.replace("lock_horario_", "")
            cita_id = r.get(f"{lock}_cita_id")
            horarios.append({"hora": hora, "cita_id": cita_id})
    
    return {"horarios_ocupados": horarios}


