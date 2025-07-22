#Joe Melia EET-107
from adafruit_circuitplayground import cp
import time

class Region:
    def __init__(self, color, leds, tone):
        self.__color = color
        self.__leds = leds
        self.__tone = tone

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

    def play_tone(self, duration):
        cp.play_tone(self.__tone, duration)

regions = {"yellow": Region((255, 255, 0), (5, 6, 7), 252),
           "blue": Region((0, 0, 255), (2, 3, 4), 209),
           "red": Region((255, 0, 0), (7, 8, 9), 310),
           "green": Region((0, 255, 0), (0, 1, 2), 415)}

while True:
    for color, region in regions.items():
        region.all_on()
        region.play_tone(0.5)
        time.sleep(0.5)
        region.all_off()
        time.sleep(0.5)
