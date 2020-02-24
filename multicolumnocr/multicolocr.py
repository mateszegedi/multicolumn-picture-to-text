import requests
import cv2
import pytesseract
import pyscreenshot as ImageGrab
import time
import pyautogui
import sys
import glob
import os

'''
The following script waits a bit, then moves the mouse
to a certain position on the screen (marked by click_x, click_y)
and clicks on a button (ideally this is a "next page" button on
some kind of image viewer program) thus going
to the next page of the document.
Then the script creates a screenshot from a part of the
screen, marketd by a bounding box.
This box is marked by the position of the upper left
(bbox_starting_point_x,bbox_starting_point_y) and lower
left (bbox_end_point_x,bbox_end_point_y) corners.
This screenshot will be saved to a pre-selected path
(file_path) by a pre-set name (file_name).
This process is iterated by the number of pages
(no_pages)

This script is also capable to handle multi-columned
texts. For such cases, the "number_of_columns" variable
has to be set to 2,3 or 4 and the respective bounding box
positions have to be set.
The script then automatically capture theses bounding
boxes and orders the screenshots dynamically underneath
each other, hence the textual conversions will follow
the reading order.
'''

def pagegrabber(file_path,
bbox_starting_point_x,bbox_starting_point_y,
bbox_end_point_x,
bbox_end_point_y,
click_x,
click_y,
no_pages,
number_of_columns=1,
file_name='page_',
bbox_starting_point_x2=0,
bbox_starting_point_y2=0,
bbox_end_point_x2=0,
bbox_end_point_y2=0,
bbox_starting_point_x3=0,
bbox_starting_point_y3=0,
bbox_end_point_x3=0,
bbox_end_point_y3=0,
bbox_starting_point_x4=0,
bbox_starting_point_y4=0,
bbox_end_point_x4=0,
bbox_end_point_y4=0):
    print("Quickly, navigate to the software, which displays the document")
    time.sleep(3)
    path=file_path
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    if number_of_columns == 1:
        for i in range(no_pages):
            pyautogui.click(click_x,click_y)
            time.sleep(2)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x,bbox_starting_point_y,bbox_end_point_x,bbox_end_point_y))
            filename=file_name+str(i)+".png"
            image.save(path+filename)
    elif number_of_columns == 2:
        for i in range(no_pages):
            pyautogui.click(click_x,click_y)
            time.sleep(2)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x,bbox_starting_point_y,bbox_end_point_x,bbox_end_point_y))
            filename="book_page_"+str(i*10+1)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x2,bbox_starting_point_y2,bbox_end_point_x2,bbox_end_point_y2))
            filename="book_page_"+str(i*10+2)+".png"
            image.save(path+filename)
    elif number_of_columns == 3:
        for i in range(no_pages):
            pyautogui.click(click_x,click_y)
            time.sleep(2)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x,bbox_starting_point_y,bbox_end_point_x,bbox_end_point_y))
            filename="book_page_"+str(i*10+1)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x2,bbox_starting_point_y2,bbox_end_point_x2,bbox_end_point_y2))
            filename="book_page_"+str(i*10+2)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x3,bbox_starting_point_y3,bbox_end_point_x3,bbox_end_point_y3))
            filename="book_page_"+str(i*10+3)+".png"
            image.save(path+filename)
    elif number_of_columns == 4:
        for i in range(no_pages):
            pyautogui.click(click_x,click_y)
            time.sleep(2)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x,bbox_starting_point_y,bbox_end_point_x,bbox_end_point_y))
            filename="book_page_"+str(i*10+1)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x2,bbox_starting_point_y2,bbox_end_point_x2,bbox_end_point_y2))
            filename="book_page_"+str(i*10+2)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x3,bbox_starting_point_y3,bbox_end_point_x3,bbox_end_point_y3))
            filename="book_page_"+str(i*10+3)+".png"
            image.save(path+filename)
            image = ImageGrab.grab(bbox=(bbox_starting_point_x4,bbox_starting_point_y4,bbox_end_point_x4,bbox_end_point_y4))
            filename="book_page_"+str(i*10+4)+".png"
            image.save(path+filename)
    else:
        print("The script only accepts integers between 1-4")

'''
The following scripts loads the screenshots from a set location
[important! The file path should be set as "\page_" or something
similar, without the page number and the .png ending.
Good example:
original file: "home\folder\document_page_1.png"
current_page_path = "home\folder\document_page_"]
reads in all the documents with the same filename (except ending number)
(no_pages) and appends the text to a .txt document (final_book_path)
'''


def from_page_screenshots_to_final_text(no_pages,current_page_path,final_book_path):
    text_holder=[]
    currentimage_path=current_page_path
    for a in range(no_pages):
        page_path_builder=currentimage_path+str(a)+".png"
        img = cv2.imread(page_path_builder)
        custom_config = r'--oem 3 --psm 6'
        test_txt =pytesseract.image_to_string(img, config=custom_config)
        text_holder.append(test_txt)
    file=open(final_book_path,"w")
    for b in range(len(text_holder)):
        file.write(text_holder[b])
    file.close()
