 NOTE 

The project code hosting has moved to git. Find it at https://github.com/debayan/Tesseract-Indic-OCR/

**Project Description**

> The aim of this project is to add Indic script support to the Tesseract OCR engine, which currently does not support connected script such as devnagri. This includes adding some routines to the existing code base, training the engine with sample images and then testing for accuracy for subsequent debugging and refinement in the algorithms.

**Hacker documentation for this project is maintained at http://hacking-tesseract.blogspot.com**

**Mailing List -> http://groups.google.com/group/indic-ocr**


---


These instructions are for Bengali. Follow the same instructions for any other language. Simply replace the 3 letter code 'ban' with your own language code.

Currently available language support is for Hindi (hin) and Bangla (ban)

**INSTALLATION**

  * Download http://tesseractindic.googlecode.com/files/tesseractindic-0.2.tar.gz . Untar.
  * cd tesseractindic-0.2
  * ./configure   -> make -> sudo make install
  * Download the appropriate language data file. http://tesseractindic.googlecode.com/files/bengali_training_data-0.1.tar.gz. Untar and copy contents to /usr/local/share/tessdata/


**USAGE**


  * tesseract sample.tif output -l xxx
  * ./reorder\_ban.py output.txt newoutput.txt . newoutput.txt is your final output.


Download reorder\_ban.py from http://tesseractindic.googlecode.com/files/reorder_ban.py .


**Training data files for other Indian languages will be added shortly.**


---


Tools and used software

Tesseract OCR engine 2.04
http://code.google.com/p/tesseract-ocr/

Gimp 2.2.17
http://www.gimp.org/

bbtesseract (GUI for editing training data, such as box files)
0.5.34
http://code.google.com/p/bbtesseract/

Project Plan
Take the input image and then manipulate it in a manner so that it then fit to be processed by the Tesseract OCR engine. For devnagri scripts, it translates to clipping the maatra(shironaam) between successive characters.

Online Documentation
http://code.google.com/p/tesseract-ocr/wiki/TesseractProjects, http://tesseract-ocr.repairfaq.org/, http://debayanin.googlepages.com/hackingtesseract