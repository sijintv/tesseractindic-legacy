#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
import codecs 
import os 
from optparse import OptionParser
def isPrebase(letter):
	unicode_letter = letter
#	print unicode_letter
	if( ( unicode_letter == "െ"  ) or ( unicode_letter == "േ"  ) or ( unicode_letter == "്ര"  ) ):
		return True
	else:
		return False
def reorderUnicode(input_text):
	curr=""
	next=""
	prev=""
	out_text =""
	pre_char = ""
	post_char=""
	prebase=0
	prebase_ra=0
	index = 0
	while index < len(input_text):
		curr = input_text[index:index+3]
#		print "current="+curr
		if(index != len(input_text)-1):
			next = input_text[index+3:index+6]
		else:
			next = ""
#		print "next="+next
		if(isPrebase(curr)):			
			if(prev == "െ" and curr == "െ"):
				prebase = 1
				pre_char="ൈ"	
			elif(prebase == 1):
				out_text+=pre_char
				pre_char=curr	
			else:
				prebase = 1
				pre_char = curr
			
			prev= pre_char
		#	prev = curr
		elif(isPrebase(curr+next)):			
			if(isPrebase(prev) and prebase ==1):
				prebase_ra =1
				post_char = curr+next
			else:
				pre_char = curr+next
				prebase = 1
			prev = curr+next
			index = index+3
		else:
			if(curr == "ഇ" and next == "ൗ"):
				curr = "ഈ"
				index = index+3;
			if(curr == "ഉ" and next == "ൗ"):
				curr = "ഊ"
				index = index+3;
			if(curr == "ഒ" and next == "ൗ"):
				curr = "ഔ"
				index = index+3;
			if(curr == "ഒ" and next == "ാ"):
				curr = "ഓ"
				index = index+3;		
			out_text+=curr
			prev = curr			
			if(prebase == 1 and curr !="്" and next != "്"):
				if(pre_char == "േ"and next == "ാ"):
					pre_char = "ോ"
					index=index+3
				if(pre_char == "െ"and next == "ാ"):
					pre_char = "ൊ"
					index=index+3
				if(pre_char == "െ"and next =="ൗ"):
					pre_char = "ൌ"
					index=index+3
				if(prebase_ra == 1 ):
					prebase_ra =0
					out_text+=post_char
				print "current="+pre_char
				out_text+=pre_char
			#	prev = pre_char
				pre_char=""
				prebase = 0
		index = index+3
	return out_text
	
def readwrite(infile,outfile):
	f1=open(infile,'r')
	fc=f1.readlines()
	f1.close()

	inputs = ""
	output=""
	words = []
	wno=0
        for ts in fc:
		words = ts.split(' ')
		for w in words:
        		output+=reorderUnicode(w)
			output+=' '
			wno+=1		
	print wno
	f=open(outfile,"w")
	f.write(output)
	f.close()
readwrite(sys.argv[1],sys.argv[2])
