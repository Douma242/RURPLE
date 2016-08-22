def instrucciones(n1):
	instrucciones=[]
	f= open(n1, "r")
	for linea in f:
		l=linea.strip()
		instrucciones.append(l)
	f.close()
	return instrucciones