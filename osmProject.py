import cv2
import time
import poseModule as pm


cap = cv2.VideoCapture('poseVideos/1.mp4')
pTime = 0
detecter = pm.poseDetecter()

while True:
    success, img = cap.read()
    img = detecter.findPose(img)
    img = cv2.resize(img, (500, 600))
    lmList = detecter.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (255, 0, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("pose", img)
    cv2.waitKey(1)
