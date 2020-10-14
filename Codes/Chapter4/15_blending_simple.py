import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('../../Images/airballoon.jpg')
img2 = cv2.imread('../../Images/mountain.jpg')

img3 = img1 + img2
img4 = cv2.add(img1, img2)

imgs = { 'img1':img1, 'img2':img2, 'img1+img2':img3, 'cv2.add(img1,img2)':img4 }

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.imshow(v)
    plt.xticks([]); plt.yticks([])
plt.show();