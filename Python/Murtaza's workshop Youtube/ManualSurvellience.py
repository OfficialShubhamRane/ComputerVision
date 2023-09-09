from djitellopy import tello
import KeyPressModule as kpm
import cv2
import time

kpm.init()
telloObject = tello.Tello()
telloObject.connect()
print(telloObject.get_battery())
global img
telloObject.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kpm.getKey("a"): lr = -speed
    elif kpm.getKey("d"): lr = speed

    elif kpm.getKey("w"): fb = speed
    elif kpm.getKey("s"): fb = -speed

    elif kpm.getKey("UP"): ud = speed
    elif kpm.getKey("DOWN"): ud = -speed

    elif kpm.getKey("q"): yv = -speed
    elif kpm.getKey("e"): yv = speed

    elif kpm.getKey("t"): telloObject.takeoff()
    elif kpm.getKey("l"): telloObject.land(); time.sleep(3)

    if kpm.getKey("c"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    telloObject.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    img = telloObject.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
