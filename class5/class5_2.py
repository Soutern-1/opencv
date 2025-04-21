import  cv2

video_file  = "class5/resources/video.mp4"
video_capture = cv2.VideoCapture(video_file)

if not video_capture.isOpened():
    print("error opening file")
    
while video_capture.isOpened():
    status,frame  = video_capture.read()
    if not status:
        break
    cv2.imshow("video",frame)

cv2.waitKey(1)
cv2.destroyAllWindows()
