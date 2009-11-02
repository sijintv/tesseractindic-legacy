#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk


class TopWindow:

	def __init__(self):
		self.mainwindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.mainwindow.set_title("Tesseract Trainer")
                self.mainwindow.connect('destroy', lambda w: gtk.main_quit())
                self.mainwindow.set_icon_from_file("/usr/share/tesseract-gui/tesseract-gui-logo.png")
		self.mainwindow.set_size_request(300, 200)

		self.vboxtw = gtk.VBox(False,1)
		self.mainwindow.add(self.vboxtw)
		self.vboxtw.show()
		################
		self.hboxlang = gtk.HBox(False,3)
                self.vboxtw.pack_start(self.hboxlang,True,True,1)
                self.hboxlang.show()

                                
                self.langlabel = gtk.Label("Language")
                self.hboxlang.pack_start(self.langlabel,True,True,1)
                self.langlabel.show()
                
                self.combolang = gtk.combo_box_new_text()
                self.hboxlang.pack_start(self.combolang,True,True,1)
                self.combolang.show()
		#################### 
	
		self.hboxfont = gtk.HBox(False,3)
		self.vboxtw.pack_start(self.hboxfont,True,True,1)
		self.hboxfont.show()

				
		self.fontlabel = gtk.Label("Font")
		self.hboxfont.pack_start(self.fontlabel,True,True,1)
		self.fontlabel.show()
		
		self.combofont = gtk.combo_box_new_text()
		self.hboxfont.pack_start(self.combofont,True,True,1)
		self.combofont.show()
		
		#####################





		self.mainwindow.show()


	def main(self):
		gtk.main()

if __name__ == "__main__":
	tw = TopWindow()
	tw.main()
