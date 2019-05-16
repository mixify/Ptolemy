import pytesseract
import time
import cv2
import numpy as np
from PIL import Image
from PIL import ImageGrab


last_time = time.time()
#img = Image.open('test.png')
img = ImageGrab.grab(bbox=(0, 140, 500, 500))
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)
print(result)

print('time : {} '.format(time.time() - last_time))