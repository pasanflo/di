#!/usr/bin/env python
tablero = [[_,_,_,_,_,_,_,_,_, 0],[_,_,_,_,_,_,_,_,_, 1],[_,_,_,_,_,_,_,_,_,],[_,_,_,_,_,_,_,_,_,],[_,_,_,_,_,_,_,_,_,],[_,_,_,_,_,_,_,_,_,]]

def mostrarTablero(tablero):
	tc = range(9)
	tf = range(6)
	for i in tc:
		for j in tf:
			sys.stdout.write('|')
			sys.stdout.write tablero[i][j]
	sys.stdout.write('|') + str(j)
	print ""


