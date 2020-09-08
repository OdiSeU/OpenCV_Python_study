import cv2

img_file = '../Images/girl.jpg'
save_file = '../Images/girl_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow('IMG', img)
cv2.imwrite(save_file, img)
cv2.waitKey(0)
cv2.destroyAllWindows()