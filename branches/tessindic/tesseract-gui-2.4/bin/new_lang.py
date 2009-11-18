#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
import subprocess

class TopWindow:

	def __init__(self):
		self.mainwindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.mainwindow.set_title("Tesseract Trainer")
                self.mainwindow.connect('destroy', lambda w: gtk.main_quit())
                self.mainwindow.set_icon_from_file("/usr/share/tesseract-gui/tesseract-gui-logo.png")
		self.mainwindow.set_size_request(700, 200)

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
		langfile = open('lang_list.txt','r')
		flines = langfile.readlines()
		langfile.close()
		for line in flines:
			lang = line.rsplit(':',2)[0]
			#print lang
			self.combolang.append_text(lang)
                self.combolang.show()
		self.combolang.connect("changed",self.changed_combo_lang)
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
		self.hboxstyle = gtk.HBox(False,3)
                self.vboxtw.pack_start(self.hboxstyle,True,True,1)
                self.hboxstyle.show()


                self.stylelabel = gtk.Label("Style")
                self.hboxstyle.pack_start(self.stylelabel,True,True,1)
                self.stylelabel.show()

                self.combostyle = gtk.combo_box_new_text()
                self.hboxstyle.pack_start(self.combostyle,True,True,1)
                self.combostyle.show()

		self.mainwindow.show()

	def get_active_text(self,combobox):
   		model = combobox.get_model()
		active = combobox.get_active()
		if active < 0:
      			return None
   		return model[active][0]

	def changed_combo_lang(self,combobox):
		lang_selected = self.get_active_text(self.combolang)
		langfile = open('lang_list.txt','r')
                flines = langfile.readlines()
                langfile.close()
                for line in flines:
			lang = line.rsplit(':',2)[0]	                        
                        if (lang == lang_selected):
				self.code = line.rsplit(':',2)[1]
				#print self.code
		exec_string = "fc-list :lang="+self.code+" >temp"
	        output = runBash(exec_string)
		ftemp = open('temp','r')
		lines = ftemp.readlines()
		ftemp.close()
	        self.combofont.get_model().clear()	
		for line in lines:
			#print lines
			font = line.rsplit(":",1)[0]
			self.combofont.append_text(font)
		self.combofont.show()
		self.combofont.connect("changed",self.changed_combo_font)

	def changed_combo_font(self,combobox):
		self.font_selected = self.get_active_text(self.combofont)
		langfile = open('temp','r')
                flines = langfile.readlines()
                langfile.close()
		self.combostyle.get_model().clear()
                for line in flines:
                        font = line.rsplit(':',1)[0]
                        if (font == self.font_selected):
                                styles = line.rsplit('=',1)[1]
				style_set = styles.split(',')
				for style in style_set:
					self.combostyle.append_text(style)
		self.combostyle.show()
                                #print self.code



	def main(self):
		gtk.main()
def runBash(cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read()#.strip()
        return out

if __name__ == "__main__":
	tw = TopWindow()
	tw.main()
