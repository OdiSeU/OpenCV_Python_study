import numpy as np, cv2
import matplotlib.pyplot as plt

img1 = np.zeros((200, 200), dtype=np.uint8)
img2 = np.zeros((200, 200), dtype=np.uint8)
img1[:, :100] = 255
img2[100:200, :] = 255

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot = cv2.bitwise_not(img1)

imgs = {'img1':img1, 'img2':img2, 'and':bitAnd, 'or':bitOr,
        'xor':bitXor, 'not(img1)':bitNot }
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(3, 2, i+1)
    plt.title(k)
    plt.imshow(v, 'gray')
    plt.xticks([]); plt.yticks([])
plt.show()