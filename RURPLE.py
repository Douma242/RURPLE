import MapEIns
from claseMapa import Mapa
from claseMonedas import Monedas
from Robocop import Robot
import time

mapita=input("coloque mapa: ")
mapaso=MapEIns.mapitas(mapita)
ins=input("que instrucciones usara: ")
instruccion=MapEIns.instrucciones(ins)

maposo= Mapa(80, 25)

for y in range (len(mapaso)):
	fila= mapaso[y]
	for x in range (len(fila)):
		maposo.dibujar_mapa()
		maposo.cuente()

for instrucciones in instruccion:
	if instrucciones=="MOVE":
		Robot.mover()
	else: 
		Robot.rotar()
	time.sleep(1)
	

