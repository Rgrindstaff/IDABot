import smbus
import math

#Set Addresses

IMU=0x6b
WHO_I_AM=0x0f
CTRL_REG1=0x10
CTRL_REG4=0x1e

GXL=0x18
GXH=0x19
GYL=0x1a
GYH=0x1b
GZL=0x1c
GZH=0x1d
GSEN=0.07
GRES=(245.0/32768.0)



#Set I2C Bus

i2c=smbus.SMBus(1)

#Control Registers
i2c.write_byte_data(IMU,CTRL_REG1,0b00100000)
i2c.write_byte_data(IMU,CTRL_REG4,0b00111000)

#Grab X Data

XLow=i2c.read_byte_data(IMU,GXL)
XHigh=i2c.read_byte_data(IMU,GXH)
X=(XLow)|(XHigh<<8)
if X >= 32768:
    X-=65536
X=X*GRES*GSEN
print ("X: ") + str(X)

#Grab Y Data

YLow=i2c.read_byte_data(IMU,GYL)
YHigh=i2c.read_byte_data(IMU,GYH)
Y=(YLow)|(YHigh<<8)
if Y >= 32768:
    Y-=65536
Y=Y*GRES*GSEN
print ("Y: ") + str(Y)

#Grab Z Data

ZLow=i2c.read_byte_data(IMU,GZL)
ZHigh=i2c.read_byte_data(IMU,GZH)
Z=(ZLow)|(ZHigh<<8)
if Z >= 32768:
    Z-=65536
Z=Z*GRES*GSEN
print ("Z: ") + str(Z)

REVX=X/360
REVY=Y/360
REVZ=Z/360
print ("REV/S X: ") + str(REVX)
print ("REV/S Y: ") + str(REVY)
print ("REV/S Z: ") + str(REVZ)
