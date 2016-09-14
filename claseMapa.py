class Mapa(object):
	def __init__(self):
		self.ancho=80
		self.alto=25
		self.monedas=[]
		self.robot= None

	def robocop(self, robot):
		self.robot= robot

	def cuente(self, x, y):
		conta=0
		for moneda in self.monedas:
			if moneda.x==x and moneda.y==y:
				conta += 1
		return conta

	def agregar_moneda(self, monedita):
		self.monedas.append(monedita)

	def dibujar_mapa(self, ancho, alto):

		resultado=""

		for y in range(alto):
			for x in range(ancho):

				if self.robot.y == y and self.robot.x == x:
					resultado += self.robot.rotar()

				elif self.cuente(x, y) > 0:
					resultado += self.cuente(x, y)
                
				else:
					resultado += " "

			resultado += "\n"
	
		return resultado

	def quitar(self, x, y):
		if self.robot.x==x and self.robot.y==y:
			self.moneda.x=-1
			self.moneda.y=-1


		