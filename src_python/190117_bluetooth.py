#!/usr/bin/env python
import serial
import time

ser = serial.Serial('/dev/ttyAMA0',9600)
ser.flushInput()

while True: 
	print (ser.read()) 
	time.sleep(0.1)
