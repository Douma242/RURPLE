class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot= None
	def robocop(self, robot):
		self.robot= robot
	def moneda(self, monedita):
		self.monedas.append(monedita)
		