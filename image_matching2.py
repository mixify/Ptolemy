
from PIL import ImageGrab
import numpy as np
import time
import sys
import cv2

np.set_printoptions(threshold=sys.maxsize)
def match_image(thr, background, factor, game_over):
    img = background
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    alive = True
    mat_background = matrixlize(img)
    for fac in factor:
        template = fac[0]
        value = fac[1]
        w, h = template.shape[::-1]
        #print(w,h)


        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # min_thresh = (min_val + 1e-6) * 1.5
        # loc = np.where(res<=min_thresh)
        loc = np.where(res >= thr)
        # print(loc)
        for pt in zip(loc[1], loc[0]):
            x = shrinklize(pt[0])
            y = shrinklize(pt[1])
            shrinked_w = shrinklize(w)+1
            shrinked_h = shrinklize(h)+1
            # print(x,shrinked_w)
            # print(y,shrinked_h)
            mat_background[x:x+shrinked_w,y:y+shrinked_h] = value

    # print(mat_background)
    for num, template in enumerate(game_over):
    ####     w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= thr)
        for pt in zip(loc[1], loc[0]):
            alive = False
        # if(loc)

            # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # print(shrinklize(pt[0]),shrinklize(w))
    # print(pt[1],shrinklize(h))
    # print("sibal")
    # print(mat_background.shape)
    #     ;
        # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return alive, img, mat_background

similarity = 0.5

L_X = 26
L_Y = 96
R_X = 501
R_Y = 651

width = R_X - L_X
height = R_Y - L_Y
# print(width,height)
# snake = cv2.imread('snake.png', cv2.IMREAD_GRAYSCALE) # let's change to memory in the future
# target = cv2.imread('target.png', cv2.IMREAD_GRAYSCALE) # let's change to memory in the future
game_over = cv2.imread('flap_gameover.png', cv2.IMREAD_GRAYSCALE)
# game_over2 = cv2.imread('game_over2.png', cv2.IMREAD_GRAYSCALE)
m1 = [cv2.imread('flap_bird.png', cv2.IMREAD_GRAYSCALE),1]
o1 = [cv2.imread('flap_pipe.png', cv2.IMREAD_GRAYSCALE),-2]
factor = [m1,o1]
game_over = [game_over]
def get_state():
    last_time = time.time()
    state = np.zeros((width//25, height//25,4))
    done = False
    for i in range(4):
        background_img_pil = ImageGrab.grab(bbox = (L_X, L_Y, R_X, R_Y))
        background_img_cv = cv2.cvtColor(np.array(background_img_pil), cv2.COLOR_RGB2BGR)
        alive, img, mat = match_image(similarity, background_img_cv, factor, game_over)
        # printScreen = np.array(img)
        # print(mat)

        state[:,:,i] = mat
        # print('{} : '.format(time.time() - last_time))
        # last_time = time.time()
        if(not alive):
            done = True

        # cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        #
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
    #     break
    #print(state[:,:,:].T)
    return done, state

def get_shape():
    return (width//25,height//25,4)
def matrixlize(img, shrinkage = 25):
    height, width = img.shape[:2]
    return np.zeros((int(width/shrinkage),int(height/shrinkage)))

def shrinklize(val, shrinkage = 25):
    return int(val/shrinkage)
# get_state()

