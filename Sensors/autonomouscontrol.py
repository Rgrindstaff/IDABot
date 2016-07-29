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
FeetToClicks=1800/2.5
kp=20
ki=20
kd=10.5
dt=.1
target=10000

#Set Bus

i2c=smbus.SMBus(1)

#Functions

def goToEncoderPosition(position):
    ser.write('!PR')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(position))
    ser.write('\r')

    ser.write('!PR')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('%d' %(-position))
    ser.write('\r')

def setMotorVelocity(value):
    ser.write('!S')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(value))
    ser.write('\r')

    ser.write('!S')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('%d' %(-value))
    ser.write('\r')
    
def setMotorSpeed(speed):
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(speed))
    ser.write('\r')

    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('%d' %(speed))
    ser.write('\r')

def getEncoderValue():
    ser.write('?C')
    ser.write('%d' %(1))
    encoder=ser.readline(18)

    return encoder

def resetEncoderValue():
    ser.write('!C')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(0))
    ser.write('\r')

def propControl(target):
    current=getEncoderValue()
    error=target-current
    if error>=1000:
        output=1000
    if error<1000:
        output= (1000-error)/4
    return output

#Main
resetEncoderValue()
while(1):
    velocity=propControl(target)
    setMotorVelocity(velocity)

