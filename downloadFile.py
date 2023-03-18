import serial
import sys
import glob

port = input("list port from discoverPorts.py: ")
print(port)


ser = serial.Serial(port)
ser.flushInput()
ser.write(b'h')

"""
file = open("savedData.csv", 'wb')
while True:
    line = ser.readline()
    if line == b'Done reading\r\n':
        print("exiting")
        break
    else:
        file.write(line)
file.close()
"""
num = 0
file = None
while True:
    line = ser.readline()
    if line == b'File:\r\n':
        if file is not None:
            file.close()
        file = open(("data" + str(num) + ".csv"), "wb")
        continue
    elif line == b'Done reading\r\n':
        print("exiting")
        break
    else:
        file.write(line)

file.close()
