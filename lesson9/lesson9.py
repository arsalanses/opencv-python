import cv2
import numpy as np

img = cv2.imread('image.jpg')

cv2.imshow('page', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
