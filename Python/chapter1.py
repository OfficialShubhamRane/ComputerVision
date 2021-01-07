import cv2
import numpy as np

############################ Chapter 1
# Reading Image from location on local machine
# img = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/Formals.jpg");
# cv2.imshow("Output", img)
# cv2.waitKey(0)

########################## Reading video from location on local machine
# vid = cv2.VideoCapture("C:/Users/Shubham/Videos/InRoomVideo.mp4")
# while True:
#     success, frame = vid.read()
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

######################## Using laptop camera
# vid = cv2.VideoCapture(0)
# vid.set(3, 640)
# vid.set(4, 480)
#
# while True:
#     success, frame = vid.read()
#     cv2.imshow("Video", frame)
#     # cv2.waitKey(5000)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

########################### Chapter 3
#Resizing and crop image
# img = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/Formals.jpg")
# print(img.shape)
# cv2.imshow("Image", img) #Orignal Image
#
# imgResize= cv2.resize(img,(800,1000))   #Resized Image
# cv2.imshow("Resized", imgResize)
#
# imgCropped = img[0:500, 450:800]
# cv2.imshow("Cropped Img", imgCropped)
# cv2.waitKey(0)

######################### Chapter 4
# Text and Shapes
# img = np.zeros((512,512,3),np.uint8)
# # img[:] = 255,0,0
#
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
# cv2.rectangle(img,(200,200),(400,400),((0,0,255)),(2))
# cv2.putText(img,"Hello", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0), 1)
#
# cv2.imshow("Image",img)
# cv2.waitKey(0)

######################## Chapter 5
#WARP Perspective, Its a birds eye view. Useful for images with sloppy angle
#(339,376),(1180,239)(1722,651)(583,933)
# img = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/2.jpg")
# width,height = 841,557
# srcPts = np.float32([[339,376],[1180,237],[1722,651],[583,933]])
# destPts = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(srcPts,destPts)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#
# cv2.imshow("Image",img)
# cv2.imshow("Output",imgOutput)
# cv2.waitKey(0);

######################## Chapter 6
#Joining Image
# srcImg = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/Green MANTIS.jpg")
# horStack = np.hstack((srcImg, srcImg))
# horStack = cv2.resize(horStack, (1000,800))
# cv2.imshow("Stacked",horStack)
# cv2.waitKey(0)

######################## Chapter 9 Face Detection on photos ##############################


# # img = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/Formals.jpg")
# # img = cv2.imread('C:/Users/Shubham/Downloads/Viraj.jpeg')
# img = cv2.imread("D:/ComputerVision/Python/Lena.jpg")
# # imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgGrayResized = cv2.resize(img, (500,600))
# image= cv2.add(imgGrayResized,np.array([0.0])) #To Increse and decrese the brightness of the image
#
# faceCacade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_frontalface_default.xml")
# faceCacade1 = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_frontalface_alt.xml")
# facecascade2 = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_profileface.xml")
#
# faces = faceCacade.detectMultiScale(image,1.1,2)
# faces1 = faceCacade1.detectMultiScale(image,1.1,2)
# faces2 = facecascade2.detectMultiScale(image,1.1,2)
#
# for(x,y,w,h) in faces:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)        #BLUE, frntalface_default
#
# for(x,y,w,h) in faces1:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)        #RED, frontalface_alt
#
# for(x,y,w,h) in faces2:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)        #GREEN, profileface
#
# cv2.imshow("Result", image)
# cv2.waitKey(0)

############## Chapter 9: Face and Eye Detection using laptop camera
vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)
vid.set(10, 100)
minArea = 1000

faceCacade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_frontalface_default.xml")
faceCacade1 = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_frontalcatface_extended.xml")
eyeCascade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_eye.xml")
eyeCascade1 = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_eye_tree_eyeglasses.xml")
fullBodyCascade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_fullbody.xml")
# numberPlateCascade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_number_plate.xml")
upperBodyCascade = cv2.CascadeClassifier("D:/ComputerVision/Python/haarcascade_upperbody.xml")

while True:
    success, frame = vid.read()

    faces = faceCacade.detectMultiScale(frame,1.1,2)
    faces1 = faceCacade1.detectMultiScale(frame,1.2,3)
    eye = eyeCascade.detectMultiScale(frame,1.3,4)
    eye1 = eyeCascade1.detectMultiScale(frame,1.4,5)
    fullBody = fullBodyCascade.detectMultiScale(frame,1.1,2)
    upperBody = upperBodyCascade.detectMultiScale(frame,1.2,3)
    # numberPlate = numberPlateCascade.detectMultiScale(frame,1.6,7)

    for(x,y,w,h) in faces:
        area = w * h
        if(area > minArea):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        #BLUE, frontalface_default
    for(x,y,w,h) in faces1:
        area = w * h
        if(area > minArea):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        #BLUE, frontalface_extended
    for(x,y,w,h) in eye1:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)            #GREEN, eye-glasses cascade
    for (x, y, w, h) in eye:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)            #GREEN, eye cascade
    ## for (x, y, w, h) in numberPlate:
    ##     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)            #GREEN, number plate cascade
    for (x, y, w, h) in fullBody:
        area = w * h
        if (area > minArea):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # BLUE, fullBody cascade
    for (x, y, w, h) in upperBody:
        area = w * h
        if (area > minArea):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # BLUE, upperBody cascade

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

