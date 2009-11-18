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
		elif (curr == "ে" and next2next != "্"):
			#print "two"
			curr = next + "ে"
			index = index+3
		if (curr == "ে" and next2next == "্"):
			curr = input_text[index+3:index+12] + curr
			index = index+9
			print "ei toh"+input_text

		if (curr == "ৈ"):
			curr = next + "ৈ"
			index = index+3
		if (curr == "া" ):# and input_text[index+3] == " "):
			if (len(input_text)-3 == index):
				pass
		
			
						
		out_text+=curr
		prev = curr
		#print index
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
        #print wno
        f=open(outfile,"w")
        f.write(output)
        f.close()

if __name__=="__main__":
	readwrite(sys.argv[1],sys.argv[2])
#readwrite('out.txt','data.txt')


