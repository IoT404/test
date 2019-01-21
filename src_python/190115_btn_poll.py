import RPi.GPIO as Z
import time
Z.setmode(Z.BCM)
Z.setup(24, Z.IN)
count = 0
while True:
	value = Z.input(24)
	if value == True:
		count = count + 1
		print count
	time.sleep(0.1)
