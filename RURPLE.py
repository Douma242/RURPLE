import MapEIns
from claseMapa import Mapa
from claseMonedas import Monedas
from Robocop import Robot
import time

mapita="mapas/mapa1.txt"
mapaso=MapEIns.mapitas(mapita)
ins="instrucciones/algoritmo1.txt"
instruccion=MapEIns.instrucciones(ins)

maposo= Mapa()

for y in range (len(mapaso)):
	fila= mapaso[y]
	for x in range (len(fila)):
		maposo.dibujar_mapa(x, y)
		maposo.cuente(x, y)

for instrucciones in instruccion:
	if instrucciones=="MOVE":
		Robot.mover()
	else: 
		Robot.rotar()
	time.sleep(1)
	

