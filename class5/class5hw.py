import cv2

fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

image1 = cv2.imread("resources/fullbody_image.jpg")
image2 = cv2.imread("resources/fullbody_image2.jpg")
image3 = cv2.imread("resources/fullbody_image3.jpg")


images = [image1, image2, image3]

for image in images:
    fullbody_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    fullbody = fullbody_cascade.detectMultiScale(fullbody_gray, scaleFactor=1.1, minNeighbors=5)
    print(fullbody)
    for (x, y, w, h) in fullbody:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 10)
    cv2.imshow("fullbody_image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

