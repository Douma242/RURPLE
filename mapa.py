from claseMapa import Mapa
class Mapita(Mapa):
	def __init__(self, posicionR, posicionF):
		super(). __init__(posicionR, posicionF)

	def 

	def mapitas(mapa):
		mapitas=[]
		f= open(mapa, "r")
		for linea in f:
			l=list(linea.strip())
			mapitas.append(l)
		return mapitas
		f.close()
