import cv2
import os

snow = cv2.imread("snowy.jpg")
desert = cv2.imread("desert.jpg")

# weighted sum of two images (the proportion of each image  - 0 to 1)

combined_image = cv2.addWeighted(snow,0.5,desert,0.3,0,)

# subtraction

subtracted_image = cv2.subtract(snow,desert)
subtracted_image2 = cv2.subtract(desert,snow)

cv2.imshow("snow",snow)
cv2.imshow("desert",desert)
cv2.imshow("combined",combined_image)
cv2.imshow("snow - desert", subtracted_image)
cv2.imshow("desert - snow", subtracted_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()