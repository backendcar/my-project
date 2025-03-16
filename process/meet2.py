import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('coyote.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image', img)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([300, 200], [200, 300], 'r', linewidth=2)
plt.show()

cv2.imwrite('imgout.jpg', img)