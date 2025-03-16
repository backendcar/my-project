import cv2 as cv
from matplotlib import pyplot as plt

image_bgr = cv.imread("images/image1.jpg")

image_rgb = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()