import cv2
import mediapipe as mp

# Initialize the machine learning algorithms
facedetection = mp.solutions.face_detection
facemesh = mp.solutions.face_mesh

# Initialize how we draw on the screen
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Create objects for face detection and face mesh 
face_detection_obj = facedetection.FaceDetection(min_detection_confidence=0.3)
face_mesh_obj = facemesh.FaceMesh(static_image_mode=False, min_detection_confidence=0.1, min_tracking_confidence=0.3)

webcam = cv2.VideoCapture(0)

while True:
    status, frame = webcam.read()
    if not status:
        print("Error")
        break
    else:
        rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # Face detection
        face_points = face_detection_obj.process(rgbframe)
        if face_points.detections:
            for detected_landmark in face_points.detections:
                mp_drawing.draw_detection(frame, detected_landmark)

        # Face mesh
        # Processing using "face_mesh_obj (l14)"
        mesh_results = face_mesh_obj.process(rgbframe)
        if mesh_results.multi_face_landmarks:
            for face_landmarks in mesh_results.multi_face_landmarks:
                # If face features detected, draw landmarks
                mp_drawing.draw_landmarks(
                    frame, landmark_list=face_landmarks, connections=facemesh.FACEMESH_TESSELATION,landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )


        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

webcam.release()
cv2.destroyAllWindows()
