Problema: 
Se requiere simular un sistema de reservas donde 50 usuarios intentan reservar 10 cursos de manera 
concurrente.

El principal problema en este tipo de sistemas es la condición de carrera.
Esto ocurre cuando múltiples hilos acceden y modifican variables compartidas al mismo tiempo 
(por ejemplo, el contador de reservas), lo que puede generar:
Valores incorrectos en el contador (cont)
Reservas duplicadas o inconsistentes
Salidas impredecibles

Solucion con lock:
Para evitar conflictos, se utiliza un bloqueo mutuo (threading.Lock), 
que garantiza que solo un hilo pueda acceder a la sección crítica a la vez.

Solucion con semaphore:
El semáforo (threading.Semaphore) permite controlar cuántos hilos pueden acceder simultáneamente a un recurso.
Esto significa que hasta 3 hilos pueden ejecutar la sección crítica al mismo tiempo.
Cada hilo debe adquirir el semáforo (sem.acquire()).
Si el límite se alcanza, los demás hilos esperan.
Al finalizar, el hilo libera el semáforo (sem.release()).

Resultados con lock:
usuario N.: 1, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 2, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 3, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 4, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 5, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 6, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 7, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 8, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 9, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 10, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 11, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 12, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 14, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 13, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 15, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 16, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 17, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 18, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 19, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 20, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 21, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 22, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 23, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 24, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 25, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 26, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 27, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 28, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 29, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 30, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 32, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 31, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 33, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 34, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 35, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 36, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 37, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 38, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 39, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 40, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 41, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 42, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 43, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 44, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 45, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 46, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 47, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 48, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 49, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 50, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}


Resultado con semaphore:
usuario N.: 1, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 2, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 3, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 4, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 5, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 6, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 7, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 8, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 9, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 10, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 11, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 12, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 13, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 14, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 15, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 16, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 17, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 18, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 19, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 20, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 21, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 22, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 23, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 24, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 25, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 26, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 27, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 28, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 29, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 30, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 31, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 32, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 33, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 34, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 35, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 36, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 37, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 38, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 39, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 40, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 41, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 42, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 43, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 44, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 45, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 46, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 47, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 48, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 49, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
usuario N.: 50, Materias: {'c1': 'español', 'c2': 'matemáticas', 'c3': 'ciencias', 'c4': 'historia', 'c5': 'geografía', 'c6': 'arte', 'c7': 'música', 'c8': 'deportes', 'c9': 'tecnología', 'c10': 'inglés'}
