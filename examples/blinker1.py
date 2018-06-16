from digitalio import DigitalInOut, Direction
import board
import time

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
ledToggle = True

while True:
    ledToggle = not ledToggle
    led.value = ledToggle
    time.sleep(0.5)
