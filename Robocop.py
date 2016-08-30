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
		

	def rotar(self):
		if self.direccion=="^":
			self.direccion=">"
		elif self.direccion==">":
			self.direccion="v"
		elif self.direccion=="v":
			self.direccion="<"
		else: 
			self.direccion="^"
			
		