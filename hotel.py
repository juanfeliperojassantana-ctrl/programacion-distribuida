from fastapi import FastAPI
import asyncio

app = FastAPI()

habitaciones = 8
lock = asyncio.Lock()

@app.get("/reservar")
async def reservar():
    global habitaciones

    async with lock:  # Protege para evitar condiciones de carrera
        disponibles = habitaciones

        await asyncio.sleep(0.2)  # Simula proceso lento

        if disponibles > 0:
            habitaciones -= 1
            return {"mensaje": "Reserva exitosa", "disponibles": habitaciones}
        else:
            return {"mensaje": "No hay habitaciones"}

@app.get("/estado")
async def estado():
    return {"disponibles": habitaciones}

@app.post("/reiniciar")
async def reiniciar():
    global habitaciones
    habitaciones = 8
    return {"mensaje": "Reiniciado a 8 habitaciones"}
