from PIL import ImageGrab
import numpy as np
import cv2
import time

def capture_image():
    last_time = time.time()
    while(True):
        screen = ImageGrab.grab(bbox=(260, 240, 607, 856))
        screen = np.array(screen)
        image = match_image(screen)
        printScreen = np.array(image)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def match_image(screen):
    target = cv2.imread('ob.jpg', cv2.IMREAD_GRAYSCALE)
    target = cv2.resize(target, dsize=(0, 0), fx = 1.3, fy = 1.3, interpolation=cv2.INTER_CUBIC)
    background = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    #background = cv2.resize(background, dsize=(0, 0), fx = 0.7, fy = 0.7, interpolation=cv2.INTER_LINEAR)
    res = None

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    # compute the descriptors with ORB
    kp1, des1 = orb.detectAndCompute(target, None)
    kp2, des2 = orb.detectAndCompute(background, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x:x.distance)
    # draw only keypoints location,not size and orientation
    res = cv2.drawMatches(target, kp1, background, kp2, matches[:15], res, flags=2)

    return res

capture_image()