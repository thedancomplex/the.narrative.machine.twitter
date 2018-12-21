import serial
import sys
import time
import random
import os

ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)
# Start Drum
os.system("/home/pi/projects/the.narrative.machine.twitter/drumOn.sh &")
#os.system("./drumOn.sh &")
time.sleep(20.0)

print("connected to: " + ser.portstr)
time.sleep(5.0)
theMin = 200
theMax = 500
theMid = (500-200)/1.0
theStr = 'G0 X' + str(theMid) + ' Y' + str(theMid) + '\r'
ser.write(theStr)
#os.system("sudo ./gpioHigh.sh &")
for i in range(20):
  x = random.randint(theMin,theMax)
  y = random.randint(theMin,theMax)
  onOff = random.randint(1,10)
  theStr = 'G0 X' + str(x) + ' Y' + str(y) + '\r'
  ser.write(theStr)
  time.sleep(0.1)
  ser.write('G98\r')
  #if(onOff == 0):
  #    ser.write('G99\r')
  #else:
  #    ser.write('G98\r')
  print theStr + ' motor = ' + str(onOff)
  time.sleep(1.9)
#ser.write('G0 X300 Y300\r')
ser.write('G99\r')
time.sleep(0.5)
#os.system("sudo ./gpioLow.sh &")

# Drum Off
time.sleep(5.0)
os.system("/home/pi/projects/the.narrative.machine.twitter/drumOff.sh")

ser.close()
