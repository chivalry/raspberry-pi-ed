import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

print('Setting up pins...')
GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

pattern = '11111111'

GPIO.output(PIN_LATCH, 0)
print('Sending pattern...')
for bit in pattern:
    GPIO.output(PIN_DATA, int(bit))
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)

print('Latch...')
GPIO.output(PIN_LATCH, 1)
print('Done!')

while True:
    pass
GPIO.cleanup()
