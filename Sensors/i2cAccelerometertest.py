import smbus
import math
from LSM9DS1 import *

def getAccel():
   #Grab X Data
   XLow=i2c.read_byte_data(ACC_ADD,ACC_X_L)
   XHigh=i2c.read_byte_data(ACC_ADD,ACC_X_H)
   X=((XLow)|(XHigh<<8))
   if X>=32678:
      X-=65536
   X=X*ARES
   #Grab Y Data
   YLow=i2c.read_byte_data(ACC_ADD,ACC_Y_L)
   YHigh=i2c.read_byte_data(ACC_ADD,ACC_Y_H)
   Y=(YLow)|(YHigh<<8)
   if Y>=32678:
       Y-=65536
   Y=Y*ARES
   #Grab Z Data
   ZLow=i2c.read_byte_data(ACC_ADD,ACC_Z_L)
   ZHigh=i2c.read_byte_data(ACC_ADD,ACC_Z_H)
   Z=(ZLow)|(ZHigh<<8)
   if Z>=32768:
      Z-=65536
   Z=Z*ARES
   print ("X: ") + str(X)# + ("   Sense Hat X: ") + str(x)
   print ("Y: ") + str(Y)# + ("   Sense Hat Y: ") + str(y)
   print ("Z: ") + str(Z)# + ("   Sense Hat Z: ") + str(z)

#Misc Values
   
ARES=(4.0/32768.0)

#Set i2c Bus

i2c=smbus.SMBus(1)

#x,y,z=sense.get_accelerometer_raw().values()
i2c.write_byte_data(ACC_ADD,CTRL_REG1,0b00100010)
i2c.write_byte_data(ACC_ADD,CTRL_REG6,0b00110000)


