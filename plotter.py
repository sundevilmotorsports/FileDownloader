import serial
import sys
import glob


"""
def download():
    ser = serial.Serial('COM3')
    ser.flushInput()
    ser.write(b'h')
    file = open('run.csv', 'wb')

    while True:
        line = ser.readline()
        if line == b'I received: 104\r\n':
            print("exiting")
            break
        else:
            file.write(line)
        print(line)

    file.close()

#['COM'7]
"""



def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())
