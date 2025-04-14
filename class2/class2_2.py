import cv2
import os
import numpy

pika_image = cv2.imread("pika.png")
pika_resized = cv2.resize(pika_image,(209,207))

 
# errosion - making changes to the boundary
# stating a kernel size
kernel_size = numpy.ones((9,9),numpy.uint8)
eroded_image = cv2.erode(pika_image,kernel_size)

# blurring
# gaussian blur

gaussian_blurred_image = cv2.GaussianBlur(pika_image,(9,9),0)

# median blur
median_blurred_image = cv2.medianBlur(pika_image,5)

# bilateral filter blur
bilateral_filter_blur_image = cv2.bilateralFilter(pika_image,4,70,70)

# rotation of image (row,column)

(row,column) = pika_image.shape[:2]
rotated = cv2.getRotationMatrix2D((column/2, row/2),180,1)
rotated_image = cv2.warpAffine(pika_image,rotated,(row,column))


cv2.imshow("original",pika_image)
# cv2.imshow("resized",pika_resized)
# cv2.imshow("eroded",eroded_image)
# cv2.imshow("gaussian blur",gaussian_blurred_image)
# cv2.imshow('median blur',median_blurred_image)
# cv2.imshow('bilateral_filter_blur',bilateral_filter_blur_image)
cv2.imshow("rotated image", rotated_image)


cv2.waitKey(0)
