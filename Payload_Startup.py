import time, threading
import subprocess
import datetime
import io
import sys
import os
import string
import re
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN)
GPIO.setup(16,GPIO.IN)

inPin = GPIO.input(18)

if (inPin == 1):
	subP = subprocess.Popen(['python','Refactored_RFD_python_Pi.py'])

while (inPin == 1):
	inPin = GPIO.input(18)
	#print "running"
	if (subP.poll() != None):
		os.chdir("/home/pi/RFD_Payload")
		subP = subprocess.Popen(['python','Refactored_RFD_python_Pi.py'])

try:
	subP.kill()
except NameError:
	print "process did not start"

print "sleeping process"

time.sleep(6)

print "testing for shutdown"

if (GPIO.input(16) == 1):
	subprocess.call("sudo shutdown -h now", shell=True)

