import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image', img)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([100, 200], [200, 300], 'r', linewidth=5)
plt.show()

cv2.imwrite('imgout.png', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
