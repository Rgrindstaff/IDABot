import smbus
import math
import time
import serial
ser = serial.Serial('/dev/ttyS0', 115200)
from LSM9DS1 import *
import IMUFunctions as func

#Constants

PI=3.1415926
RadToDeg=180/PI
Declination=13
kp=20
ki=20
kd=10.5
dt=.1
speed1=500.0
speed2=500.0

#Set Bus

i2c=smbus.SMBus(1)

#Functions

def updatePID(current,target,dt):
    pidError=target-current
    if pidError<-270:
        pidError+=360
    if pidError>270:
        pidError-=360

    P=kp*pidError
    I=ki*pidError
    D=kd*pidError

    previousError=pidError

    pidOutput=P+I+D

    if pidOutput<-100:
        pidOutput=-100
    if pidOutput>100:
        pidOutput=100

    time.sleep(dt)

    return pidOutput

def getHeading():
    x=func.MAGX()
    y=func.MAGY()
    heading=func.getHeading(x,y)-declination
    return heading

def setMotorSpeed(speed1,speed2):
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(speed1))
    ser.write('\r')

    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('%d' %(-speed2))
    ser.write('\r')

#main

target=getHeading()

while (1):
    heading=getHeading()
    output=updatePID(heading,target,dt)
    speed1+=output
    if speed1 > 700.0:
        speed1=700.0
    if speed1 < -700.0:
        speed1=-700.0
    speed2-=output
    if speed2 > 700.0:
        speed2=700.0
    if speed2 < -700.0:
        speed2=-700.0
    setMotorSpeed(speed1,speed2)
    print ("heading: ") + str(heading)
    print ("speed1: ") + str(speed1)
    print ("speed2: ") + str(speed2)
    print (" ")
    break
    
    
