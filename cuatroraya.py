#!/usr/bin/env python
import sys

tablero = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"]]
def mostrar(tablero):
	tc = range(6)
	tf = range(9)
	for i in tc:
		for j in tf:
			sys.stdout.write('|')
			sys.stdout.write(tablero[i][j])
		sys.stdout.write('|')
		print("")
	
	
mostrar(tablero)
