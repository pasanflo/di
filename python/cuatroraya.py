# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import sys
import string
from random import randint

def clear(): #Limpia consola (windows y ubuntu)
	os.system(['clear','cls'][os.name == 'nt'])

tablero = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"], ["0","1","2","3","4","5","6","7","8"]]

jugador = ""
maquina = ""

def mostrar(tablero): #Función para mostrar el tablero
	print("--CUATRO EN RAYA--")
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
		
	if jugador == 'X':
		maquina='O'

	print("Has elegido "+ jugador)
def tiradaHumano(): #Función para tirada del jugador
	columna = 10
	fila = 0
	while columna not in [0,1,2,3,4,5,6,7,8]:
		columna = int(raw_input("Tira: "))
	for fila in [5,4,3,2,1,0]:
		if tablero[fila][columna]=="_":
			tablero[fila][columna] = jugador
			clear()
			mostrar(tablero)
			comprueba(fila, columna)
			return;
		fila=fila-1
		if fila<0:
			print("No hay más huecos, prueba otro.")
			tiradaHumano()

def tiradaMaquina(): #Función para tirada de la máquina.
	fila = 0
	columna = randint(0,8)	
	for fila in [5,4,3,2,1,0]:
		if tablero[fila][columna]=="_":
			tablero[fila][columna] = maquina
			clear()
			mostrar(tablero)
			comprueba(fila, columna)
			return;
		fila=fila-1
		if fila =='-1':
			tiradaMaquina()

def comprueba(fila, columna):
	global jugador, maquina

def juego():
	clear()
	print("-------- BIENVENIDO --------")
	elige()
	clear()
	mostrar(tablero)
	while(1):
		tiradaHumano()
		tiradaMaquina()

juego()









