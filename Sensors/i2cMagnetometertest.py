import smbus
import math
from LSM9DS1 import *

#Constants

PI=3.1415926
RadToDeg=180/PI
Declination=13

#Functions

def getHeading():
    
    #Grab X Data
    
    XLow=i2c.read_byte_data(MAG_ADD,MAG_X_L)
    XHigh=i2c.read_byte_data(MAG_ADD,MAG_X_H)
    XRAW=((XLow)|(XHigh<<8))
    if XRAW>=32768:
        XRAW-=65536
    X=XRAW
    
    #Grab Y Data
    
    YLow=i2c.read_byte_data(MAG_ADD,MAG_Y_L)
    YHigh=i2c.read_byte_data(MAG_ADD,MAG_Y_H)
    YRAW=(YLow)|(YHigh<<8)
    if YRAW>=32678:
        YRAW-=65536
    Y=YRAW
    
    #Grab Z Data
    
    ZLow=i2c.read_byte_data(MAG_ADD,MAG_Z_L)
    ZHigh=i2c.read_byte_data(MAG_ADD,MAG_Z_H)
    ZRAW=(ZLow)|(ZHigh<<8)
    if ZRAW>=32768:
        ZRAW-=65536
    Z=ZRAW    
    
    #Determine Heading
    heading=math.atan2(Y,X)*RadToDeg

    return heading


#Set i2c Bus

i2c=smbus.SMBus(1)

#Check Device ID

ID=i2c.read_byte_data(MAG_ADD,WHO_I_AM_M)
print ("Device ID: ") + str(ID)

#Initialize Magnetometer
i2c.write_byte_data(MAG_ADD,CTRL_REG2_M, 0b01100000)
i2c.write_byte_data(MAG_ADD,CTRL_REG3_M, 0b00000000)

#Run Compass
total=0.0
i=0
minimum=1000
maximum=-1000

headingTest=getHeading()
if headingTest>90 or headingTest<-90:
    for x in range (1000):
        i+=1
        heading=getHeading()
        if heading < 0:
            heading +=360
        if heading < minimum:
            minimum=heading
        if heading > maximum:
            maximum=heading
        total+=heading
        
else:
    for x in range (1000):
        i+=1
        heading=getHeading()
       
        if heading < minimum:
            minimum=heading
        if heading > maximum:
            maximum=heading
        total+=heading

mean=total/i
if mean <0:
    mean+=360
mean-=Declination
print ("Mean Heading: ") + str(mean)
print ("Max Heading: ") + str(maximum)
print ("Min Heading: ") + str(minimum)
