import cv2

title = 'mouse event'
img = cv2.imread('../../Images/blank_500px.jpg')
cv2.imshow(title, img)

colors = {'black' : (0,0,0),
          'red' : (0,0,255),
          'blue' : (255,0,0),
          'green' : (0,255,0) }

def onMouse(event, x, y, flags, param):
    print(event, x, y)
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['red']
        cv2.circle(img, (x,y), 30, color, -1)
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
