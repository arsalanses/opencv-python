import cv2
import numpy as np

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('page', threshold)
cv2.imshow('page2', th)

cv2.waitKey(0)
cv2.destroyAllWindows()
