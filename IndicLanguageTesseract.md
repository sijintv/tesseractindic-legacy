# Introduction #

Some initial Testing of Tesseract engine for Malayalam were conducted. Basic interest was in finding out how classifier of Tesseract handles Malayalam. This page will be updated as the work progresses.

From initial observations,there are some small bugs in pre processing and post processing routines of tesseract.

A better training of tesseract was conducted and was able to achieve an accuracy of around 88%(not using any language model information, which tesseract relies on a lot).

Initially around 76% accuracy was achieved. A major source of error was the prebase post base reordering of vowel and consonant modifiers. I was able to tackle this using an external routine written in python(this can be easily rewritten in c++, will update it soon). The code for this is available in the svn.

Tessdata is updated with the Malayalam language related files. After using the reordering for vowels, accuracy was improved to around 88%.

Next step is error analysis and detecting any flaws in training and accounting the remaining 12%.


# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages