# This module distorts images
from PIL import Image, ImageOps

def distort(filename2):
	temp_image=Image.open(filename2)
	new1 = ImageOps.mirror(temp_image)
	filename=filename2.split('.tif')[0]+"_1"+".tif"
	new1.save(filename,"TIFF")
	
