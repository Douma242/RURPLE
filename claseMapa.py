class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
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

		for y in range(self.alto):
			for x in range(self.ancho):

				if x == self.robot.x and y == self.robot.y:
                    resultado += self.robot.rotar()

                elif self.cuente(x, y) > 0:
                    resultado += self.cuente(x, y)
                
                else:
                    resultado += " "

            resultado += "\n"
	
		return resultado

	def kit9r(self, x, y):
        if self.robot.x==x and self.robot.y==y:
        	self.moneda.x=-1
        	self.moneda.y=-1


		