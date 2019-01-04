import cv2
import numpy as np

img1 = cv2.imread('image.tif')
img2 = cv2.imread('imglogo.tif')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

