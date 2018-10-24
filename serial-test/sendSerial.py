import serial
import sys
import time


ser = serial.Serial(
    port='COM7',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=1)

print("connected to: " + ser.portstr)
i = 0x00
while True:
    #ser.write("robot")
    ser.write('G0 X100 Y100')
    time.sleep(1.0)
    ser.write('G0 X100 Y500')
    time.sleep(1.0)
ser.close()
