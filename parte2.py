import threading 

usuarios = 50
dic = {"c1","c2","c3","c4","c5","c6","c7","","c8","c9","c10"}
cont = 0

lock = threading.Lock()

def reservar():
	global cont

	if cont >=0:
		lock.acquire()
		cont +=1
		lock.release()

for i in range(usuarios):
	threading.Thread(target=reservar).start()
	print(f"usuario N.: {cont}, Materias: {dic}")


