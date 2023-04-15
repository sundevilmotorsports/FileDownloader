import serial
import sys
import glob

port = input("list port from discoverPorts.py: ")
print(port)


ser = serial.Serial(port)
ser.flushInput()
ser.write(b's')

num = input("input run number to download: ")
file = open("run" + str(num) + ".csv", "wb")

num += "-"
ser.write(num.encode())
ser.flush()
print("doing things...")
while True:
    line = ser.readline()
    print(line)
    if line == b'Done reading\r\n':
        print("exiting")
        break
    else:
        file.write(line)

file.close()
