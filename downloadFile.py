import serial
import sys
import glob

port = input("list port from discoverPorts.py: ")
print(port)

ser = serial.Serial(port)
ser.flushInput()
ser.write(b'h')
while True:
    line = ser.readline()
    if line == b'Done reading\r\n':
        print("exiting")
        break
    else:
        file.write(line)


file.close()
