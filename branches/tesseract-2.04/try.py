#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open('out.txt')
fl = f.readlines()
f.close()

f = open('data.txt','w')

for lines in fl:
	words = lines.split(' ')
	for w in words:
		for c in range(0,len(w)-1,3):
			print w[c:c+3]
			#f.write(w[c]+'\n')
f.close()
