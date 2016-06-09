import smbus
import math

def getHeading():
    
    #Grab X Data
    
    XLow=i2c.read_byte_data(IMU,MXL)
    XHigh=i2c.read_byte_data(IMU,MXH)
    XRAW=((XLow)|(XHigh<<8))
    if XRAW>=32768:
        XRAW-=65536
    X=XRAW
    
    #Grab Y Data
    
    YLow=i2c.read_byte_data(IMU,MYL)
    YHigh=i2c.read_byte_data(IMU,MYH)
    YRAW=(YLow)|(YHigh<<8)
    if YRAW>=32678:
        YRAW-=65536
    Y=YRAW
    
    #Grab Z Data
    
    ZLow=i2c.read_byte_data(IMU,MZL)
    ZHigh=i2c.read_byte_data(IMU,MZH)
    ZRAW=(ZLow)|(ZHigh<<8)
    if ZRAW>=32768:
        ZRAW-=65536
    Z=ZRAW    
    
    #Determine Heading
    heading=math.atan2(Y,X)*RadToDeg

    return heading

#Set Addresses

IMU=0x1e
WHO_I_AM=0x0f
CTRL_REG1_M=0x20
CTRL_REG2_M=0x21
CTRL_REG3_M=0x22
CTRL_REG4_M=0x23
CTRL_REG5_M=0x24
MXL=0x28
MXH=0x29
MYL=0x2a
MYH=0x2b
MZL=0x2c
MZH=0x2d
PI=3.1415926
RadToDeg=180/PI

#Set i2c Bus

i2c=smbus.SMBus(1)

#Check Device ID

ID=i2c.read_byte_data(IMU,WHO_I_AM)
print ("Device ID: ") + str(ID)

#Initialize Magnetometer
i2c.write_byte_data(IMU,CTRL_REG2_M, 0b01100000)
i2c.write_byte_data(IMU,CTRL_REG3_M, 0b00000000)
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


    #print ("Heading: ") + str(heading)
mean=total/i
if mean <0:
    mean+=360
print ("Mean Heading: ") + str(mean)
print ("Max Heading: ") + str(maximum)
print ("Min Heading: ") + str(minimum)

