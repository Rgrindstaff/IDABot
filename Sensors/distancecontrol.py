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
FeetToClicks=1800/2.5
kp=1
ki=1
kd=1
dt=.1
maxspeed=500

#Set Bus

i2c=smbus.SMBus(1)

#Functions

def goToEncoderPosition(position):
    ser.write('!R')
    ser.write('\r')
    ser.write('!PR')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('%d' %(position))

    ser.write('!R')
    ser.write('\r')
    ser.write('!PR')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('%d' %(-position))
