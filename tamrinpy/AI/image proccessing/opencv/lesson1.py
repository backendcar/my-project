import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/image1.jpg', cv.IMREAD_GRAYSCALE) 
imgcolor = cv.imread('images/image2.jpg', cv.IMREAD_COLOR)

# cv.IMREAD_GRAYSCALE              0
#cv.IMREAD_COLOR                   1
#cv.IMREAD_UNCHANGED(Chanel alfa) -1


# cv.imshow("IMAGE display", img)
# cv.imshow("IMAGE Color display", imgcolor)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.imwrite('saveimages/saveimage.jpg', img)

# (R,G,B) normal
# (B,G,R) in opencv
# RGBA, BGRA

plt.imshow(imgcolor, interpolation="bicubic")
plt.xticks([]), plt.yticks([])
plt.plot([50,100], [100,200], "c", linewidth=5)
plt.show()

