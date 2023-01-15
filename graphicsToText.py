# import the necessary packages
import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
def getGraphicsToText(imgTitle): 
    img = cv2.imread(imgTitle) 
    text = pytesseract.image_to_string(img)
    return (text)
