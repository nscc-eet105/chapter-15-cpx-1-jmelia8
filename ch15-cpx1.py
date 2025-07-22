#Joe Melia EET-107
from adafruit_circuitplayground import cp
import time

class Region:
    def __init__(self, color, leds):
        self.__color = color
        self.__leds = leds

    def get_color(self):
        return self.__color
    def get_leds(self):
        return self.__leds

    def set_color(self, color):
        self.__color = color
    def set_leds(self, leds):
        self.__leds = leds

    def all_on(self):
        for on in self.__leds:
            cp.pixels[on] = self.__color

    def all_off(self):
        for off in self.__leds:
            cp.pixels[off] = (0, 0, 0)

yellow = Region((255, 255, 0), (5, 6, 7))
blue = Region((0, 0, 255), (2, 3, 4))

while True:
    yellow.all_on()
    time.sleep(0.5)
    yellow.all_off()
    blue.all_on()
    time.sleep(0.5)
    blue.all_off()
