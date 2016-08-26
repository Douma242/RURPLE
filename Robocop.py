class Robot(object):
	def __init__(self, x, y):
		self.x= x
		self.y= y
		self.monedas= 0
		self.direccion= 'UP'
		self.mapa= None
	def colocar_mapa(self, mapa):
		self.mapa= mapa
	
	def mover(self):
		self.moverse= 1

	def rotar(self):
		pass
		