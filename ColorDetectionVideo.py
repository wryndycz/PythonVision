import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.open(0)

while(cam.isOpened()):
    ret, frame = cam.read()
    
    blur = cv2.GaussianBlur(frame,(5,5),0)
    #Color conversion from RGB Space to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Define thresholds, in future determine intensity values over each matrix
    lower_red = np.array([5,50,50])
    upper_red = np.array([15,255,255])

    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask = red_mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Gaussian Blur', blur)
    cv2.imshow('Mask', red_mask)
    cv2.imshow('Resultant', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Cleanup
cam.release()
cv2.destroyAllWindows()
