import pytesseract
from PIL import Image

img = Image.open('test.png')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)
print(result)
