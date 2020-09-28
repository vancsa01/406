#test_serial.py test to communicate with STM board

import serial
import time

ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

while True:
    char = ser.read()
    char = char.decode('utf-8')
    if char != '\0':
        print(char, end = '')
    
ser.close()