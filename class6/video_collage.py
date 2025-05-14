import cv2
import os
from PIL import Image
import time

# -------------------------------

images = []
sum_x,sum_y,image_width,image_height = 0,0,0,0
framerate = 1

# -------------------------------


folder_path = "images"
image_list = os.listdir(folder_path)
for file_name in os.listdir(folder_path):
    # get all the names of files in the given file
    if file_name.endswith((".jpg",".png",".jpeg")):
        image_path = os.path.join(folder_path,file_name)
        # location of file
        
        image = cv2.imread(image_path)
        # cv2.waitKey(0)
        images.append(image)


# -------------------------------

for image in images:
    # image_size = image.shape()
    sum_x +=image.shape[0]
    sum_y +=image.shape[1]

print(sum_x,sum_y)


image_width = int(sum_x / len(images))
image_height = int(sum_y / len(images))

print(image_width, image_height)

# =-------------------------

resized_images = []

for image in images:
    resized_images.append(cv2.resize(image,(image_width,image_height)))
        
print("resizing complete")

# -------------------------------
# for image in resized_images:
#     cv2.imshow('image',image)
#     cv2.waitKey(0)



def video_generator():
    media_file = '/Users/sutirthrajesh/Documents/vs/openCV/class6/video.avi'
    video_writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v') ,framerate,(image_height,image_width))
    for image in resized_images:
        video_writer.write(image)
        # cv2.imshow('image',image)

    for image in resized_images:
        cv2.imshow('image',image)
        cv2.waitKey(1000)

        # if cv2.waitKey(1) == 27:
        #     cv2.waitKey(10)
            # break

    video_writer.release()
    cv2.destroyAllWindows()

video_generator()

    
