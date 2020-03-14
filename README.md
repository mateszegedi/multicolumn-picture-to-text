# multicolumn-picture-to-text

**About**
This script, built on the top of a [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), captures multi-columned text from image scans from your screen and complies these to a single text file

**The Problem:**
Many OCR (=Optical Character Recognition) solutions are currently publicly & commercially available. 
These are so developed and easy-to-use, user can specify an input document and these solutions automatically locate texts, lines from images and saves these as strings as an output. 

Nevertheless, while these solutions are capable to capture texts from a single document, per default it assumes single-column texts (e.g the whole document will be captured line-by-line from left-to-right or reverse). If there are multiple-columns, users have to manulally set up multiple runs and stich the results with difficulties together.

This python script provides a solution to these, by buliding a light wrapper around [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which:
1.) (assuming the user opened a image-viewer software) makes a screenshot from a pre-set section of the screen
(in case of multiple columns, from multiple sections of it), then the mouse automatically forces the viewer
to step to a next page by clicking on an appropriate button. The screenshots then saved to a pre-defined location. 
This step is iterated by a pre-defined number of the user (ideally the number of the pages)
2.) The script iterates through all the images in a pre-defined location, captures the text from these and saves the result to a pre-set output file.

These steps are separated, if any user might be interested about only a single part of this script

**Requirements:**
- Linux OS (tested at Linux version 4.15.0-88-generic )
- Tesseract (it has to be installed separately from https://github.com/tesseract-ocr/tesseract )
- Python 3.x (tested at 3.7)
    - cv2
    - pytesseract
    - pyscreenshot
    - pyautogui
