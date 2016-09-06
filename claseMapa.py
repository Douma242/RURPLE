class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot= None

	def robocop(self, robot):
		self.robot= robot

	def cuente(self, x, y):
		cont=0
		for moneda in self.monedas:
			if moneda.x==x and moneda.y==y:
				cont += 1
		return cont

	def agregar_moneda(self, monedita):
		self.monedas.append(monedita)

	def dibujar_mapa(self, ancho, alto):

		resultado=""

		for y in range(self.alto):
			for x in range(self.ancho):

				if x == self.robot.x and y == self.robot.y:
                    resultado += self.robot.dibujar()

                elif self.contar_monedas_en(x, y) > 0:
                    resultado += self.contar_monedas_en(x, y)
                
                else:
                    resultado += " "

            resultado += "\n"
	
		return resultado

	def kit9r(self, x, y):
        indice_coincidencia = -1
        for indice in range(len(self.monedas)):
            moneda = self.monedas[indice]
            if moneda.x == x and moneda.y == y:
                indice_coincidencia = indice
                break

        if indice_coincidencia >= 0:
            self.monedas.pop(indice_coincidencia)




		