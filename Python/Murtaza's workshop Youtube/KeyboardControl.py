from djitellopy import tello
import KeyPressModule as kpm
from time import sleep

kpm.init()
telloObject = tello.Tello()
telloObject.connect()
print(telloObject.get_battery())

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
    elif kpm.getKey("l"): telloObject.land()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    telloObject.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.85)
