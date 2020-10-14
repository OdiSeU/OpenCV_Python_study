import numpy as np, cv2
import matplotlib.pyplot as plt

mx, my = 500, 350
img = cv2.imread('../../Images/girl.jpg')
mask = np.zeros_like(img)
cv2.circle(mask, (mx, my), 100, (255,255,255), -1)
masked = cv2.bitwise_and(img, mask)
cv2.imshow('masked', masked)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        mx, my = x, y
    mask = np.zeros_like(img)
    cv2.circle(mask, (mx, my), 100, (255,255,255), -1)
    masked = cv2.bitwise_and(img, mask)
    cv2.imshow('masked', masked)

cv2.setMouseCallback('masked', onMouse)

cv2.waitKey()
cv2.destroyAllWindows();