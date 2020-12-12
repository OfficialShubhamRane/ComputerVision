import cv2

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


vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)

while True:
    success, frame = vid.read()
    cv2.imshow("Video", frame)
    # cv2.waitKey(5000)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


