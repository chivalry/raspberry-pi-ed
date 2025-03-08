#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)   # Set all ledPins' mode is output
        GPIO.output(i, GPIO.HIGH)  # Set all ledPins to high(+3.3V) to off led


def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()


def loop():
    while True:
        pass


if __name__ == '__main__':
    setup()
    for i in ledPins:
        GPIO.output(i, GPIO.LOW)
    time.sleep(1)
    for i in range(0, 10, 2):
        GPIO.output(ledPins[i], GPIO.HIGH)
    time.sleep(1)
    for i in range(10):
        GPIO.output(ledPins[i], GPIO.HIGH)
    time.sleep(1)
    for i in range(0, 10, 2):
        GPIO.output(ledPins[i], GPIO.LOW)
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
