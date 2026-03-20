import threading 

sem = threading.Semaphore(3)
usuarios = 50
dic = {"c1","c2","c3","c4","c5","c6","c7","","c8","c9","c10"}
cont = 0

def reservar():
    global cont

    sem.acquire()
    if cont <= usuarios:
        cont +=1
        print(f"usuario N.: {cont}, Materias: {dic}")
    sem.release()



for i in range(usuarios):
	threading.Thread(target=reservar).start()
	


