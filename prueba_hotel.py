import httpx
import asyncio

URL = "http://localhost:8000"
TOTAL_CLIENTES = 30
MAX_SIMULTANEOS = 5

semaforo = asyncio.Semaphore(MAX_SIMULTANEOS)

async def cliente(id):
    async with semaforo:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:  # Timeout aquí
                resp = await client.get(f"{URL}/reservar")
                data = resp.json()
                
                if "exitosa" in data["mensaje"]:
                    print(f"Cliente {id}: Reservado")
                else:
                    print(f"Cliente {id}: Sin cupo")
                    
        except httpx.TimeoutException:
            print(f"Cliente {id}: TIEMPO DE ESPERA")

async def main():
    print(f"Simulando {TOTAL_CLIENTES} clientes...")
    print(f"Máximo {MAX_SIMULTANEOS} simultáneas")
    print("-" * 40)
    
    tareas = [cliente(i + 1) for i in range(TOTAL_CLIENTES)]
    await asyncio.gather(*tareas)
    
    print("-" * 40)
    async with httpx.AsyncClient(timeout=5.0) as client:
        resp = await client.get(f"{URL}/estado")
        print(f"Habitaciones disponibles: {resp.json()['disponibles']}")

asyncio.run(main())
