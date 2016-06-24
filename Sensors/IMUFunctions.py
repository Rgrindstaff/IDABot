import smbus
import math
from LSM9DS1 import *

#Constants
PI=3.141592653589793
RadToDeg=180/PI

#Set Bus

i2c=smbus.SMBus(1)

#Functions

def GYRX():
    GXLow=i2c.read_byte_data(IMU,GXL)
    GXHigh=i2c.read_byte_data(IMU,GXH)
    GX=(GXLow)|(GXHigh<<8)
    if GX >= 32768:
        GX-=65536
    return GX
def GYRY():
    GYLow=i2c.read_byte_data(IMU,GYL)
    GYHigh=i2c.read_byte_data(IMU,GYH)
    GY=(GYLow)|(GYHigh<<8)
    if GY >= 32768:
        GY-=65536
    return GY
def GYRZ():
    GZLow=i2c.read_byte_data(IMU,GZL)
    GZHigh=i2c.read_byte_data(IMU,GZH)
    GZ=(GZLow)|(GZHigh<<8)
    if GZ >= 32768:
        GZ-=65536
    return GZ
def ACCX():
    AXLow=i2c.read_byte_data(IMU,MXL)
    AXHigh=i2c.read_byte_data(IMU,MXH)
    AX=((AXLow)|(AXHigh<<8))
    if AX>=32678:
       AX-=65536
    return AX
def ACCY():
    AYLow=i2c.read_byte_data(IMU,MYL)
    AYHigh=i2c.read_byte_data(IMU,MYH)
    AY=(AYLow)|(AYHigh<<8)
    if AY>=32678:
        AY-=65536
    return AY
def ACCZ():
    AZLow=i2c.read_byte_data(IMU,MZL)
    AZHigh=i2c.read_byte_data(IMU,MZH)
    AZ=(AZLow)|(AZHigh<<8)
    if AZ>=32768:
       AZ-=65536
    return AZ
def MAGX():
    XLow=i2c.read_byte_data(MAG_ADD,MAG_X_L)
    XHigh=i2c.read_byte_data(MAG_ADD,MAG_X_H)
    MX=((XLow)|(XHigh<<8))
    if MX>=32768:
        MX-=65536
    return MX
def MAGY():
    YLow=i2c.read_byte_data(MAG_ADD,MAG_Y_L)
    YHigh=i2c.read_byte_data(MAG_ADD,MAG_Y_H)
    MY=(YLow)|(YHigh<<8)
    if MY>=32678:
        MY-=65536
    return MY
def MAGZ():
    ZLow=i2c.read_byte_data(MAG_ADD,MAG_Z_L)
    ZHigh=i2c.read_byte_data(MAG_ADD,MAG_Z_H)
    MZ=(ZLow)|(ZHigh<<8)
    if MZ>=32768:
        MZ-=65536
    return MZ
def getHeading(x,y):
    heading=math.atan2(y,x)*RadToDeg
    return heading
