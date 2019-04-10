import numpy as np
import cv2
import os

cap = cv2.VideoCapture('camera_0.avi')

nr = -1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret!=True:
        break
    nr = nr + 1
    name = 'Output/frame' + str(nr) + '.jpg'
    cv2.imwrite(name,frame)

print(nr)
cap.release()
