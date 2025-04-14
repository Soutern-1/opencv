import cv2
import numpy as np

blobs = cv2.imread("blobs.jpeg")

grey_blobs = cv2.cvtColor(blobs, cv2.COLOR_BGR2GRAY)

# si,ple blob detecter

params=cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.filterByCircularity = True
params.minCircularity = 0.65
params.filterByConvexity = True
params.minConvexity = 0.3
params.filterByInertia = True
params.minInertiaRatio = 0.03

blob_detector = cv2.SimpleBlobDetector_create(params)
blob_points = blob_detector.detect(grey_blobs)
blob_color = np.zeros((1,1))
blobs = cv2.drawKeypoints(blobs,blob_points,blob_color,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print("Number of blobs present: ", len(blob_points))


cv2.imshow("blobs",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


