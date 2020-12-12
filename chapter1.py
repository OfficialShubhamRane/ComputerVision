import cv2
import numpy as np

# Reading Image from location on local machine
# img = cv2.imread("C:/Users/Shubham/Pictures/Desktop_Bg/Formals.jpg");
# cv2.imshow("Output", img)
# cv2.waitKey(3000)

#Reading video from location on local machine
# vid = cv2.VideoCapture("C:/Users/Shubham/Videos/InRoomVideo.mp4")
# while True:
#     success, frame = vid.read()
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#Using laptop camera
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

#Text and Shapes
img = np.zeros((512,512,3),np.uint8)
# img[:] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
cv2.rectangle(img,(200,200),(400,400),((0,0,255)),(2))
cv2.putText(img,"Hello", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0), 1)

cv2.imshow("Image",img)
cv2.waitKey(0)