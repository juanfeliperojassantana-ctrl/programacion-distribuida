preguntas 
1. ¿Es seguro usar variable global?
No. clientes y contador_clientes son globales compartidas. FastAPI usa ASGI, causando error cuando dos operaciones concurrentes modifican el mismo recurso
y el resultado final depende de cuál termina primero. al hacer append() o
modificar sin sincronización.
​

3. ¿Dónde aparece el recurso compartido?
En clientes (lista global) y contador_clientes. Ambos se modifican desde endpoints concurrentes POST - clientes

4. ¿Se debería usar lock en producción?
Sí, imprescindible usar lock FastAPI procesa requests concurrentemente 
Con Lockmserializa accesos, garantiza atomicidad.
Sin lock datos inconsistentes, crashes, dinero perdido en app bancaria
