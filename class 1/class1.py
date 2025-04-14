import cv2
import os

# First we have to get the image - reading the image

logo_image1 = cv2.imread("OpenCV_Logo.png")
nature_image2 = cv2.imread("nature_image.png", 0) # The 0 changes the image to be read as grayscale (not converted)

# converting a loaded color image into greyscale
city_image3 = cv2.imread("city_image_3.png") 
grey_city_image = cv2.cvtColor(city_image3, cv2.COLOR_BGR2GRAY)

# saving the file 
cv2.imwrite("greyconverted_city.png",grey_city_image)
# storying at a specific given location
destination = "/Users/sutirthrajesh/Downloads"
os.chdir(destination)
cv2.imwrite("greyconverted_city.png",grey_city_image)


# Displaying in a new window
cv2.imshow("image 1",logo_image1)
cv2.imshow("image 2",nature_image2)
cv2.imshow("image 3", city_image3)
cv2.imshow("modified image 3", grey_city_image)
cv2.waitKey(0)

