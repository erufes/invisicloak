import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(5):
    ret,background = cap.read()

#Para cor AZUL!!!
key = 0
while(key is not 27):
    ret, img = cap.read()
    cv2.imshow('meh',img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_color = np.array([125, 30, 90])
    upper_color = np.array([255, 255, 255])
    mask = cv2.inRange(hsv,lower_color,upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    
    img[np.where(mask==255)] = background[np.where(mask==255)]
    cv2.imshow('Deteccao da cor', mask)
    cv2.imshow('Tadaaaaah',img)
    key = cv2.waitKey(5)
cap.release()
cv2.destroyAllWindows()
