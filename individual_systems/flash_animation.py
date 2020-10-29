#LIBRARIES
import opc
import random
from time import sleep
client = opc.Client('localhost:7890')

led_colour = [(255,255,255)]*360
#DEFINITIONS - SYSTEMS
def update():
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)


def damage():
    global led_colour
    for x in range(0, 2):     
        led_colour = [(90, 90, 100)]*360
        update()
        sleep(0.05)
        led_colour = [(255, 255, 255)]*360
        update()
        sleep(0.05)


damage()
update()