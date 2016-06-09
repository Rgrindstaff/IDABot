import smbus
import math
import time

def getAccel():
   #Grab X Data
   XLow=i2c.read_byte_data(IMU,MXL)
   XHigh=i2c.read_byte_data(IMU,MXH)
   X=((XLow)|(XHigh<<8))
   if X>=32678:
      X-=65536
   X=X*ARES
   #Grab Y Data
   YLow=i2c.read_byte_data(IMU,MYL)
   YHigh=i2c.read_byte_data(IMU,MYH)
   Y=(YLow)|(YHigh<<8)
   if Y>=32678:
       Y-=65536
   Y=Y*ARES
   #Grab Z Data
   ZLow=i2c.read_byte_data(IMU,MZL)
   ZHigh=i2c.read_byte_data(IMU,MZH)
   Z=(ZLow)|(ZHigh<<8)
   if Z>=32768:
      Z-=65536
   Z=Z*ARES
   print ("X: ") + str(X)# + ("   Sense Hat X: ") + str(x)
   #print ("Y: ") + str(Y)# + ("   Sense Hat Y: ") + str(y)
   #print ("Z: ") + str(Z)# + ("   Sense Hat Z: ") + str(z)

#Set Addresses

IMU=0x6b
WHO_I_AM=0x0f
MXL=0x28
MXH=0x29
MYL=0x2a
MYH=0x2b
MZL=0x2c
MZH=0x2d
ARES=(4.0/32768.0)
CTRL_REG1=0x10
CTRL_REG6=0x20

#Set i2c Bus

i2c=smbus.SMBus(1)

#Check Device ID

#ID=i2c.read_byte_data(IMU,WHO_I_AM)
#print ("Device ID: ") + str(ID)

#x,y,z=sense.get_accelerometer_raw().values()
i2c.write_byte_data(IMU,CTRL_REG1,0b00100010)
i2c.write_byte_data(IMU,CTRL_REG6,0b00110000)


for x in range (100):
   getAccel()
   time.sleep(1)

