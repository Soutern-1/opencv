import cv2
import os

nature_image = cv2.imread("nature_image.png" ) 
modified_nature_image_cold = cv2.applyColorMap(nature_image, cv2.COLORMAP_COOL)
modified_nature_image_hot = cv2.applyColorMap(nature_image, cv2.COLORMAP_HOT)
modified_nature_image_jet = cv2.applyColorMap(nature_image, cv2.COLORMAP_JET)
modified_nature_image_magma = cv2.applyColorMap(nature_image, cv2.COLORMAP_MAGMA)



cv2.imshow("nautre",nature_image)
cv2.imshow("nature modified - hot",modified_nature_image_hot)
cv2.imshow("nature modified - cold",modified_nature_image_cold)
cv2.imshow("nature modified - jet ",modified_nature_image_jet)
cv2.imshow("nature modified - magma",modified_nature_image_magma)
cv2.waitKey(0)

