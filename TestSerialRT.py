import time
import serial

port  = "/dev/ttyS0"
baud = 38400
timeout = 3

ser = serial.Serial(port = port, baudrate = baud, timeout = timeout)

i = 0

while (i < 10):
    time.sleep(1)
    print ("writing " + str(ser.write('T')) + " bytes")
    print (str(ser.inWaiting()) + " bytes waiting")
    print ("reading: " + ser.read())
    i = i + 1
