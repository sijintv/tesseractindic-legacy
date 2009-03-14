#!/usr/local/bin/python
#-*- coding:utf8 -*-
#This code generates the training files for tesseract-ocr for bootstrapping a new character set
import file
import train
import os
import sys

import ImageFont, ImageDraw, ImageChops
from PIL import Image

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
    font= ImageFont.truetype(font,fsz)
    filecount=0 #for different filenames for the images
    filename=image_dir+"/"+"image"+font_name.split('.')[0]+str(filecount)+".tif"
    boxfile=image_dir+"/"+"image"+font_name.split('.')[0]+str(filecount)+".box"
    f=open(boxfile,"w")
     
    
    
    for akshar in alphabets:
        akshar.strip() #remove nasty characters
        
        #I shall now create an image with black bgc and white font color. One 
        #getbbox() determines the bounding box values I shall invert the image.
        #This has to be done since getbbox() only finds bounding box values for
        #non-zero pixels (read as white), but tesseract-ocr runs on the exact 
        #opposite bgc fgc combination. Contact debayanin@gmail.com.
        
        temp_image=Image.new("L",(fsz*3,fsz*2)) #This is an image with a black background
        #temp_image.show()
        draw = ImageDraw.Draw(temp_image)
        draw.text((fsz,5), unicode(akshar,'UTF-8'), font=font,fill=255) #draw the aksharas. fill=255 means white ink.
        #temp_image.show()
        original_bbox=temp_image.getbbox() #get the bounding box of the black pixels relative to the small image
        symbol_image=ImageChops.invert(temp_image) #symbol_image is the black-on-white symbol image
        draw= ImageDraw.Draw(symbol_image)      #Lets transfer "draw" to the new image
        
        
        
        if(type(original_bbox) != tuple):
            print "NONETYPE ERROR"
            line="Nonetype error"
        else:
            bbox=expand(original_bbox) #The bounding box should not overlap with the symbol, hence we must expand the boxes by a certain tolerance vale tol.
            #draw.rectangle(bbox,None,300) #draw the bounding box
            line=akshar+" "+str(bbox[0])+" "+str(bbox[1])+" "+str(bbox[2])+" "+str(bbox[3])
            
        f.write(line+'\n')
        
        
        symbol_image.save(filename,"TIFF")#save the symbol to a file
        #print filename
        filecount+=1 # give a new name to the file to be created
        filename=image_dir+"/"+"image"+font_name.split('.')[0]+str(filecount)+".tif"
        boxfile=image_dir+"/"+"image"+font_name.split('.')[0]+str(filecount)+".box"
        f.close()
        f=open(boxfile,"w") #open new file"""
        
            
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
                    draw(lang,f,font_file,40,file.read_file(alphabet_dir))#reads all fonts in the directory font_dir and trains

train.train(lang)
#training ends
