from digitalio import DigitalInOut, Direction
import adafruit_dotstar as dotstar
import board
import time

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
ledToggle = True

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0)
dot.show()

while True:
    ledToggle = not ledToggle
    led.value = ledToggle
    time.sleep(0.5)
