# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:18:22 2018

@author: prince khera
"""

import cv2
import pandas as pd
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) #BGR in cv2
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.scatter(0,0,')
#plt.show()

#cv2.imwrite('watchgray.png', img)