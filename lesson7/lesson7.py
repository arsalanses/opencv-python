import cv2
import numpy as np

img1 = cv2.imread('image1.tif')
img2 = cv2.imread('image2.tif')

add = img1 + img2
