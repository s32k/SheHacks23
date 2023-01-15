# import the necessary packages
import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

img = cv2.imread('textbook.png') # breaking-news
text = pytesseract.image_to_string(img)

print(text)
