#! /usr/bin/env python
# -*- coding: UTF-8 -*-


# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk

def valor_combobox(combobox):
	model = combobox.get_model()
	activo = combobox.get_active()
	if activo < 0:
		return None
	return model[activo][0]

# Creamos la clase de la ventana principal del programa
class MainWin:

	def __init__(self):
		# Le decimos a nuestro programa que archivo de glade usar (puede tener
		# un nombre distinto del script). Si no esta en el mismo directorio del
		# script habría que indicarle la ruta completa en donde se encuentra
		self.widgets  = gtk.glade.XML("practica_3_pablosanchez.glade")
		
		signals = {"on_entryPrecio_changed" : self.on_entryPrecio_changed,
			"on_about_activate" : self.on_about_activate,
			"on_comboBox_changed" : self.on_comboBox_changed,
			"gtk_main_quit" : gtk.main_quit }
		self.widgets.signal_autoconnect(signals)

		self.comboBox = self.widgets.get_widget("comboBox")
		self.entryPrecio = self.widgets.get_widget("entryPrecio")
		self.labelFinal = self.widgets.get_widget("labelFinal")
		self.labelDescuento = self.widgets.get_widget("labelDescuento")
		self.comboBox.set_active(0)

	def on_entryPrecio_changed(self, widget):
		"Cuando se cambia el valor de entryPrecio"
		self.valor = self.entryPrecio.get_text()
		try:
			self.valor = float(self.valor)
			combo = valor_combobox(self.comboBox)
			self.labelDescuento.set_text("<b>"+str(float(self.valor)*0.01*float(valor_combobox(self.comboBox)))+" €</b>")
			self.labelDescuento.set_property("use-markup", True)
			self.labelFinal.set_text("<b>"+str(self.valor-float(self.valor)*0.01*float(valor_combobox(self.comboBox)))+" €</b>")
			self.labelFinal.set_property("use-markup", True)
		except:
			if len(self.valor)>0:
				self.error("No es un numero válido.")
			elif len(self.valor)==0:
				self.labelFinal.set_text("")
				self.labelDescuento.set_text("")
		
	def on_comboBox_changed(self,widget):
		"Cuando se cambia el valor del combobox"
		self.on_entryPrecio_changed(self)

	def error(self, message):
		"Muestra un error si no es un numero"
		dialog_error = gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK)
		dialog_error.set_title("Error")
		label = gtk.Label(message)
		dialog_error.vbox.pack_start(label, True, True, 0)
		# Con show_all() mostramos el contenido del cuadro de dialogo (en este
		# caso solo tiene la etiqueta) si no se hace el dialogo aparece vacio
		dialog_error.show_all()
		# El run y destroy hace que la ventana se cierre al apretar el boton
		dialog_error.run()
		dialog_error.destroy()

	def on_about_activate(self, widget):
		"Muestra la ventana Acerca de"
		about = gtk.AboutDialog()
		about.set_name("Calculadora de Descuentos")
		about.set_version("1.0")
		about.set_comments("Calcula el descuento del 5%, 10% o 20% sobre el precio indicado.")
		about.set_authors(["Pablo Sánchez"])
		about.run()
		about.destroy()
		

# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
