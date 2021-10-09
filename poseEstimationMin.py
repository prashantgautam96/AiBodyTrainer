import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture('poseVideos/1.mp4')
pTime = 0
while True:
    success,img = cap.read()
    imgResize = cv2.resize(img,(500,600))
    imgRGB = cv2.cvtColor(imgResize,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(imgResize,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # print(id,lm)
            h, w, c = imgResize.shape
            print((id,lm))
            cx, cy = int(lm.x * w), int(lm.y * h)

            cv2.circle(imgResize, (cx, cy), 7, (255, 0, 0), cv2.FILLED)




    cTime =  time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(imgResize,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("pose", imgResize)
    cv2.waitKey(1)