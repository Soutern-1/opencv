import cv2

image = cv2.imread("/Users/sutirthrajesh/Documents/vs/openCV/videocollage1.jpg")

image = cv2.line(image,(100,100),(500,100), (0,255,0), 3)
image = cv2.rectangle(image,(200,600),(400,800), (255,0,155), 3)
image = cv2.rectangle(image,(700,300),(900,500), (0,255,0), -1)
image = cv2.circle(image, (800,800),50,(255,255,254),3)
image = cv2.circle(image, (900,900),50,(255,255,254),-3)

font = cv2.FONT_HERSHEY_TRIPLEX
image = cv2.putText(image, "Hello World", (700,100),font,3,(255,255,255),1)


cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
