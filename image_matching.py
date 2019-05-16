from PIL import ImageGrab
import numpy as np
import time
import cv2

def match_image(thr, background):
    img = background
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    template = cv2.imread('target.png', cv2.IMREAD_GRAYSCALE) # let's change to memory in the future
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= thr)
    mat_background = matrixlize(img)
    value = 3
    for pt in zip(*loc[::-1]):
        x = shrinklize(pt[0])
        y = shrinklize(pt[1])
        shrinked_w = shrinklize(w)
        shrinked_h = shrinklize(h)
        mat_background[x:x+shrinked_w,y:y+shrinked_h] += value
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # print(shrinklize(pt[0]),shrinklize(w))
    # print(pt[1],shrinklize(h))
    # print(mat_background[10:20,33:40])
    # print(mat_background.shape)
    #     ;
        # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return img, mat_background

similarity = 0.9

X = 0
Y = 140
width = 950
height = 900

def get_state():
    last_time = time.time()
    # while(True):
    background_img_pil = ImageGrab.grab(bbox = (X, Y, width, height))
    background_img_cv = cv2.cvtColor(np.array(background_img_pil), cv2.COLOR_RGB2BGR)
    img, mat = match_image(similarity, background_img_cv)
    printScreen = np.array(img)

    print('{} : '.format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    #     break
    return mat

def matrixlize(img, shrinkage = 10):
    height, width = img.shape[:2]
    return np.zeros((int(width/shrinkage),int(height/shrinkage)))

def shrinklize(val, shrinkage = 10):
    return int(val/shrinkage)
get_state()
