import math
import cv2
from djitellopy import tello
import KeyPressModule as kpm
from time import sleep
import numpy as np

################Parameteres###################
F_SPEED = 117 / 10  # forward speed in cm/sec
A_SPEED = 360 / 10  # angular speed degrees/sec (50/s)
INTERVAL = 0.25

DISTANCE_INTERVAL = F_SPEED * INTERVAL
ANGULAR_INTERVAL = A_SPEED * INTERVAL
##############################################
x, y = 500, 500
angle = 0
yaw = 0

kpm.init()
telloObject = tello.Tello()
telloObject.connect()
print(telloObject.get_battery())

points = [(0,0),(0,0)]


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    angular_speed = 50
    global x, y, yaw, angle
    distance = 0

    if kpm.getKey("a"):
        lr = -speed
        distance = DISTANCE_INTERVAL
        angle = -180

    if kpm.getKey("d"):
        lr = speed
        distance = -DISTANCE_INTERVAL
        angle = 180

    if kpm.getKey("w"):
        fb = speed
        distance = DISTANCE_INTERVAL
        angle = 270
    if kpm.getKey("s"):
        fb = -speed
        distance = -DISTANCE_INTERVAL
        angle = -90

    if kpm.getKey("UP"):
        ud = speed
    if kpm.getKey("DOWN"):
        ud = -speed

    if kpm.getKey("q"):
        yv = -angular_speed
        yaw += ANGULAR_INTERVAL
    if kpm.getKey("e"):
        yv = angular_speed
        yaw -= ANGULAR_INTERVAL

    if kpm.getKey("t"):
        telloObject.takeoff()
    if kpm.getKey("l"):
        telloObject.land()

    sleep(INTERVAL)
    angle += yaw
    x += int(distance * math.cos(math.radians(angle)))
    y += int(distance * math.sin(math.radians(angle)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(img1, point_coordinates):
    for point in point_coordinates:
        cv2.circle(img1, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img1, points[-1], 5, (0, 255, 0), cv2.FILLED)
    cv2.putText(img1, f'({(point_coordinates[-1][0] - 500)/100},{(point_coordinates[-1][1] - 500)/100})m',
                (point_coordinates[-1][0]+10,point_coordinates[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,
                (255,0,255),1)

while True:
    vals = getKeyboardInput()
    telloObject.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((750, 750, 3), np.uint8)
    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
