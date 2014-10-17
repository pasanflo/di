# !/usr/bin/env python
import sys
import string
tablero = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"], ["1","2","3","4","5","6","7","8","9"]]
tirada = 'X'

def mostrar(tablero):
	tc = range(7)
	tf = range(9)
	for i in tc:
		for j in tf:
			sys.stdout.write('|')
			sys.stdout.write(tablero[i][j])		
		sys.stdout.write('|')
		print("")
def elige():
	j = ' '
	while j<> 'O' and j<> 'X':
		j =raw_input("Elige una ficha(O/X): ")
	if j == 'O':
		maquina='X'
		jugador='O'
	else:
		jugador='X'
		maquina='O'

	print("Has elegido "+ jugador)
def tirada():
	if jugador==tirada:
		t = raw_input("Tira: ")
mostrar(tablero)
elige()
tirada()
