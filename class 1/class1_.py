import cv2

logo = cv2.imread("OpenCV_Logo.png")
cv2.imshow("unfiltered",logo)


# splitting the image 

b,g,r=cv2.split(logo)

# 
cv2.imshow("blue saturated",b)
cv2.waitKey(0)
cv2.imshow("green saturated",g)
cv2.waitKey(0)
cv2.imshow("red saturated",r)
cv2.waitKey(0)




