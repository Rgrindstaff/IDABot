import smbus
import math

def GYRX():
    GXLow=i2c.read_byte_data(IMU,GXL)
    GXHigh=i2c.read_byte_data(IMU,GXH)
    GX=(GXLow)|(GXHigh<<8)
    if GX >= 32768:
        GX-=65536
    GX=GX*GRES*GSEN
    REVX=GX/360
    return GX
def GYRY():
    GYLow=i2c.read_byte_data(IMU,GYL)
    GYHigh=i2c.read_byte_data(IMU,GYH)
    GY=(GYLow)|(GYHigh<<8)
    if GY >= 32768:
        GY-=65536
    GY=GY*GRES*GSEN
    REVY=GY/360
    return GY
def GYRZ():
    GZLow=i2c.read_byte_data(IMU,GZL)
    GZHigh=i2c.read_byte_data(IMU,GZH)
    GZ=(GZLow)|(GZHigh<<8)
    if GZ >= 32768:
        GZ-=65536
    GZ=GZ*GRES*GSEN
    REVZ=GZ/360
    return GZ
def ACCX():
    AXLow=i2c.read_byte_data(IMU,MXL)
    AXHigh=i2c.read_byte_data(IMU,MXH)
    AX=((AXLow)|(AXHigh<<8))
    if AX>=32678:
       AX-=65536
    AX=AX*ARES
    return AX
def ACCY():
    AYLow=i2c.read_byte_data(IMU,MYL)
    AYHigh=i2c.read_byte_data(IMU,MYH)
    AY=(AYLow)|(AYHigh<<8)
    if AY>=32678:
        AY-=65536
    AY=AY*ARES
    return AY
def ACCZ():
    AZLow=i2c.read_byte_data(IMU,MZL)
    AZHigh=i2c.read_byte_data(IMU,MZH)
    AZ=(AZLow)|(AZHigh<<8)
    if AZ>=32768:
       AZ-=65536
    AZ=AZ*ARES
    return AZ
    
#Set Addresses

IMU=0x6b
WHO_I_AM=0x0f
CTRL_REG1=0x10
CTRL_REG4=0x1e
CTRL_REG6=0x20

GXL=0x18
GXH=0x19
GYL=0x1a
GYH=0x1b
GZL=0x1c
GZH=0x1d
MXL=0x28
MXH=0x29
MYL=0x2a
MYH=0x2b
MZL=0x2c
MZH=0x2d
GSEN=1
GRES=(2000.0/32768.0)
ARES=(8.0/32768.0)
ASEN=1
dt=.00105042016807
tau=.05    #50 millisecond response time
PI=3.141592653589793
RadToDeg=180/PI
CFXangle=0.0
CFYangle=0.0
i=1

#Set i2c Bus

i2c=smbus.SMBus(1)

#Control Registers
i2c.write_byte_data(IMU,CTRL_REG1,0b11011000)
i2c.write_byte_data(IMU,CTRL_REG4,0b00111000)
i2c.write_byte_data(IMU,CTRL_REG4,0b11011000)

for x in range (6):
    
    for x in range (10):

        GX=GYRX()
        GY=GYRY()
        GZ=GYRZ()
        AX=ACCX()
        AY=ACCY()
        AZ=ACCZ()
        #Accel Angles
        AXangle=math.atan2(AY,AZ)*RadToDeg
        AYangle=math.atan2(AZ,AY)*RadToDeg
    
        #Complementary Filter
        CFConst=tau/(tau+dt)
        CFXangle=(1-CFConst)*(CFXangle+GX*dt)+CFConst*AXangle
        CFYangle=(1-CFConst)*(CFYangle+GY*dt)+CFConst*AYangle
    print ("Position ") + str(i) + (":")
    print ("CFX: ") + str(CFXangle) + ("    CFY: ") + str(CFYangle)
    i+=1
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

