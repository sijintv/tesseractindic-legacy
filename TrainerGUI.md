## TesseractIndic Trainer GUI Ver 0.1 ##

### Author: Debayan Banerjee <debayanin@gmail.com> ###

**NOTE**: The GUI does not include any features to generate the dictionary/DAWG (http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract) files yet. It will be available in the next release.


**Pre-requisites**


  1. Go through http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract to learn about the manual method. Read once atleast.
  1. PyGtk should be installed
  1. Install Tesseract 2.03 <Download from http://tesseract-ocr.googlecode.com/files/tesseract-2.03.tar.gz>. Version 2.04 has a bug in the mftraining/cntraining executables that makes it crash.
  1. Download http://tesseractindic.googlecode.com/files/TesseractIndic-Trainer-GUI-0.1.3.tar.gz . Untar and follow the instructions below.

**Usage**

0) Fire up the TesseractIndic trainer GUI by doing the following:

> chmod +x trainer\_gui.py

> ./trainer\_gui.py


1) Create 3 files for your script.
  * consonants\_conjuncts -> This file contains all the consonants and conjuncts/ligatures for your language
  * post\_vowels -> This file contains all the vowel signs for your language
  * rest -> Allt the symbols that do not fit into the 2 categories above, eg, punctuations, independent symbols such as aa, ee etc.

**If you are training for a language like english, you do not need the first 2 files. Simply put all the characters in the third file 'rest'  and proceed.**

2) Select Langauge, Font, Style (not working yet), Output Folder and Folder with the 3 files above, and click on the 'Train' Button.

3) Rename the 5 files that have been generated,eg, rename intproto to hin.intproto.

4) Now generate the DAWG files from a wordlist of your language.

You will find an image named bigimage.tif generated by the above process in the xxx.images directory. Do view this image and see whether all the glyohs have been rendered properly or not. If you find that the image's size is not sufficient for all the glyphs, kindly edit line numbers 43 and 44 in tesseract\_trainer/generate.py to change the width and height of the image. Then repeat the entire process again.

IMPORTANT: Only add those vowels to the post\_vowels file that overlap on a vertical axis with the consonant they are being joined with.
There may be consonant+vowel combinations that fit in a rectangular box, like কু <means ku in bengali>. Now কু = ক + ু .
We can not train ু separately because we will not find this symbol in an image isolated. Hence we need to train all consonants + ু . Hence what I need from you is to tell me cases like these where consonant + vowel produces a glyph that overlaps vertically. To make myself more clear কা (ka) has a consonant + vowel too, but ক and া do not overlap on a vertical axis, and can be trained separately, but for কি (ki) ক and ি overlaps vertically and needs to be trained as a single symbol, together. The thing is that the Tesseract segmenter is built for english and it only boxes rectangles.