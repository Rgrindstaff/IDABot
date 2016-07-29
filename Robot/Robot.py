import serial
import time
ser = serial.Serial('/dev/ttyS0', 115200)

def Forward(Power1, Power2, length):
    x=0
    for x in range (0,length):
        ser.write('!R')
        ser.write('\r')
        ser.write('!G')
        ser.write(' ')
        ser.write('1')
        ser.write(' ')
        ser.write('%d' %(Power1))
        ser.write('\r')
    
        ser.write('!G')
        ser.write(' ')
        ser.write('2')
        ser.write(' ')
        ser.write('%d' %(-Power2))
        ser.write('\r')
        x+=1
        time.sleep(1)
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')

def Right(Power1, Power2, length):
    x=0
    for x in range (0,length):
        ser.write('!R')
        ser.write('\r')
        ser.write('!G')
        ser.write(' ')
        ser.write('1')
        ser.write(' ')
        ser.write('%d' %(Power1))
        ser.write('\r')
    
        ser.write('!G')
        ser.write(' ')
        ser.write('2')
        ser.write(' ')
        ser.write('%d' %(Power2))
        ser.write('\r')
        x+=1
        time.sleep(1)
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    
def Left(Power1, Power2, length):
    x=0
    for x in range (0,length):
        ser.write('!R')
        ser.write('\r')
        ser.write('!G')
        ser.write(' ')
        ser.write('1')
        ser.write(' ')
        ser.write('%d' %(-Power1))
        ser.write('\r')
    
        ser.write('!G')
        ser.write(' ')
        ser.write('2')
        ser.write(' ')
        ser.write('%d' %(-Power2))
        ser.write('\r')
        x+=1
        time.sleep(1)
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    
def Reverse(Power1, Power2, length):
    x=0
    for x in range (0,length):
        ser.write('!R')
        ser.write('\r')
        ser.write('!G')
        ser.write(' ')
        ser.write('1')
        ser.write(' ')
        ser.write('%d' %(-Power1))
        ser.write('\r')
    
        ser.write('!G')
        ser.write(' ')
        ser.write('2')
        ser.write(' ')
        ser.write('%d' %(Power2))
        ser.write('\r')
        x+=1
        time.sleep(1)
    ser.write('!G')
    ser.write(' ')
    ser.write('1')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
    ser.write('!G')
    ser.write(' ')
    ser.write('2')
    ser.write(' ')
    ser.write('0')
    ser.write('\r')
def GetVoltage():
    ser.write('?V')
    ser.write('\r')
    V = ser.readline(18)
    print str(V)
    return
def RunScript():
    ser.write('!R')
    ser.write('\r')
def GetMotorAmps(MotorNumber):
    ser.write('?A')
    ser.write('%d' %(MotorNumber))
    ser.write('\r')
    A = ser.readline(18)
    print str(A)
def GetBatteryAmps():
    ser.write('?BA')
    ser.write('\r')
    BA = ser.readline(18)
    print str(BA)
def GetAbsoluteEncoder(MotorNumber):
    ser.write('?C')
    ser.write('%d' %(MotorNumber))
    ser.write('\r')
    EA = ser.readline(18)
    print str(EA)
    
