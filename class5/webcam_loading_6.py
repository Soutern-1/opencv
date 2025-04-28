import cv2


webcam = cv2.VideoCapture(0)

cascade_file = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(cascade_file)

while True:
    if not webcam.isOpened():
        print("error")
        break
    status,frame = webcam.read()
    if not status:
        print("Error")
        break
    else:
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(grey_frame,scaleFactor=1.1, minNeighbors=5)
        for (x,y,w,h) in face:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
        
        cv2.imshow("Video",frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        # 27 is the "esc" key
    
cv2.waitKey()
cv2.destroyAllWindows

