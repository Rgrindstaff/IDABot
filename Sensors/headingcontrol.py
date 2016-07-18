import smbus
import math
import time
#import serial
#ser = serial.Serial('/dev/ttyS0', 115200)
from LSM9DS1 import *
import IMUFunctions as func

#Constants

PI=3.1415926
RadToDeg=180/PI
Declination=13
kp=1
ki=1
kd=1
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

    #steadyError+=pidError*dt
    #if steadyError<-10.0:
    #    steadyError=-10.0
    #if steadyError>10.0:
    #    steadyError=10.0

    P=kp*pidError
    I=ki*pidError
    D=kd*pidError

    previousError=pidError

    pidOutput=P+I+D

    #if pidOutput<-0.1:
    #    pidOutput=-0.1
    #if pidOutput>0.1:
    #    pidOutput=0.1

    time.sleep(dt)

    return pidOutput

def getHeading():
    x=func.MAGX()
    y=func.MAGY()
    heading=func.getHeading(x,y)
    return heading

##def setMotorSpeed(speed1,speed2):
##    ser.write('!G')
##    ser.write(' ')
##    ser.write('1')
##    ser.write(' ')
##    ser.write('%d' %(speed1))
##    ser.write('\r')
##
##    ser.write('!G')
##    ser.write(' ')
##    ser.write('2')
##    ser.write(' ')
##    ser.write('%d' %(-speed2))
##    ser.write('\r')

#main

initHeading=getHeading()
target=0#initHeading-180
#if target<-180:
#    target +=360
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
    #setMotorSpeed(speed1,speed2)
    print ("heading: ") + str(heading)
    print ("speed1: ") + str(speed1)
    print ("speed2: ") + str(speed2)
    print (" ")
    break
    
    
