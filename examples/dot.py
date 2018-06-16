import adafruit_dotstar as dotstar
import board
import time

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)
dot[0] = [0,0,255]
dot.show()
