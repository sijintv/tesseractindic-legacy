#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
import subprocess
import os

import tesseract_trainer.generate
import tesseract_trainer.file

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
		#####################
		self.dlgFiles = gtk.FileChooserDialog("Select File", None, 
                                                gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, (gtk.STOCK_CANCEL,\
                                                gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))

                self.dlgFiles.set_select_multiple(True)
                self.dlgFiles.set_current_folder(os.getenv('HOME'))
                self.dlgFiles.connect("response", self.f_load_files)

		self.dlgFilesOutDir = gtk.FileChooserDialog("Select File", None,
                                                gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, (gtk.STOCK_CANCEL,\
                                                gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))

                self.dlgFilesOutDir.set_select_multiple(True)
                self.dlgFilesOutDir.set_current_folder(os.getenv('HOME'))
                self.dlgFilesOutDir.connect("response", self.set_output_dir)

		hboxOutDir = gtk.HBox(False,3)
		self.vboxtw.pack_start(hboxOutDir, True, True, 1)
		hboxOutDir.show()

		self.lblSelectfile = gtk.Label()
                self.lblSelectfile.set_markup("Select Output Folder:")
                hboxOutDir.pack_start(self.lblSelectfile, True, True, 1)
                self.lblSelectfile.show()

                self.btnFiles = gtk.FileChooserButton(self.dlgFilesOutDir)
                self.btnFiles.set_current_folder(os.getenv('HOME'))
                #self.btnFiles.set_title("home")
                self.btnFiles.set_width_chars(18)
                hboxOutDir.pack_start(self.btnFiles, True, True, 1)
                self.btnFiles.set_filename("Open")
                self.btnFiles.show()

		hboxOutDir = gtk.HBox(False,3)
                self.vboxtw.pack_start(hboxOutDir, True, True, 1)
                hboxOutDir.show()

                self.lblSelectfile = gtk.Label()
                self.lblSelectfile.set_markup("Select folder with alphabet:")
                hboxOutDir.pack_start(self.lblSelectfile, True, True, 1)
                self.lblSelectfile.show()

                self.btnFiles = gtk.FileChooserButton(self.dlgFiles)
                self.btnFiles.set_current_folder(os.getenv('HOME'))
                #self.btnFiles.set_title("home")
                self.btnFiles.set_width_chars(18)
                hboxOutDir.pack_start(self.btnFiles, True, True, 1)
                self.btnFiles.set_filename("Open")
                self.btnFiles.show()
		
		self.buttontrain = gtk.Button("Train")
                self.vboxtw.pack_start(self.buttontrain, True, True, 1)
		self.buttontrain.show()
		self.buttontrain.connect("clicked",self.train)

		self.mainwindow.show()

	def train(self,dummy):
		print dummy
		font_string=self.font_selected+" "+self.language+" 15"	
		tesseract_trainer.generate.draw(font_string,15,self.language,tesseract_trainer.file.read_file(self.DirectoryIn),self.DirectoryOut)


 	def f_load_files(self, widget, Data):
		if Data == -5 :
	               self.DirectoryIn = widget.get_current_folder() + "/"
                	
	def set_output_dir(self, widget,Data):
		if Data == -5 :
                       self.DirectoryOut = widget.get_current_folder() + "/"
               
		

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
				self.code = line.rsplit(':',2)[1].lower()
				self.language = line.rsplit(':',2)[0]
				#print self.code
		exec_string = "fc-list :lang="+self.code
	        output = runBash(exec_string)
		ftemp = open('temp','w')
		ftemp.write(output)
		ftemp.close()
		#print output
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


	def main(self):
		gtk.main()
def runBash(cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read()#.strip()
        return out
def mod():
	tw = TopWindow()
        tw.main()



if __name__ == "__main__":
	tw = TopWindow()
	tw.main()

