from djitellopy import tello
import cv2

telloObject = tello.Tello()
telloObject.connect()

print(telloObject.get_battery())

telloObject.streamon()

while True:
    img = telloObject.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
