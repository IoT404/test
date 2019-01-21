#!/usr/bin/env python
import RPi.GPIO as GPIO

import time

LED = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(LED, True)
    time.sleep(1)
    GPIO.output(LED, False)
    time.sleep(1)
