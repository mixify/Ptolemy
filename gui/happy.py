import cv2
import numpy as np

image = cv2.imread("flap_brid.PNG",cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
#surf = cv2.xfeatures2d_SURF_create()

orb  = cv2.ORB_create(nfeatures = 15000 )

(keypoints, descriptors) = sift.detectAndCompute(gray,None)

#img = cv2.drawKeypoints(img,keypoints,None)
