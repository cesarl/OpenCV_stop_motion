import numpy as np
import cv2
from cv2 import *

def CV_FOURCC(c1, c2, c3, c4) :
    return (c1 & 255) + ((c2 & 255) << 8) + ((c3 & 255) << 16) + ((c4 & 255) << 24)

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
codecArr = "MPEG"
fourcc = CV_FOURCC(ord(codecArr[0]),ord(codecArr[1]),ord(codecArr[2]),ord(codecArr[3]))
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()