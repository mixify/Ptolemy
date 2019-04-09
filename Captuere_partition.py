import numpy
from PIL import ImageGrab
import cv2

imgGrab = ImageGrab.grab(bbox=(480, 100, 1170, 724))

cv_img = cv2.cvtColor(numpy.array(imgGrab), cv2.COLOR_RGB2BGR)
cv2.imshow('image', cv_img)
cv2.waitKey(0)
print("shit")