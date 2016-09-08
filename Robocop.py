class Robot(object):
	def __init__(self, x, y):
		self.x= x
		self.y= y
		self.monedas= 0
		self.direccion= "^"
		self.mapa= None
		
	def colocar_mapa(self, mapa):
		self.mapa= mapa
	
	def mover(self):
		if self.direccion=="^":
			self.y -= 1
		elif self.direccion==">":
			self.x += 1
		elif self.direccion=="v":
			self.y += 1
		else: 
			self.x -= 1

	def rotar(self):
		if self.direccion=="^":
			self.direccion=">"
		elif self.direccion==">":
			self.direccion="v"
		elif self.direccion=="v":
			self.direccion="<"
		else: 
			self.direccion="^"

	def recoger(self, x, y):
		if self.mapa.cuente(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.kit9r(x, y)


		
			
		