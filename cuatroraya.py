# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string
tablero = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"], ["0","1","2","3","4","5","6","7","8"]]

jugador = ""
maquina = ""
turno = ""

def mostrar(tablero): #Función para mostrar el tablero
	tc = range(7)
	tf = range(9)
	for i in tc:
		for j in tf:
			sys.stdout.write('|')
			sys.stdout.write(tablero[i][j])		
		sys.stdout.write('|')
		print("")
def elige(): #Función para elegir ficha del jugador
	global jugador, maquina, turno
	while jugador<>'O' and jugador<>'X':
		jugador =raw_input("Elige una ficha(O/X): ")
	if jugador == 'O':
		maquina='X'
		turno='M'
		
	if jugador == 'X':
		maquina='O'
		turno='H'

	print("Has elegido "+ jugador)
def tiradaHumano(): #Función para tirada del jugador
	t = 10
	i = 0
	while t not in [0,1,2,3,4,5,6,7,8]:
		t = int(raw_input("Tira: "))
	for i in [5,4,3,2,1,0]:
		if tablero[i][t]=="_":
			tablero[i][t] = jugador
			mostrar(tablero)
			return;
		i=i-1
		if i not in [0,1,2,3,4,5]:
			print("No hay más huecos, prueba otro.")
			print(i)
	
	global turno
	turno = 'H'

print("-------- BIENVENIDO --------")
elige()
mostrar(tablero)
while(1):
	tiradaHumano()

