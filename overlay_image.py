import numpy as np
import cv2
import argparse

# example: python overlay_image.py -f /Users/ryanzotti/Documents/repos/Self_Driving_RC_Car/data/1/output.mov

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = True,
    help = "path to where the face cascade resides")
args = vars(ap.parse_args())
mov_file = args["file"]

up_arrow = cv2.imread('/Users/ryanzotti/Dropbox/PhotoshopMiscellaneous/UpArrow.tif')
scale = 0.125
resized_image = cv2.resize(up_arrow,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
rows,cols,channels = resized_image.shape
roi = resized_image[0:rows, 0:cols ]

cap = cv2.VideoCapture(mov_file)

while(cap.isOpened()):
    ret, frame = cap.read()    
    frame[0:resized_image.shape[0],0:resized_image.shape[1]] = resized_image
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()