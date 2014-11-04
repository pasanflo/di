#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

class MainWin:
	def __init__(self):

		self.widgets = gtk.glade.XML("formulario.glade")

		signals = { "on_entry_activate" : self.on_button_clicked,
		"on_button1_clicked" : self.on_button_clicked,
		"gtk_main_quit" : gtk.main_quit }

		self.widgets.signal_autoconnect(signals)

		self.label = self.widgets.get_widget("label")
		self.entry = self.widgets.get_widget("entry")

	def on_button_clicked(self, widget):
		texto = self.entry.get_text()
		self.label.set_text("Hola %s" % texto)

if __name__ == "__main__":
	MainWin()
	gtk.main()
