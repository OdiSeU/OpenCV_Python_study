import cv2
import numpy as np
import matplotlib.pyplot as plt

blk_size = 9
C = 5
img = cv2.imread('../../Images/book.jpg', cv2.IMREAD_GRAYSCALE)
ret, th1 =cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv2.THRESH_BINARY, blk_size, C)
imgs = {'original':img, 'otsu:%d'%ret: th1, 'adapted-mean':th2, 'adapted-gaussian':th3}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.title(key)
    plt.imshow(value, 'gray')
    plt.xticks([]); plt.yticks([])

plt.show()