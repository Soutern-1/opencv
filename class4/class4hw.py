import cv2
import os
import numpy as np

sum_x,sum_y=0,0

images = []
collage_row = []

rows,columns = 2,3


image_width, image_height = 0,0


folder_path = "images"
for file_name in os.listdir(folder_path):
    # get all the names of files in the given file
    if file_name.endswith((".jpg",".png",".jpeg")):
        image_path = os.path.join(folder_path,file_name)
        # location of file

        image = cv2.imread(image_path)
        # image = cv2.resize(image,(image_width,image_height))
        images.append(image)

#  -----------------------------------------------------


for image in images:
    image_size = image.shape
    sum_x +=image_size[1] 
    sum_y +=image_size[0]

image_width = int(sum_x / len(images))
image_height = int(sum_y / len(images))


print(image_height, image_width)
print(sum_x, sum_y, len(images))

resized_images = []

for image in images:
    resized_images.append(cv2.resize(image,(image_width,image_height)))

    print(image.shape)

#  -----------------------------------------------------
print(resized_images)



if len(images) < rows*columns:
    print("Not enough images")
elif len(images) > rows*columns:
    print("Too many images")
else:
    print("Correct amount of images")

    for i in range(rows):

        starting = i*columns
        ending = (i+1) * columns
        sublist = resized_images[starting:ending]
        row_stack = np.hstack(sublist)
        collage_row.append(row_stack)

    collage = np.vstack(collage_row)
    
    print(collage_row)
    cv2.imshow("image_collage",collage)
    cv2.imwrite("collage.png",collage)
cv2.waitKey(0)
cv2.destroyAllWindows



        # j=0
        # for j in range(columns):
        #     sublist.append(images.pop(0))
        # collage_row.append(sublist)
            # For each row, find *column* number of images, add it to the sublist while deleting it (.pop) and add the sublist back to the row list


