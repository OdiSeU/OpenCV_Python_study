import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../Images/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img)
thresh_np[ img > 127 ] = 255

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_binInv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrInv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


imgs = {'Original':img, 'BINARY':t_bin, "BINARY_INV":t_binInv, "TRUNC":t_truc, "TOZERO":t_2zr, "TOZERO_INV":t_2zrInv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()