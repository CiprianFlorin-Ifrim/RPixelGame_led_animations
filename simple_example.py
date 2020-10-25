#to use simulator

import opc
import random
import numpy
from time import sleep
client = opc.Client('localhost:7890')

pixels = []

for hue in range(360):
    white = (255,255,255)
    pixels.append(white)

while True:
     for i in range(360):
         yellow = (255, 255, 0)
         client.put_pixels(yellow)
         #need to send it twice if not constantly sending values 
         #due to interpolation setting on fadecandy
         client.put_pixels(yellow)
         pixels = numpy.roll(pixels, 9)
         sleep(0.2)