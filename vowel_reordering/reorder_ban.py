#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import os
from optparse import OptionParser

def reorderUnicode(input_text):
        curr=""
        next=""
        prev=""
        out_text =""
        index = 0
        while index < len(input_text):
                curr = input_text[index:index+3]
                #print "current="+curr
                if(index != len(input_text)-1):
                        next = input_text[index+3:index+6]
		else: 
			next = ""

		if(index != len(input_text)-2):
			next2next = input_text[index+6:index+9]
                else:
                        next2next = ""
#               print "next="+next

		if (curr == "ে" and next2next == "া"):
			#print "one"
			curr = next + "ো"
			index = index+6
		elif (curr == "ে"):
			#print "two"
			curr = next + "ে"
			index = index+3

		if (curr == "ৈ"):
  			#print "three"
			curr = next + "ৈ"
			index = index+3
		
		out_text+=curr 
		#print index
        	index = index+3
        try:
        	out_text1=unicode(out_text,"utf-8")
        except UnicodeDecodeError:
		print "Encountered a decoding error but continuing"
		out_text1='*'
        return out_text1
       
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
        f=codecs.open(outfile,"w","utf-8")
       	f.write(output)
        f.close()
readwrite(sys.argv[1],sys.argv[2])
