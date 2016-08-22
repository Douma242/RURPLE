def instrucciones(n1):
	instrucciones=[]
	f= open("Instrucciones/algoritmo1.txt", "r")
	for linea in f:
		l=linea.strip()
		instrucciones.append(l)
	return instrucciones
	f.close()