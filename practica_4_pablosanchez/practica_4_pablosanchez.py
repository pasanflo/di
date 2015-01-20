#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygtk
import sqlite3
pygtk.require("2.0")

import gtk
import gtk.glade
import gtk.gdk

#conexion
bbdd = 'dbprueba'
conex = sqlite3.connect(bbdd)
c = conex.cursor()

class MainWin:

	def __init__(self):

		self.widgets  = gtk.glade.XML("practica_4_pablosanchez.glade")

		window1 = self.widgets.get_widget("window1")

		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FFFFFF'))

		signals = {"on_button1_clicked" : self.on_button1_clicked,
			"on_button2_clicked": self.on_button2_clicked,
			"on_button3_clicked": self.on_button3_clicked,
			"gtk_main_quit" : gtk.main_quit
			 }


		self.widgets.signal_autoconnect(signals)

	def on_button1_clicked(self, widget):
		"Muestra la ventana con los datos"
		ventana = gtk.Dialog()
		ok_button = ventana.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
		cancelar_button = ventana.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		ok_button.grab_default()
		ventana.set_title("Lista de ")
		label = gtk.Label("<b>¿Guardar Datos?</b>\n")
		label.set_property("use-markup", True)
		entry1 = gtk.Label("Usuario: "+self.widgets.get_widget("entry1").get_text())
		entry2 = gtk.Label("Contraseña: "+self.widgets.get_widget("entry2").get_text())
		entry3 = gtk.Label("E-mail: "+self.widgets.get_widget("entry3").get_text())
		entry4 = gtk.Label("Nombre: "+self.widgets.get_widget("entry4").get_text())
		entry5 = gtk.Label("Apellidos: "+self.widgets.get_widget("entry5").get_text())

		textview1 = self.widgets.get_widget("textview1")
		buffer = textview1.get_buffer()
		textview = gtk.Label("Direccion: "+buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())+"\n\n")
		
		ventana.vbox.pack_start(label, True, True, 0)
		ventana.vbox.pack_start(entry1, True, True, 0)
		ventana.vbox.pack_start(entry2, True, True, 0)
		ventana.vbox.pack_start(entry3, True, True, 0)
		ventana.vbox.pack_start(entry4, True, True, 0)
		ventana.vbox.pack_start(entry5, True, True, 0)
		ventana.vbox.pack_start(textview, True, True, 0)

		ventana.show_all()

		ventana.run()
		ventana.destroy()

	def on_button3_clicked(self, bbdd): #listar
		ventana = gtk.Dialog()
		ok_button = ventana.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
		cancelar_button = ventana.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		ok_button.grab_default()
		ventana.set_title("Listar")
		
		c.execute('SELECT * FROM tabla;')

		for x in c.fetchall():
			entry1 = gtk.Label("Nombre: "+x[4]+" - Apellidos: "+x[5])
			ventana.vbox.pack_start(entry1, True, True, 0)
		
		ventana.show_all()

		ventana.run()
		ventana.destroy()

	def on_button2_clicked(self, bbdd): #grabar

		usuario = self.widgets.get_widget("entry1").get_text()
		contrasena = self.widgets.get_widget("entry2").get_text()
		correo = self.widgets.get_widget("entry3").get_text()
		nombre = self.widgets.get_widget("entry4").get_text()		
		apellido = self.widgets.get_widget("entry5").get_text()	
		
		textview1=self.widgets.get_widget("textview1")
		buffer=textview1.get_buffer()
		descripcion=buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())


		c.execute('insert into tabla(usuario,contrasena,correo,nombre,apellido,descripcion) values ("'+str(usuario)+'","'+str(contrasena)+'","'+str(correo)+'","'+str(nombre)+'","'+str(apellido)+'","'+str(descripcion)+'")')
		conex.commit()

# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
