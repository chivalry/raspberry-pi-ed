from gpiozero import LED
from time import sleep

LED_A = LED(4)
LED_B = LED(17)
LED_C = LED(27)
LED_D = LED(22)
LED_E = LED(5)
LED_F = LED(6)
LED_G = LED(13)

LEDS = [LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G]

ONE = [LED_B, LED_C]
TWO = [LED_A, LED_B, LED_G, LED_E, LED_D]
THREE = [LED_A, LED_B, LED_G, LED_C, LED_D]
FOUR = [LED_F, LED_G, LED_B, LED_C]
FIVE = [LED_A, LED_F, LED_G, LED_C, LED_D]
SIX = [LED_A, LED_F, LED_G, LED_C, LED_D, LED_E]
SEVEN = [LED_A, LED_B, LED_C]
EIGHT = [LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G]
NINE = [LED_A, LED_B, LED_C, LED_F, LED_G]
ZERO = [LED_A, LED_B, LED_C, LED_D, LED_E, LED_F]

COUNTDOWN = [NINE, EIGHT, SEVEN, SIX, FIVE, FOUR, THREE, TWO, ONE, ZERO]

if __name__ == '__main__':
    print('Press Ctrl-C to quit.')
    while True:
        for digit in COUNTDOWN:
            for led in digit:
                led.on()
            sleep(1)
            for led in digit:
                led.off()
