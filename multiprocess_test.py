from multiprocessing import Process, Queue
import pytesseract
import time
import cv2
import numpy as np
from PIL import Image
from PIL import ImageGrab

ocr_cnt = 0
cap_cnt = 0

def ocr_image():
    while True:
        img = ImageGrab.grab(bbox=(0, 140, 500, 500))
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
        result = pytesseract.image_to_string(img)
        print(result)
        global ocr_cnt
        ocr_cnt+=1
        print('ocr-------- ', ocr_cnt, ' --------')

def match_image(thr, background):
    img = background
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    template = cv2.imread('target.png', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= thr)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return img

def capture_image():
    last_time = time.time()
    while(True):
        background_img_pil = ImageGrab.grab(bbox = (0, 140, 950, 900))
        background_img_cv = cv2.cvtColor(np.array(background_img_pil), cv2.COLOR_RGB2BGR)
        img = match_image(0.9, background_img_cv)
        printScreen = np.array(img)

#        print('cap time : {} '.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        global cap_cnt
        cap_cnt+=1
        print('cap-------- ', cap_cnt, ' --------')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    data = [5, 10, 13, -1]
    process_one = Process(target = capture_image)
    process_two = Process(target = ocr_image)
    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()