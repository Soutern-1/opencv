import cv2
import numpy as np

ghost = cv2.imread("ghost.png")
blobs = cv2.imread("blobs.jpeg")

grey_ghost = cv2.cvtColor(ghost, cv2.COLOR_BGR2GRAY)
grey_blurred_ghost = cv2.blur(grey_ghost,(3,3))

# Hough circle detection
# setting properties

detected_circles = cv2.HoughCircles(grey_blurred_ghost,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=90)
print(detected_circles)
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for circle in detected_circles[0,:]:
        x=circle[0]
        y=circle[1]
        r=circle[2]
        ghost = cv2.circle(ghost,(x,y),r,(0,255,0),5)
        ghost = cv2.circle(ghost,(x,y),1,(0,255,0),5)


cv2.imshow("ghost",ghost)
cv2.imshow("blobs",blobs)


cv2.waitKey(0)
cv2.destroyAllWindows()


