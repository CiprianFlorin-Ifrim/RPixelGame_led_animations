#LIBRARIES
import opc
import random
from time import sleep
client = opc.Client('localhost:7890')
import colorsys

#DEFINITIONS - SYSTEMS
def update():
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)
    
#BACKGROUND
led_colour = [(255,255,255)]*360
update()
s = 1.0
v = 1.0
colour = []
led_colour = [(255,255,255)]*360



#MAIN CODE
#RGB 250, 250, 85 = YELLOW               
def won():
    #HEART BLACK CONTOUR
    #SIXTH ROW                                #FIFTH ROW                                         
    led_colour[328]=(0,0,0);                  led_colour[265]=(0,0,0);                  
    led_colour[331]=(0,0,0);                  led_colour[274]=(0,0,0);                  
    #FORTH ROW                                #THIRD ROW 
    led_colour[203]=(0,0,0);                  led_colour[141]=(0,0,0); 
    led_colour[216]=(0,0,0);                  led_colour[158]=(0,0,0);                                             
    #SECOND ROW                               #FIRST ROW - FIRST HALF  
    led_colour[81]=(0,0,0);                   led_colour[22]=(0,0,0); 
    led_colour[98]=(0,0,0);                   led_colour[27]=(0,0,0);  
    #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF                                 
    led_colour[32]=(0,0,0);                   led_colour[37]=(0,0,0);
    update() 
    
    for c in range(360):
        rgb_colorsys = colorsys.hsv_to_rgb(c/360.0, s, v)
        
        r_value = rgb_colorsys[0]
        g_value = rgb_colorsys[1]
        b_value = rgb_colorsys[2]
       
        colour = (r_value*255, g_value*225, b_value*255)
        
        #BACKGROUND COLOR SHIFT
        #FIRST ROW
        for x in range(0, 22):    led_colour[x] =(colour); 
        for x in range(28, 32):   led_colour[x] =(colour); 
        for x in range(38, 60):   led_colour[x] =(colour);
        #SECOND ROW
        for x in range(60, 81):   led_colour[x] =(colour); 
        for x in range(99, 120): led_colour[x] =(colour);
        #THIRD ROW
        for x in range(120, 141): led_colour[x] =(colour); 
        for x in range(159, 180): led_colour[x] =(colour);
        #FORTH ROW
        for x in range(180, 203): led_colour[x] =(colour); 
        for x in range(217, 240): led_colour[x] =(colour);
        #FIFTH ROW
        for x in range(240, 265): led_colour[x] =(colour);
        for x in range(267, 300): led_colour[x] =(colour);
        #SIXTH ROW        
        for x in range(300, 328): led_colour[x] =(colour);
        for x in range(332, 360): led_colour[x] =(colour); 
                             
        #HEART FLASHING - RED/YELLOW                             
        for x in range(33, 37):   led_colour[x] =(255, 0, 17); 
        for x in range(23, 27):   led_colour[x] =(255, 0, 17); 
        for x in range(82, 98):   led_colour[x] =(255, 0, 17);
        for x in range(329, 331): led_colour[x] =(255, 0, 17); 
        for x in range(266, 274): led_colour[x] =(255, 0, 17);
        for x in range(204, 216): led_colour[x] =(255, 0, 17); 
        for x in range(142, 158): led_colour[x] =(255, 0, 17);
        update(); sleep(0.1)
        for x in range(33, 37):   led_colour[x] =(250, 250, 85); 
        for x in range(23, 27):   led_colour[x] =(250, 250, 85); 
        for x in range(82, 98):   led_colour[x] =(250, 250, 85);
        for x in range(329, 331): led_colour[x] =(250, 250, 85); 
        for x in range(266, 274): led_colour[x] =(250, 250, 85);
        for x in range(204, 216): led_colour[x] =(250, 250, 85); 
        for x in range(142, 158): led_colour[x] =(250, 250, 85);
        update(); sleep(0.1)     
        


won()