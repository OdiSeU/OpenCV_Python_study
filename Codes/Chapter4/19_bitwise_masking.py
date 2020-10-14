import numpy as np, cv2
import matplotlib.pyplot as plt

img = cv2.imread('../../Images/girl.jpg')

mask = np.zeros_like(img)
cv2.circle(mask, (500, 350), 100, (255,255,255), -1)

masked = cv2.bitwise_and(img, mask)

cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey()
cv2.destroyAllWindows();