def combine(fc,fpresv,fpostsv):
	all_comb=[]
	for c1 in fc:
		c=c1.strip() #remove special characters
		all_comb.append(c)
		for prev in fpresv:
			txt=prev.strip()+c
			all_comb.append(txt)
		for postv in fpostsv:
			txt=c+postv.strip()
			all_comb.append(txt)
			count=0
	for a in all_comb:
		print count,
		count+=1
		print a
		return all_comb



def read_file():
	print "in file.py"
	#file containing vowels
	f=open("alphabets/consonants",'r')
	fc=f.readlines()
	f.close()
	
	#file containing semivowels of the form consonant+semivowel	
	f=open("alphabets/pre_semivowels",'r')
	fpresv=f.readlines()
	f.close()

	#file containing semivowels of the form semivowel+consonant
	f=open("alphabets/post_semivowels",'r')
	fpostsv=f.readlines()
	f.close()	
	return combine(fc,fpresv,fpostsv)
