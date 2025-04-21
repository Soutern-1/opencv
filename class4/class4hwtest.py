import cv2
import os
import numpy as np

images = []
collage_row = []

rows,columns = 2,3
image_width, image_height = 0,0
sum_x,sum_y=0,0

folder_path = "class4/images"
for file_name in os.listdir(folder_path):
    # get all the names of files in the given file
    if file_name.endswith((".jpg",".png",".jpeg")):
        image_path = os.path.join(folder_path,file_name)
        # location of file

        image = cv2.imread(image_path)
        images.append(image)


for image in images:
    image_size = image.shape
    sum_x +=image_size[0] 
    sum_y +=image_size[1]

image_width = int(sum_x / len(images))
image_height = int(sum_y / len(images))


print(image_height, image_width)
print(sum_x, sum_y, len(images))

for image in images:
    image = cv2.resize(image,(image_width,image_height))

