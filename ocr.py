#!/usr/bin/python

import sys
import subprocess

args = sys.argv[1:]
print args
exec_string = ['tesseract'] + args

qpipe = subprocess.call(exec_string)
#print qpipe

if (sys.argv[-1] == 'ban'):
	qpipe = subprocess.call(['./reorder_ban.py','out.txt','reordered_out.txt'])
	qpipe = subprocess.call(['gedit','reordered_out.txt'])
else:
        qpipe = subprocess.call(['gedit',sys.argv[2]+'.txt'])


#print qpipe




