from djitellopy import tello
from time import sleep

telloObject = tello.Tello()
telloObject.connect()

print("Battery (%): " + telloObject.get_battery())

telloObject.takeoff()
telloObject.send_rc_control(0,40,0,0) #(left-right, forward-backward, speed, turn)
sleep(2)
telloObject.send_rc_control(0,-40,0,0)
telloObject.land()