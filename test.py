from PIL import ImageGrab
import numpy as np
import time
import cv2

def match_image(thr):
    img = cv2.imread('background_img.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    template = cv2.imread('target.png', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= thr)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return img
#    cv2.imshow('res', img)
#    cv2.waitKey(0)

def capture_image():
    while(True):
#        background_img = ImageGrab.grab()
        background_img = ImageGrab.grab(bbox = (0, 140, 950, 900))
        background_img.save('background_img.png')
        img = match_image(0.9)
        printScreen = np.array(img)

        cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
capture_image()