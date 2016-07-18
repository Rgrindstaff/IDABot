import smbus
import math
import time
from LSM9DS1 import *
import IMUFunctions as func

#Constants

PI=3.1415926
RadToDeg=180/PI
FeetToClicks=1800/2.5
kp=1
ki=1
kd=1
dt=.1

#Set Bus

i2c=smbus.SMBus(1)

#Functions

def updatePID(current,target,dt):
    pidError=target-current
    if pidError>10000:
        pidOutput=0
    else:
        pidOutput=(10000-pidError)/20

    time.sleep(dt)

    return pidOutput

def getEncoder():
    return encoderData

#Main

target=1000000000


while (1):
    current=getEncoder()
    output=updatePID(current,target,dt)
    speed-=output
    if speed<0:
        speed=0
