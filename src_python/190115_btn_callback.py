import RPi.GPIO as pi
import time
pi.setmode(pi.BCM)
count = 0
pi.setup(18, pi.OUT)
def handler(channel):
	global count
	count = count + 1
	print count

pi.setup(24, pi.IN, pull_up_down=pi.PUD_DOWN)
pi.add_event_detect(24, pi.RISING, callback = handler)
while True:
	pi.output(18, True)
	time.sleep(1)
	pi.output(18, False)
	time.sleep(1)
