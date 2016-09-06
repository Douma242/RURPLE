def instrucciones(n1):
	instrucciones=[]
	f= open(n1, "r")
	for linea in f:
		l=linea.strip()
		instrucciones.append(l)
	f.close()
	return instrucciones

def mapitas(mapa):
	mapitas=[]
	f= open(mapa, "r")
	for linea in f:
		l=list(linea.strip())
		mapitas.append(l)
	return mapitas
	f.close()
