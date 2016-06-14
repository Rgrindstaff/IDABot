import smbus
import math
from LSM9DS1 import *

#Misc Values

GSEN=0.07
GRES=(245.0/32768.0)


#Set I2C Bus

i2c=smbus.SMBus(1)

#Control Registers
i2c.write_byte_data(GYR_ADD,CTRL_REG1,0b00100000)
i2c.write_byte_data(GYR_ADD,CTRL_REG4,0b00111000)

#Grab X Data

XLow=i2c.read_byte_data(GYR_ADD,GYR_X_L)
XHigh=i2c.read_byte_data(GYR_ADD,GYR_X_H)
X=(XLow)|(XHigh<<8)
if X >= 32768:
    X-=65536
X=X*GRES*GSEN
print ("X: ") + str(X)

#Grab Y Data

YLow=i2c.read_byte_data(GYR_ADD,GYR_Y_L)
YHigh=i2c.read_byte_data(GYR_ADD,GYR_Z_H)
Y=(YLow)|(YHigh<<8)
if Y >= 32768:
    Y-=65536
Y=Y*GRES*GSEN
print ("Y: ") + str(Y)

#Grab Z Data

ZLow=i2c.read_byte_data(GYR_ADD,GYR_Z_L)
ZHigh=i2c.read_byte_data(GYR_ADD,GYR_Z_H)
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
