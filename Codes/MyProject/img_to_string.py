import cv2

CHARS = ' .,-!:;*#$@'
nw = 100

img = cv2.imread('../../Images/girl.jpg',cv2.IMREAD_GRAYSCALE)
print(img)
h, w = img.shape
nh = int(h / w * nw)

img = cv2.resize(img, (nw * 2, nh))

for row in img:
    for pixel in row:
        idx = int(pixel / 256 * len(CHARS))
        print(CHARS[idx], end='')
    print()