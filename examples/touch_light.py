from touchio import TouchIn
import adafruit_dotstar as dotstar
import board
import time

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)
colors = [0,0,0]

a0 = TouchIn(board.A0)
a1 = TouchIn(board.A1)
a2 = TouchIn(board.A2)

while True:
    if a0.value:
        colors[0] = 255
    else:
        colors[0] = 0

    if a1.value:
        colors[1] = 255
    else:
        colors[1] = 0

    if a2.value:
        colors[2] = 255
    else:
        colors[2] = 0

    dot[0] = colors
    dot.show()
