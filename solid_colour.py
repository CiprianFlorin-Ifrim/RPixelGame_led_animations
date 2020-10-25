import opc
client = opc.Client('localhost:7890')

#create list with 1 tuple, then make it 10 long
led_colour = [(0,0,0)]*360
led_colour[60]=(255,255,0)

def update_led(led_colour):
   client.put_pixels(led_colour)
   #need to send it twice if not constantly sending values 
   #due to interpolation setting on fadecandy
   client.put_pixels(led_colour)








#to use simulator


