# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:07:43 2018

@author: prince khera
"""

import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (1000,1000), (255,0,0),15)
cv2.rectangle(img, (15,25), (1000,1000),(255,0,255), 5)
cv2.circle(img, (500,500), 100, (0,0,255), -1)

pts = np.array([[50,50], [40,60], [10,1000]], np.int32).reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,233),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
