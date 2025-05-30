import cv2
import mediapipe as mp

# Initialize the machine learning algorithm to what we want to detect. 

facedetection = mp.solutions.face_detection

# Initialize how we draw on the screen

mp_drawing = mp.solutions.drawing_utils

# creating an object for facedetection

face_detection_obj = facedetection.FaceDetection(min_detection_confidence=0.3)

webcam = cv2.VideoCapture(0)

while True:
    status,frame = webcam.read()
    if not status:
        print("Error")
        break
    else:
        rgbframe = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # Media pipe uses RGB and not BGR 
        face_points = face_detection_obj.process(rgbframe)
        if face_points.detections:
                for detected_landmark in face_points.detections:
                    mp_drawing.draw_detection(frame,detected_landmark)

        cv2.imshow("Video",frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

cv2.waitKey(0)
cv2.destroyAllWindows

# Change CD to frameworks
# Delete file (3.9)
# Install 3.11
# Install opencv + mediapipe 


