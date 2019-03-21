import pytesseract
from PIL import Image

img = Image.open('test.png')

#pytesseract.pytesseract.tesseract_cmd =
result = pytesseract.image_to_string(img)
print(result)