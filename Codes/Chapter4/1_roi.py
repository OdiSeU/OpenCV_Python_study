import cv2
import numpy as np

img = cv2.imread('../../images/sunset.jpg')

x=770; y=225; w=77; h=77;
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()