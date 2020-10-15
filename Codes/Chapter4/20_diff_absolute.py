import numpy as np, cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('../../Images/leaves1.jpg')
img2 = cv2.imread('../../Images/leaves2.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(img1_gray, img2_gray)

_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_red = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
diff_red[:,:,2] = 0

spot = cv2.bitwise_xor(img2, diff_red)

imgs = {'img1':img1, 'img2':img2, 'diff':diff, 'spot':spot}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.imshow(v,'gray')
    plt.xticks([]); plt.yticks([])
plt.show()