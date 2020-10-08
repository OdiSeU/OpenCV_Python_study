import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../Images/tonkatsu.jpg')
img2 = img.astype(np.uint16)
b, g, r = cv2.split(img)
gray1 = ((b + g + r)/3).astype(np.uint8)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgs = {'original': img, 'gray - 평균': gray1, 'gray - cvtColor 함수': gray2}
plt.subplot(1, 3, 1)
plt.title('original')
plt.imshow(img[:,:,::-1])
plt.xticks([]); plt.yticks([])

plt.subplot(1, 3, 2)
plt.title('gray - 평균')
plt.imshow(gray1)
plt.xticks([]); plt.yticks([])

plt.subplot(1, 3, 3)
plt.title('gray - cvtColor 함수')
plt.imshow(gray2)
plt.xticks([]); plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()