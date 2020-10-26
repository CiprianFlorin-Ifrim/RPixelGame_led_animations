import opc
import random
import numpy
from time import sleep
client = opc.Client('localhost:7890')

led_colour = [(0,0,0)]*360

colours = { 'blue' : (0, 0, 255), 'red' : (255, 0 , 0)}

def update_led(led_colour):
          client.put_pixels(led_colour)
          #need to send it twice if not constantly sending values 
          #due to interpolation setting on fadecandy
          client.put_pixels(led_colour)
  
led_colour = [(0,0,0)]*360
update_led(led_colour)  

def full(colour1, colour2, sleept):
  # for x in range(0, 1):
     #  led_colour[x] = (colours.get(colour1))
       led_colour[10] = (colours.get(colour2))
     #  led_colour[x+120] = (colours.get(colour1))
     #  led_colour[x+180] = (colours.get(colour2))
     #  led_colour[x+240] = (colours.get(colour1))
      # led_colour[x+300] = (colours.get(colour2))
       update_led(led_colour)
       sleep(sleept)
       
       
full('blue', 'red', 0.1)
