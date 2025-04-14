import cv2
import os
import numpy


path = str(input("Enter the path of the image you would like to use: "))
image=cv2.imread(path)

choice = int(input("Choose one of the options:\nErode:1\nGaussianBlur:2\nMedian Blur:3\nBilateral BLur:4\nRotate:5\nWeighted Sum:6\nSubtraction:7\n : "))


kernel_size = numpy.ones((9,9),numpy.uint8)

def erode():
    eroded_image = cv2.erode(image,kernel_size)
    cv2.imshow("eroded image", eroded_image)

def gaussian_blur():
    gaussian_blurred_image = cv2.GaussianBlur(image,(9,9),0)
    cv2.imshow("gaussian blurred image", gaussian_blurred_image)

def median_blur():
    median_blurred_image = cv2.medianBlur(image,5)
    cv2.imshow("median blurred image", median_blurred_image)

def bilateral_blur():
    bilateral_filter_blur_image = cv2.bilateralFilter(image,4,70,70)
    cv2.imshow("Bilateral filter blurred image",bilateral_filter_blur_image)


def rotate():
    (row,column) =image.shape[:2]
    rotated = cv2.getRotationMatrix2D((column/2, row/2),180,1)
    rotated_image = cv2.warpAffine(image,rotated,(row,column))
    cv2.imshow("rotated image",rotated_image)

def weighted_sum():
    path2 = str(input("Enter the path of the second image you would like to use"))
    image2=cv2.imread(path)

    combined_image = cv2.addWeighted(image,0.5,image2,0.5,0)
    cv2.imshow("combined image",combined_image)


def subraction():
    path2 = str(input("Enter the path of the second image you would like to use"))
    image2=cv2.imread(path)
    subtracted_image = cv2.subtract(image,image2)
    subtracted_image2 = cv2.subtract(image2,image)

    cv2.imshow("image 1 - image 2",subtracted_image)
    cv2.imshow("image 2 - image 1",subtracted_image2)


if choice==1:
    erode()
if choice==2:
    gaussian_blur()
if choice==3:
    median_blur()
if choice==4:
    bilateral_blur()
if choice==5:
    rotate()
if choice==6:
    weighted_sum()
if choice==7:
    subraction()
cv2.waitKey(0)
cv2.destroyAllWindows()