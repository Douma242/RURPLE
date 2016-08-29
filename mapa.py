def mapitas(mapa):
	mapitas=[]
	f= open(mapa, "r")
	for linea in f:
		l=list(linea.strip())
		mapitas.append(l)
	return mapitas
	f.close()
