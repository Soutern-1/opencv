import cv2
import os
import numpy as np

images = []
collage_row = []

rows,columns = 2,3
image_width, image_height = 300,300
folder_path = "class4/images"
for file_name in os.listdir(folder_path):
    # get all the names of files in the given file
    if file_name.endswith((".jpg",".png",".jpeg")):
        image_path = os.path.join(folder_path,file_name)
        # location of file

        image = cv2.imread(image_path)
        image = cv2.resize(image,(image_width,image_height))
        images.append(image)

if len(images) < rows*columns:
    print("Not enough images")
elif len(images) > rows*columns:
    print("Too many images")
else:
    print("Correct amount of images")

    for i in range(rows):

        starting = i*columns
        ending = starting+columns
        sublist = images[starting:ending]
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


