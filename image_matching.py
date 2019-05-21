from PIL import ImageGrab
import numpy as np
import time
import sys
import cv2

np.set_printoptions(threshold=sys.maxsize)
def match_image(thr, background, factor, game_over):
    img = background
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    alive = true
    mat_background = matrixlize(img)
    for num, template in enumerate(factor):
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= thr)
        print(loc)
        if(num==0):
            value = 2
        else:
            value = -1
        for pt in zip(*loc[::-1]):
            x = shrinklize(pt[0])
            y = shrinklize(pt[1])
            shrinked_w = shrinklize(w)
            shrinked_h = shrinklize(h)
            mat_background[x:x+shrinked_w,y:y+shrinked_h] += value

    for num, template in enumerate(game_over):
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= thr)
        # if(loc)

            # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # print(shrinklize(pt[0]),shrinklize(w))
    # print(pt[1],shrinklize(h))
    # print("sibal")
    # print(mat_background.shape)
    #     ;
        # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return alive, img, mat_background

similarity = 0.9

L_X = 44
L_Y = 258
R_X = 639
R_Y = 702

width = R_X - L_X
height = R_Y - L_Y
print(width,height)
snake = cv2.imread('snake.png', cv2.IMREAD_GRAYSCALE) # let's change to memory in the future
target = cv2.imread('target.png', cv2.IMREAD_GRAYSCALE) # let's change to memory in the future
game_over1 = cv2.imread('game_over.png', cv2.IMREAD_GRAYSCALE)
game_over2 = cv2.imread('game_over2.png', cv2.IMREAD_GRAYSCALE)
factor = [snake, target]
game_over = [game_over1, game_over2]
def get_state():
    last_time = time.time()
    state = np.zeros((width//10, height//10))
    for i in range(100000):
        background_img_pil = ImageGrab.grab(bbox = (L_X, L_Y, R_X, R_Y))
        background_img_cv = cv2.cvtColor(np.array(background_img_pil), cv2.COLOR_RGB2BGR)
        img, mat = match_image(similarity, background_img_cv, factor, game_over)
        printScreen = np.array(img)

        if(i%30 == 0):
            print(mat[:].T)
            print('----------------------')
        # print('{} : '.format(time.time() - last_time))
        last_time = time.time()
        # cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        #
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
    #     break
    return state

def matrixlize(img, shrinkage = 15):
    height, width = img.shape[:2]
    return np.zeros((int(width/shrinkage),int(height/shrinkage)))

def shrinklize(val, shrinkage = 15):
    return int(val/shrinkage)
get_state()
