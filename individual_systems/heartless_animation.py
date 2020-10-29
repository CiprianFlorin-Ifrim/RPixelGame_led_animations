import opc
from time import sleep
client = opc.Client('localhost:7890')

def update():
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

def blinking(delay, value):
    for x in range(0, value):
        #--------------------------------------------- H E A L T H    F U L L  --------------------------------------------------------------------
        #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
        #SIXTH ROW                                #SIXTH ROW                                #SIXTH ROW
        led_colour[308]=(0,0,0);                  led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
        led_colour[311]=(0,0,0);                  led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
        #FIFTH ROW                                #FIFTH ROW   
        led_colour[245]=(0,0,0);                  led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
        led_colour[254]=(0,0,0);                  led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
        #FORTH ROW                                #FORTH ROW                                #FORTH ROW
        led_colour[183]=(0,0,0);                  led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
        led_colour[196]=(0,0,0);                  led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
        #THIRD ROW                                #THIRD ROW                                #THIRD ROW
        led_colour[121]=(0,0,0);                  led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
        led_colour[138]=(0,0,0);                  led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
        #SECOND ROW                               #SECOND ROW                               #SECOND ROW
        led_colour[61]=(0,0,0);                   led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
        led_colour[78]=(0,0,0);                   led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
        #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
        led_colour[2]=(0,0,0);                    led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
        led_colour[7]=(0,0,0);                    led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
        #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
        led_colour[12]=(0,0,0);                   led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
        led_colour[17]=(0,0,0);                   led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)

        for x in range(309, 311): led_colour[x] =(255, 0, 17);
        for x in range(329, 331): led_colour[x] =(255, 0, 17);
        for x in range(349, 351): led_colour[x] =(255, 0, 17);
        for x in range(309, 310): led_colour[x] =(255, 0, 17);
        for x in range(246, 254): led_colour[x] =(255, 0, 17);
        for x in range(266, 275): led_colour[x] =(255, 0, 17);
        for x in range(286, 294): led_colour[x] =(255, 0, 17);
        for x in range(184, 196): led_colour[x] =(255, 0, 17);
        for x in range(204, 216): led_colour[x] =(255, 0, 17);
        for x in range(224, 236): led_colour[x] =(255, 0, 17);
        for x in range(122, 138): led_colour[x] =(255, 0, 17);
        for x in range(142, 158): led_colour[x] =(255, 0, 17);
        for x in range(162, 178): led_colour[x] =(255, 0, 17);
        for x in range(62, 78):   led_colour[x] =(255, 0, 17);
        for x in range(82, 98):   led_colour[x] =(255, 0, 17);
        for x in range(102, 118): led_colour[x] =(255, 0, 17);
        for x in range(3, 7):     led_colour[x] =(255, 0, 17);
        for x in range(23, 27):   led_colour[x] =(255, 0, 17);
        for x in range(43, 47):   led_colour[x] =(255, 0, 17);
        for x in range(13, 17):   led_colour[x] =(255, 0, 17);
        for x in range(33, 37):   led_colour[x] =(255, 0, 17);
        for x in range(53, 57):   led_colour[x] =(255, 0, 17);

        update()
        sleep(delay)

        #---------------------------------- H E A L T H    F U L L Y    D E P L E T E D -----------------------------------------------------------
        #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
        #SIXTH ROW                                #SIXTH ROW                                #SIXTH ROW
        led_colour[308]=(0,0,0);                  led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
        led_colour[311]=(0,0,0);                  led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
        #FIFTH ROW                                #FIFTH ROW   
        led_colour[245]=(0,0,0);                  led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
        led_colour[254]=(0,0,0);                  led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
        #FORTH ROW                                #FORTH ROW                                #FORTH ROW
        led_colour[183]=(0,0,0);                  led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
        led_colour[196]=(0,0,0);                  led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
        #THIRD ROW                                #THIRD ROW                                #THIRD ROW
        led_colour[121]=(0,0,0);                  led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
        led_colour[138]=(0,0,0);                  led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
        #SECOND ROW                               #SECOND ROW                               #SECOND ROW
        led_colour[61]=(0,0,0);                   led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
        led_colour[78]=(0,0,0);                   led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
        #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
        led_colour[2]=(0,0,0);                    led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
        led_colour[7]=(0,0,0);                    led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
        #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
        led_colour[12]=(0,0,0);                   led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
        led_colour[17]=(0,0,0);                   led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)
        
        for x in range(309, 311): led_colour[x] =(90, 90, 100);
        for x in range(329, 331): led_colour[x] =(90, 90, 100);
        for x in range(349, 351): led_colour[x] =(90, 90, 100);
        for x in range(309, 310): led_colour[x] =(90, 90, 100);
        for x in range(246, 254): led_colour[x] =(90, 90, 100);
        for x in range(266, 275): led_colour[x] =(90, 90, 100);
        for x in range(286, 294): led_colour[x] =(90, 90, 100);
        for x in range(184, 196): led_colour[x] =(90, 90, 100);
        for x in range(204, 216): led_colour[x] =(90, 90, 100);
        for x in range(224, 236): led_colour[x] =(90, 90, 100);
        for x in range(122, 138): led_colour[x] =(90, 90, 100);
        for x in range(142, 158): led_colour[x] =(90, 90, 100);
        for x in range(162, 178): led_colour[x] =(90, 90, 100);
        for x in range(62, 78):   led_colour[x] =(90, 90, 100);
        for x in range(82, 98):   led_colour[x] =(90, 90, 100);
        for x in range(102, 118): led_colour[x] =(90, 90, 100);
        for x in range(3, 7):     led_colour[x] =(90, 90, 100);
        for x in range(23, 27):   led_colour[x] =(90, 90, 100);
        for x in range(43, 47):   led_colour[x] =(90, 90, 100);
        for x in range(13, 17):   led_colour[x] =(90, 90, 100);
        for x in range(33, 37):   led_colour[x] =(90, 90, 100);
        for x in range(53, 57):   led_colour[x] =(90, 90, 100);

        update() 
        sleep(delay)

#BACKGROUND
led_colour = [(255,255,255)]*360

#MAIN CODE
blinking(1, 5)