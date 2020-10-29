import opc
from time import sleep
client = opc.Client('localhost:7890')

def update():
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

#BACKGROUND
led_colour = [(255,255,255)]*360

def full(sleept):
    for x in range(0, 60):
        led_colour[x] = (255, 255, 255)
        led_colour[x+60] = (90, 90, 100)
        led_colour[x+120] = (255, 255, 255)
        led_colour[x+180] = (90, 90, 100)
        led_colour[x+240] = (255, 255, 255)
        led_colour[x+300] = (90, 90, 100)
        update()
        sleep(sleept)
           
full(0.05)           