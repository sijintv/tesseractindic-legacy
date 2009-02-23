#!/usr/local/bin/python
#-*- coding:utf8 -*-
import file
import train

import ImageFont, ImageDraw
from PIL import Image


def draw(font,fsz,alphabets):
    x=0; y=0
    
    im = Image.new("RGB",(fsz*20,fsz*2),"white")
    #im.show()
    # use a truetype font
    font= ImageFont.truetype(font,fsz)
    filecount=0 #for different filenames for the images
    filename="images/image"+str(filecount)+".tif"
    boxfile="images/image"+str(filecount)+".box"
    f=open(boxfile,"w")
     
    
    for akshar in alphabets:
        #print akshar
        sub_im=Image.new("RGB",(fsz*2,fsz*1.5),"white") #first create a small image for just one set of characters, will later paste it onto a larger image im
        draw = ImageDraw.Draw(sub_im)
        draw.text((0,0), unicode(akshar,'UTF-8'), font=font,fill=0) #draw the aksharas
        bbox_sub=sub_im.getbbox() #get the bounding box of the black pixels relative to the small image
        box_im=(x,y,x+fsz*2,y+fsz*1.5)
        bbox_im=(x+bbox_sub[0],y+bbox_sub[1],x+bbox_sub[2],y+bbox_sub[3]) #calculate relative to the big image
        #the lines below create the box files
        line=akshar+" "+str(bbox_im[0])+" "+str(bbox_im[1])+" "+str(bbox_im[2])+" "+str(bbox_im[3])
        f.write(line)
        f.write("\n")
        
        print bbox_im
        #draw.rectangle((0,0,150,70)) #draw the bounding box
        #draw.rectangle(bbox_sub) #draw the bounding box
        im.paste(sub_im,box_im)
        x+=fsz*3 #fsz*(size of the character(S))
        
        if x>900:
        #create next strip
            x=0; y=0
            im.save(filename,"TIFF")#save the strip to a file
            print filename
            filecount+=1 # give a new name to the file to be created
            im = Image.new("RGB",(fsz*20,fsz*1.5),"white") #create a new image
            filename="images/image"+str(filecount)+".tif" #new file name
            boxfile="images/image"+str(filecount)+".box" #new box file name
            f.close()
            f=open(boxfile,"w") #open new file
            
    
    


draw("/usr/share/fonts/truetype/ttf-bengali-fonts/JamrulNormal.ttf",40,file.read_file())

train.train()
