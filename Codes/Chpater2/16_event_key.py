import cv2

img_file = '../../Images/girl.jpg'
img = cv2.imread(img_file)

x, y = 100, 100

while True:
    cv2.imshow('IMG', img)
    cv2.moveWindow('IMG', x, y)
    key = cv2.waitKey(0) & 0xFF
    print(key, chr(key))
    if key == ord('w'):
        y -= 10
    elif key == ord('a'):
        x -= 10
    elif key == ord('s'):
        y += 10
    elif key == ord('d'):
        x += 10
    elif key == ord('q') or key == 27:
        break
        cv2.destroyAllWindows()
    cv2.moveWindow('IMG', x, y)
