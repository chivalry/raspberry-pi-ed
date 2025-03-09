#!/usr/bin/env python3

from gpiozero import Button

button = Button(2)
print('Waiting for press...')
button.wait_for_press()
print('Button was pressed!')
