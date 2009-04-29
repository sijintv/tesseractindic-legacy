#!/usr/local/bin/python
#-*- coding:utf8 -*-
#This code generates the training files for tesseract-ocr for bootstrapping a new character set
import file
import distort
import train

import os
import sys

#from Sayamindu's code
import cairo
import pango
import pangocairo

import ImageFont, ImageDraw, ImageChops
from PIL import Image

bigbox=()


def expand(temp_bbox):
    """expand a bounding box a little bit"""
    tol=2
    bbox=(temp_bbox[0]-tol,temp_bbox[1]-tol,temp_bbox[2]+tol,temp_bbox[3]+tol)
    return bbox


def draw(lang,font_name,font,fsz,alphabets): # language, font file name, font full path, font size, characters
    """ Generates tif images and box files"""
   
    image_dir=lang+"."+"images"
    if(os.path.exists(image_dir)):
        pass
    else:
        os.mkdir(image_dir)
       
    #Using a font
    #font= ImageFont.truetype(font,fsz)
    boxfile=image_dir+"/"+"bigimage.box"
    f=open(boxfile,"w")
     
    bigimage=Image.new("L",(500,500),255)
    bigdraw=ImageDraw.Draw(bigimage)
    x=y=10
   
    for akshar in alphabets:
        akshar.strip() #remove nasty characters
       
        #I shall now create an image with black bgc and white font color. One
        #getbbox() determines the bounding box values I shall invert the image.
        #This has to be done since getbbox() only finds bounding box values for
        #non-zero pixels (read as white), but tesseract-ocr runs on the exact
        #opposite bgc fgc combination. Contact debayanin@gmail.com.
      
       
        #The lines below are pango/cairo code
        surface = cairo.ImageSurface(cairo.FORMAT_A8, fsz*3, fsz*2)
        context = cairo.Context(surface)

        pc = pangocairo.CairoContext(context)

        layout = pc.create_layout()
        layout.set_font_description(pango.FontDescription('Lohit Bengali 15'))
        layout.set_text(akshar)
        print akshar

        # Next four lines take care of centering the text. Feel free to ignore ;-)
        width, height = surface.get_width(), surface.get_height()
        w, h = layout.get_pixel_size()
        position = (10,10)#(width/2.0 - w/2.0, height/2.0 - h/2.0)
        context.move_to(*position)
        pc.show_layout(layout)
        surface.write_to_png("pango.png")

        #Here we open the generated image using PIL functions
        temp_image=Image.open("pango.png") #black background, white text
        draw = ImageDraw.Draw(temp_image)
        bbox = temp_image.getbbox()
        deltax=bbox[2]-bbox[0]
        deltay=bbox[3]-bbox[1]

       
        print bbox
        new_image=temp_image.crop(bbox)
        #temp_image=temp_image.load()
        inverted_image = ImageChops.invert(new_image) #White background, black text

        bigimage.paste(inverted_image,(x,y))
        bigbox=(x,y,x+deltax,y+deltay)
        print bigbox
        draw=ImageDraw.Draw(bigimage)
        #draw.rectangle(bigbox,None,100)
        x=bigbox[2]+2
        if x>450:
            x=10; y=y+35

        os.unlink("pango.png") #delete the pango generated png

        line=akshar+" "+str(bigbox[0])+" "+str(500-(bigbox[1]+deltay))+" "+str(bigbox[2])+" "+str(500-(bigbox[3]-deltay)) # this is the line to be added to the box file
        f.write(line+'\n')

	#degrade code starts
	strip=[deltax*.2,deltax*.4,deltax*.7]
	for values in range(0,3):
		distort2=inverted_image
		for wai in range(0,deltay):
			for ex in range(strip[values],strip[values]+1):
				distort2.putpixel((ex,wai),255)
		bigbox=(x,y,x+deltax,y+deltay)
		line=akshar+" "+str(bigbox[0])+" "+str(500-(bigbox[1]+deltay))+" "+str(bigbox[2])+" "+str(500-(bigbox[3]-deltay)) # this is the line to be added to the box file
        	f.write(line+'\n')
		bigimage.paste(distort2,(x,y))
		x=bigbox[2]+2
        	if x>450:
            		x=10; y=y+35
	#degrade code ends
     
        #distort.distort(filename2,bbox,fsz,akshar)
     
       
       
    bigimage.save(image_dir+"/"+"bigimage.tif","TIFF")
    f.close()
       
           
if(len(sys.argv)!=7):
    print "Usage: python generate.py -fd <font directory> -l <language> -a <input alphabet directory>"
    exit()

if(sys.argv[1]=="-fd"):
    font_dir=sys.argv[2]
else:
    print "Usage: python generate.py -fd <font directory> -l <language> -a <imput alphabet directory>"
    exit()
       
if(sys.argv[3]=="-l"):
    lang=sys.argv[4]
else:
    print "Usage: python generate.py -fd <font directory> -l <language> -a <input alphabet directory>"
    exit()
   
if(sys.argv[5]=="-a"):
    alphabet_dir=sys.argv[6]
else:
    print "Usage: python generate.py -fd <font directory> -l <language> -a <input alphabet directory>"
    exit()
   


#begin training    
#font_dir="/usr/share/fonts/truetype/ttf-bengali-fonts/"
for t in os.walk(font_dir):
        for f in t[2]:
            if(os.path.exists(font_dir+f)):
                if(f.split('.')[1]=="ttf"):
                    font_file=font_dir+f
                    #print font_file
                    draw(lang,f,font_file,15,file.read_file(alphabet_dir))#reads all fonts in the directory font_dir and trains

train.train(lang)
#training ends


