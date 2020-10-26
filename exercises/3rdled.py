import opc
from time import sleep    
import numpy
import colorsys
client = opc.Client('localhost:7890')

s = 1.0
v = 1.0
pixels = []


for hue in range(360):
    
    rgb = (255,255,255) 
    pixels.append(rgb)


while True:
     for i in range(360):
         client.put_pixels(pixels)
         #need to send it twice if not constantly sending values 
         #due to interpolation setting on fadecandy
         client.put_pixels(pixels)
         pixels = numpy.roll(pixels, 60)
         sleep(0.02)