#! /usr/bin/env python
import RPi.GPIO as pi
import time
pi.setmode(pi.BCM)
pi.setup(18, pi.OUT)
pi.setup(24, pi.IN, pull_up_down = pi.PUD_DOWN)
ledstate = False

def ISR_body(notuse):
	global ledstate
	ledstate = ~ledstate
	pi.output(18, ledstate)

pi.add_event_detect(24, pi.RISING, callback = ISR_body)

while (True):
	time.sleep(1)
