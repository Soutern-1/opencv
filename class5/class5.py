import cv2 as cv2
import numpy as np
import os

cascade_file =  "class5/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_file)

image1 = cv2.imread("class5/resources/image1.jpg")
image2 = cv2.imread("class5/resources/image2.jpg")
image = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5)
for (x,y,w,h) in face:
    cv2.rectangle(image2,(x,y),(x+w,y+h),(255,255,255),10)

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)



cv2.waitKey(0)
cv2.destroyAllWindows()

