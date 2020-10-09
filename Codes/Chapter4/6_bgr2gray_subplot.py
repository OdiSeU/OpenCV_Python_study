import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/gulim.ttc").get_name()
rc('font', family=font_name)

img = cv2.imread('../../Images/tonkatsu.jpg')
img2 = img.astype(np.uint16)
b, g, r = cv2.split(img2)
gray1 = ((b + g + r)/3).astype(np.uint8)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgs = {'original': img[:,:,::-1], 'gray - 평균': gray1, 'gray - cvtColor 함수': gray2}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    #cmap : value가 RGB(A)일 경우 무시
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()