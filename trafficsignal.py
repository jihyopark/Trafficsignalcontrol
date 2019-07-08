import time
import RPi.GPIO as GPIO
import time
import threading
from gpiozero import MotionSensor

def light(b):#Fuction to turn on the light according to the array
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(2, True)
    GPIO.output(3, True)
    GPIO.output(4, True)
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    if shinN[b] == 'G':
        GPIO.output(2, False)
    if shinN[b] == 'Y':
        GPIO.output(3, False)
    if shinN[b] == 'R':
        GPIO.output(4, False)
    if shinS[b] == 'G':
        GPIO.output(2, False)
    if shinS[b] == 'Y':
        GPIO.output(3, False)
    if shinS[b] == 'R':
        GPIO.output(4, False)

    if shinW[b] == 'G':
        GPIO.output(14, False)
    if shinW[b] == 'Y':
        GPIO.output(15, False)
    if shinW[b] == 'R':
        GPIO.output(18, False)
    if shinE[b] == 'G':
        GPIO.output(14, False)
    if shinE[b] == 'Y':
        GPIO.output(15, False)
    if shinE[b] == 'R':
        GPIO.output(18, False)

    if hshinW[b] == 'G':
        GPIO.output(23, False)
    if hshinW[b] == 'R':
        GPIO.output(24, False)
    if hshinE[b] == 'G':
        GPIO.output(23, False)
    if hshinE[b] == 'R':
        GPIO.output(24, False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)#ped light
GPIO.setup(24, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)#trafic light SN
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)#trafic light EW
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
sensorn = MotionSensor(16)
sensors = MotionSensor(20)
sensore = MotionSensor(21)
sensorw = MotionSensor(26)
buttonn = MotionSensor(5)
buttons = MotionSensor(6)
buttone = MotionSensor(13)
buttonw = MotionSensor(19)
GPIO.output(23, True)
GPIO.output(24, True)
GPIO.output(2, True)
GPIO.output(3, True)
GPIO.output(4, True)
GPIO.output(14, True)
GPIO.output(15, True)
GPIO.output(18, True)

i = 1
ped1 = 0
ped2 = 0
ped3 = 0
ped4 = 0

shinN = ['G', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R']#g=green, y=yellow, r=red, b=black
shinS = ['G', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R']
shinE = ['R', 'R', 'R', 'R', 'R', 'R', 'G', 'Y']
shinW = ['R', 'R', 'R', 'R', 'R', 'R', 'G', 'Y']
hshinW = ['G', 'B', 'G', 'B', 'G', 'B', 'R', 'R']
hshinE = ['G', 'B', 'G', 'B', 'G', 'B', 'R', 'R']
state = 1
a = 1
while True:
    time.sleep(1)
    EW = 0
    NS = 0
    nsen = sensorn.motion_detected
    ssen = sensors.motion_detected
    esen = sensore.motion_detected
    wsen = sensorw.motion_detected
    ped1 = buttonn.motion_detected
    ped2 = buttone.motion_detected
    ped3 = buttonw.motion_detected
    ped4 = buttons.motion_detected
    if not nsen or not ssen or not ped1 or not ped2 or not ped3 or not ped4:
        NS = 1
    if not esen or not wsen:
        EW = 1
    b = state - 1
    print i, "    ", shinN[b], "    ", shinS[b], "    ", shinE[b], "    ", shinW[b], "    ", hshinW[b], "    ", hshinE[b], "    ", state
    print
    light(b)
    i = i + 1
    if NS == 1 and EW == 0 and state == 6:
        state = 1
        a = 0
    if NS == 1 and EW == 0 and state == 7:
        state = state + 1
        a = 0
    if EW == 1 and NS == 0 and state == 8:
        state = 7
        a = 0
    if EW == 1 and NS == 0 and state == 1:
        state = state + 1
        a = 0
    if a == 15:
        state = state + 1
        a = 0
    elif a == 1 and state == 2:
        state = state + 1
        a = 0
    elif a == 1 and state == 3:
        state = state + 1
        a = 0
    elif a == 1 and state == 4:
        state = state + 1
        a = 0
    elif a == 1 and state == 5:
        state = state + 1
        a = 0
    elif a == 1 and state == 6:
        state = state + 1
        a = 0
    elif a == 5 and state == 8:
        state = 1
        a = 0
    a = a + 1
