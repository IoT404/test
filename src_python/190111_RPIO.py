#!usr/bin/env python

import RPIO

import time

LED = 18

RPIO.setmode(RPIO.BCM)
RPIO.setup(LED, RPIO.OUT)

while (True):
	RPIO.output(LED, True)
	time.sleep(1)
	RPIO.output(LED, False)
	time.sleep(1)
