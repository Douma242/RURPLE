import time

map_width= 70
map_height= 19

def dibujar(x, y):
	result=(" " * map_width) * y
	result += " " * x + "*"
	result += " " * map_width* (map_height + (y+1))
	return result
steps= 19
for i in range(steps):
	time.sleep(0.5)
	print (dibujar(5+i, i))