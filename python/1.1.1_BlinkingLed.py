#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

LED_PIN = 17

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LED_PIN's mode to output,and initial level to High(3.3v)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
    while True:
        print ('...LED ON')
        # Turn on LED
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
        print ('LED OFF...')
        # Turn off LED
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)

# Define a destroy function for clean up everything after the script finished
def destroy():
    # Turn off LED
    GPIO.output(LED_PIN, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
