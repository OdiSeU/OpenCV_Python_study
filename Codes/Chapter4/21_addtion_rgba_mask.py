import cv2
import numpy as np
import matplotlib.pyplot as plt

img_fg = cv2.imread('../../Images/opencv_logo.png', cv2.IMREAD_UNCHANGED)
img_bg = cv2.imread('../../Images/coffee.jpg')

_, mask = cv2.threshold(img_fg[:,:,3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)
h, w = img_fg.shape[:2]
roi = img_bg[10:10+h, 10:10+w]

masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask)
masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

added = masked_fg + masked_bg
img_bg[10:10+h, 10:10+w] = added

imgs = {'mask':mask, 'mask_inv':mask_inv, 'masked_fg':masked_fg[:,:,::-1], 'masked_bg':masked_bg[:,:,::-1], 'added':added[:,:,::-1], 'result':img_bg[:,:,::-1] }
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(k)
    plt.imshow(v, 'gray')
    plt.xticks([]); plt.yticks([])
plt.show()