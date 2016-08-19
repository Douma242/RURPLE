
def mapitas(mapa):
	mapitas=[]
	f= open("MapitasPalRobocop/mapa1.txt", "r")
	for linea in f:
		l=list(linea.strip())
		mapitas.append(l)
	return mapitas
	f.close()
