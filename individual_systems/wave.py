import opc
from time import sleep    
import numpy
import colorsys
client = opc.Client('localhost:7890')

s = 1.0
v = 1.0
pixels = []
led_colour = [(255,255,255)]*360


for hue in range(360):
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
    print(rgb_fractional)
    
    r_float = rgb_fractional[0]
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]
    
    
    rgb = (r_float*255, g_float*225, b_float*255)
    pixels.append(rgb)


while True:
     for i in range(360):
         client.put_pixels(pixels)
         #need to send it twice if not constantly sending values 
         #due to interpolation setting on fadecandy
         client.put_pixels(pixels)
         pixels = numpy.roll(pixels, 60)
         sleep(0.02)