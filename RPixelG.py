#LIBRARIES
import opc                                                                                         #Import simulator library
import random                                                                                      #Import library for generating random values
import colorsys                                                                                    #HSV color space to RGB conversion for LED assegnation
import winsound                                                                                    #Audio library to play sounds - Windows Only
from time import sleep                                                                             #Delay library

#VARIABLES 
client = opc.Client('localhost:7890')                                                              #Simulator address
boss_health = int()                                                                                #Empty variable to store boss health from dictionary once randomly generated
remaining_boss_health = int()                                                                      #Remaining boss hp
total_hp = 300                                                                                     #Total player hp
remaining_hp = int()                                                                               #Remaining player hp
s = 1.0                                                                                            #Saturation value for ColorSys
v = 1.0                                                                                            #Value for Colorsys
colour = []                                                                                        #Empty variable which will hold RGB values for "WON" animation
times = [1, 2]                                                                                     #Create a new list for how many times the swipe animation can run

#DEFINITIONS - SYSTEMS
def update():                                                                                      #Definition to update LED colour
    client.put_pixels(led_colour)                                                                  #need to send it twice if not constantly sending values 
    client.put_pixels(led_colour)                                                                  #due to interpolation setting on fadecandy
    
def weapon(dmg, wpn):                                                                              #Definition for the turn based system
    global remaining_boss_health; global boss_health; global total_hp; global remaining_hp         #Create global variables to be able to use them throughout the entire code
    
    sound("attack.wav")                                                                            #Use definition "sound" to play attack sound
    attack = random.randint(10, 25)                                                                #Generate random value between 10 and 25 to deal damage to the player
    
    remaining_boss_health = boss_health - dmg; boss_health = remaining_boss_health                 #Deal damage to the boss based on the weapon chosen
    if boss_health > 0:                                                                            #SYSTEM CHECK: This if was required so the boss doesn't damage the player while being dead
        remaining_hp = total_hp - attack; total_hp = remaining_hp                                  #If the boss is still alive, then deal damage to the player
      
    print("\n You used", wpn, "and dealt", dmg, "damage! \n")                                      #Print string with info about weapon choice and damage dealt to the boss
    print("\n The enemy dealt", attack, "damage! \n")                                              #Print string with info about damage done to the player by the boss
    
    damage(90, 90, 100, 255, 255, 255)                                                             #Use definition "damage" to run flash animation while taking damage
    
def durability(choice, dmg_choice):                                                                #Definition to check weapon's durability. choice = weapon selected, dmg_choice = weapon damage
    durability = weapons.get(choice)                                                               #Recall dictionary item using key
    if durability > 0:                                                                             #If the durability is higher than 0 then the player can use selected weapon
        weapon(dmg_choice, choice)                                                                 #Use values inputed to send them to the "weapon" definition for the turn based system
        weapons.update({choice : durability - 1})                                                  #Update dictionary with -1 for selected weapon's durability
        durability = weapons.get(choice)                                                           #Attribute the new durability value to the durability variable
    else: 
        print("\n THE WEAPON CHOSEN HAS BEEN BROKEN! CHOOSE ANOTHER WEAPON! \n")                   #If durability is 0, then inform player to use a different weapon
    
def sound(name):                                                                                   #Definition to play sound using winsound library, wav files required inside .py file's folder
    winsound.PlaySound(name, winsound.SND_ASYNC | winsound.SND_ALIAS )                             #Play specific sound based on requirments. Note: Asynchronous play with animations
    
#DEFINITIONS - AMIMATIONS    
#LOSS OF ALL HEARTS:
def heartloss(delay, value):                                                                       #Definition for the 3 hearts to blink when the full health has been lost
    for x in range(0, value):
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
        
        #ROW DEFINITIONS AND COLOUR APPENDING
        for x in range(3, 7):     led_colour[x] =(90, 90, 100); 
        for x in range(62, 78):   led_colour[x] =(90, 90, 100);
        for x in range(82, 98):   led_colour[x] =(90, 90, 100); 
        for x in range(23, 27):   led_colour[x] =(90, 90, 100);
        for x in range(43, 47):   led_colour[x] =(90, 90, 100); 
        for x in range(13, 17):   led_colour[x] =(90, 90, 100);
        for x in range(33, 37):   led_colour[x] =(90, 90, 100); 
        for x in range(53, 57):   led_colour[x] =(90, 90, 100);
        for x in range(309, 311): led_colour[x] =(90, 90, 100); 
        for x in range(329, 331): led_colour[x] =(90, 90, 100);
        for x in range(349, 351): led_colour[x] =(90, 90, 100); 
        for x in range(309, 310): led_colour[x] =(90, 90, 100);
        for x in range(246, 254): led_colour[x] =(90, 90, 100); 
        for x in range(266, 274): led_colour[x] =(90, 90, 100);
        for x in range(286, 294): led_colour[x] =(90, 90, 100); 
        for x in range(184, 196): led_colour[x] =(90, 90, 100);
        for x in range(204, 216): led_colour[x] =(90, 90, 100); 
        for x in range(224, 236): led_colour[x] =(90, 90, 100);
        for x in range(122, 138): led_colour[x] =(90, 90, 100); 
        for x in range(142, 158): led_colour[x] =(90, 90, 100);
        for x in range(162, 178): led_colour[x] =(90, 90, 100); 
        for x in range(102, 118): led_colour[x] =(90, 90, 100);
        
        update()                                                                                   #Update led colours using "update" definition
        sleep(delay)                                                                               #Time for transition between colours 
        
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

        #ROW DEFINITIONS AND COLOUR APPENDING
        for x in range(3, 7):     led_colour[x] =(255, 0, 17); 
        for x in range(62, 78):   led_colour[x] =(255, 0, 17);
        for x in range(82, 98):   led_colour[x] =(255, 0, 17); 
        for x in range(23, 27):   led_colour[x] =(255, 0, 17);
        for x in range(43, 47):   led_colour[x] =(255, 0, 17); 
        for x in range(13, 17):   led_colour[x] =(255, 0, 17);
        for x in range(33, 37):   led_colour[x] =(255, 0, 17); 
        for x in range(53, 57):   led_colour[x] =(255, 0, 17);
        for x in range(309, 311): led_colour[x] =(255, 0, 17); 
        for x in range(329, 331): led_colour[x] =(255, 0, 17);
        for x in range(349, 351): led_colour[x] =(255, 0, 17); 
        for x in range(309, 310): led_colour[x] =(255, 0, 17);
        for x in range(246, 254): led_colour[x] =(255, 0, 17); 
        for x in range(266, 274): led_colour[x] =(255, 0, 17);
        for x in range(286, 294): led_colour[x] =(255, 0, 17); 
        for x in range(184, 196): led_colour[x] =(255, 0, 17);
        for x in range(204, 216): led_colour[x] =(255, 0, 17); 
        for x in range(224, 236): led_colour[x] =(255, 0, 17);
        for x in range(122, 138): led_colour[x] =(255, 0, 17); 
        for x in range(142, 158): led_colour[x] =(255, 0, 17);
        for x in range(162, 178): led_colour[x] =(255, 0, 17); 
        for x in range(102, 118): led_colour[x] =(255, 0, 17);

        update()                                                                                   #Update led colours using "update" definition
        sleep(delay)                                                                               #Time for transition between colours 
       
#LOSS OF A FULL HEART:
def swipe(delay):                                                                                  #Definition for animation to run when a full heart has been lost
    global led_colour                                                                              #Create/use global variable "led_colour" to append RGB value to the selected LED
    for x in range(0, 60):
        led_colour[x] = (255, 255, 255)
        led_colour[x+60] = (90, 90, 100)
        led_colour[x+120] = (255, 255, 255)
        led_colour[x+180] = (90, 90, 100)
        led_colour[x+240] = (255, 255, 255)
        led_colour[x+300] = (90, 90, 100)
        sleep(delay)
        update()                                                                                   #Update led colours using "update" definition

#DAMAGE TAKEN FLASH:                                                                               #Definition for animation to run when a full heart has been lost  
def damage(a, b, c, d, e, f):                                                                      #Values (a,b,c) for RGB colour_1. Values (d,e,f) for RGB colour_2 
    global led_colour                                                                              #Create/use global variable "led_colour" to append RGB value to the selected LED
    for x in range(0, 2):                                                                          #The for loop will be used to set how many times the flashing will happen
        led_colour = [(a, b, c)]*360                                                               #Set (a,b,c) RGB values for the first colour flash
        update()                                                                                   #Update led colours using "update" definition
        sleep(0.04)                                                                                #Time for flash speed - first colour
        led_colour = [(d, e, f)]*360                                                               #Set (a,b,c) RGB values for the first colour flash
        update()                                                                                   #Update led colours using "update" definition
        sleep(0.04)                                                                                #Time for flash speed - second colour
        
#GAME WON:
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
    update()                                                                                         #Update led colours using "update" definition
    
    for c in range(360):                                                                             #The loop will create a hue number 
        rgb_colorsys = colorsys.hsv_to_rgb(c/360.0, s, v)                                            #Use that number/360, saturation and value to create a list with RGB value
                                                                                                                       
        r_value = rgb_colorsys[0]                                                                    #Use first value from RGB list to have only the Red value from colorsys
        g_value = rgb_colorsys[1]                                                                    #Use second value from RGB list to have only the Green value from colorsys
        b_value = rgb_colorsys[2]                                                                    #Use third value from RGB list to have only the Blue value from colorsys
       
        colour = (r_value*255, g_value*225, b_value*255)                                             #Create a list called "colour" with the 3 RGB values and append them to LEDs:
        
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
        update(); sleep(0.1)                                                                       #Update led colours using "update" definition, delay between every flash
        
#UNLOCKED SECRET WEAPON:
def secret(r, g, b):                                                                               #Definition to change background colour to yellow if secret weapon has been used
    #BACKGROUND COLOR CHANGE
    #FIRST ROW
    for x in range(0, 22):    led_colour[x] =(r, g, b); 
    for x in range(28, 32):   led_colour[x] =(r, g, b);   
    for x in range(38, 60):   led_colour[x] =(r, g, b); 
    #SECOND ROW
    for x in range(60, 81):   led_colour[x] =(r, g, b);  
    for x in range(99, 120):  led_colour[x] =(r, g, b); 
    #THIRD ROW
    for x in range(120, 141): led_colour[x] =(r, g, b); 
    for x in range(159, 180): led_colour[x] =(r, g, b); 
    #FORTH ROW
    for x in range(180, 203): led_colour[x] =(r, g, b);  
    for x in range(217, 240): led_colour[x] =(r, g, b); 
    #FIFTH ROW
    for x in range(240, 265): led_colour[x] =(r, g, b); 
    for x in range(267, 300): led_colour[x] =(r, g, b); 
    #SIXTH ROW        
    for x in range(300, 328): led_colour[x] =(r, g, b); 
    for x in range(332, 360): led_colour[x] =(r, g, b);      
    update(), sleep(0.1)


    
#BACKGROUND
led_colour = [(255,255,255)]*360                                                                   #Set a white background made out of 360LEDs


#LOGO
logo = """             
                      _  
        _            /_\            _
        |`-.___,.-~'`|=|`'~-.,___,-'|
        |  __________|=|__________  |
        | |    ______|=|__________| | 
        | |   |  ____|=|_____    /| |  
        | |   | /    |=|   /    / | |  
        | |   |/   ,-|_|- / /  /  | |
        | |     / ,'|   |/ // /   | | 
        | |    /_// |/ \/ // /    | |   
        | |      /__| |/  / /     | |   
        | |     /\  | / /| /\     | |
        | |    /  \ |/ // // \    | |
        | |   /    \/ |/ //   \   | |  
        | |  /     /    //     \  | |  
        | | /     / /  /|       \ | | 
        | |/_____/ // / |________\| |
        | |     / // /| |        /__|
        \ \    / // / | |       /|  /
         \ \  /  / /| | |______/ | /
          \ \/______| | |________|/ 
           `.`.     | | |      ,','
             `.`.   | | |   ,','   
               '.`-.| | |,-'.'      
                 '..| | |..'    
                    | | |  
                    | | |   
                    | | |  
                    | | |   
                     \|/                  
                      V                  
"""; print(logo)                                                                                   #Print whole string containing the game logo

#DICTIONARIES
#Boss dictionaty containing boss name and health value
bosses = { "GANNON" : 400, "NAYDRA" : 300, "MORPHA" : 200, "GANONDORF" : 500, "TWINROVA" :  250 }
#Weapons dictionaty containing name as key to be recalled and item value representing durability
weapons = {"THE MASTER SWORD" : 9, "BOOMERANG" : 5, "KNIGHT BROADSWORD" : 6, "ZORA SWORD" : 8, "TORCH" : 4, "MOONLIGHT SCIMITAR" : 7, 
           "FLAMEBLADE" : 4, "GUARDIAN SWORD" : 7, "ICE ROD" : 4, "KOROK LEAF" : 1, "BOULDER BREAKER" : 5, "ANCIENT SWORD" : 6, "THE BOW OF LIGHT" : 3 }

#MAIN CODE      
while total_hp > 0 and boss_health <= 0:                                                           #While the player still has health left but the boss zero, select a new boss from dictionary
    #END GAME                                                                      
    if len(bosses) == 0 and boss_health <= 0:                                                      #If the dictionary containing bosses is empty, that means the player has defeated everyone
        print("\n Congratulations, you completed the game! \n")                                    #Print string congratulating the player for completing the game
        sound("gamewon.wav")                                                                       #Use definition "sound" to play game won sound
        won()                                                                                      #Run game won animation using definition called "won"
        break                                                                                      #After around 6mins when the animation completes, break and end the code
       
    #BOSS SELECTION  
    boss_selected = random.choice(list(bosses.items()))                                            #Select a random "boss"(key) from the defined dictionary
    name = boss_selected[0]                                                                        #Attribute the key from the dictionary to the variable representing boss name
    boss_health = boss_selected[1]                                                                 #Attribute the item from the dictionary to the global variable representing boss health       
    del bosses[name]                                                                               #Remove the "already fought"(generated) bosses from the dictionary
    #print(bosses)      
    if len(bosses) < 4:                                                                            #If "bosses" dictionary is lower than 4(therefore 4 bosses or less left)
        sound("bossclear.wav")                                                                     #Use definition "sound" to play "BOSS DEFEATED" sound
        print("\n BOSS DEFEATED! \n")                                                              #Print string informing the player that the boss has been defeated
        total_hp = 300                                                                             #Restore player's health to the maximum of 300
        sleep(5)                                                                                   #Sleep for 5 seconds
        print("\n __________________________________________ \n")                                  #Divide the old boss section and the new one
        print("\n NEW BOSS APPEARS! \n")                                                           #Print string informing the player that a new boss has to be fought
    while boss_health > 0 and total_hp > 0:                                                        #While the player and boss still have health left, continue with rest of code
    #---------------------------------------------------- HEALTH TO LED TRANSLATION ------------------------------------------------------------------- 
        if (total_hp <= 300 and total_hp > 275):
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
            for x in range(266, 274): led_colour[x] =(255, 0, 17);
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
        
        elif (total_hp <= 275 and total_hp > 250):   
            #--------------------------------------------- H E A L T H   2 3/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(255, 0, 17)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(255, 0, 17)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(255, 0, 17)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(255, 0, 17)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(255, 0, 17)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(255, 0, 17)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(255, 0, 17)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(255, 0, 17)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(255, 0, 17)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(255, 0, 17)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(255, 0, 17)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(255, 0, 17)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(255, 0, 17)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(255, 0, 17)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(255, 0, 17)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(255, 0, 17)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(255, 0, 17)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(255, 0, 17)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(255, 0, 17)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(255, 0, 17)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(255, 0, 17)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(255, 0, 17)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(255, 0, 17)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(255, 0, 17)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(255, 0, 17)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(255, 0, 17)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(255, 0, 17)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(255, 0, 17)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(255, 0, 17)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(255, 0, 17)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(255, 0, 17)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(255, 0, 17)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(255, 0, 17)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(255, 0, 17)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(255, 0, 17)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(255, 0, 17)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(255, 0, 17)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(255, 0, 17)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(255, 0, 17)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(255, 0, 17)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(255, 0, 17)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(255, 0, 17)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()
        
        elif (total_hp <= 250 and total_hp > 225):
            #--------------------------------------------- H E A L T H   2 2/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(255, 0, 17)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(255, 0, 17)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(255, 0, 17)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(255, 0, 17)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(255, 0, 17)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(255, 0, 17)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(255, 0, 17)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(255, 0, 17)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(255, 0, 17)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(255, 0, 17)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(255, 0, 17)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(255, 0, 17)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(255, 0, 17)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(255, 0, 17)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(255, 0, 17)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(255, 0, 17)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(255, 0, 17)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(255, 0, 17)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(255, 0, 17)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(255, 0, 17)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(255, 0, 17)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(255, 0, 17)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(255, 0, 17)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(255, 0, 17)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(255, 0, 17)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(255, 0, 17)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(255, 0, 17)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(255, 0, 17)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(255, 0, 17)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(255, 0, 17)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(255, 0, 17)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()
              
        elif (total_hp <= 225 and total_hp > 200):
            #--------------------------------------------- H E A L T H   2 1/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(255, 0, 17)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(255, 0, 17)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(255, 0, 17)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(255, 0, 17)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(255, 0, 17)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(255, 0, 17)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(255, 0, 17)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(255, 0, 17)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(255, 0, 17)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(255, 0, 17)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(255, 0, 17)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(255, 0, 17)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(255, 0, 17)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(255, 0, 17)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(255, 0, 17)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(255, 0, 17)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(255, 0, 17)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(255, 0, 17)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(255, 0, 17)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(255, 0, 17)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()
                
        elif (total_hp <= 200 and total_hp > 175):           
            #--------------------------------------------- H E A L T H   1 4/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(255, 0, 17)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(255, 0, 17)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(255, 0, 17)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(255, 0, 17)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(255, 0, 17)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(255, 0, 17)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(255, 0, 17)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(255, 0, 17)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(255, 0, 17)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(255, 0, 17)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(255, 0, 17)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(255, 0, 17)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(255, 0, 17)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(255, 0, 17)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(255, 0, 17)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(255, 0, 17)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(255, 0, 17)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(255, 0, 17)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(255, 0, 17)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(255, 0, 17)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)
            
            update()
            
            if len(times) > 1:                                #SYSTEM CHECK: Check list length to see if animation needs to be run
                swipe(0.05)                                   #Run animation
                led_colour = [(255,255,255)]*360              #Reset background
                del times[0]                                  #Delete items from dictionary therefore animation won't run again
            #The statement is required to make sure if the damage taken is so low that we end up in this bracket twice, the animation doesn't run again

            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()
             
        elif (total_hp <= 175 and total_hp > 150):
            #--------------------------------------------- H E A L T H   1 3/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(255, 0, 17);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(255, 0, 17);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(255, 0, 17);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(255, 0, 17);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(255, 0, 17);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(255, 0, 17);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(255, 0, 17);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(255, 0, 17);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(255, 0, 17);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(255, 0, 17);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(255, 0, 17);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(90, 90, 100);           led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(90, 90, 100);           led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(90, 90, 100);           led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(90, 90, 100);           led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(90, 90, 100);           led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(90, 90, 100);           led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(90, 90, 100);           led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(90, 90, 100);           led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(90, 90, 100);            led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(90, 90, 100);            led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(90, 90, 100);            led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(90, 90, 100);            led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(90, 90, 100);            led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(90, 90, 100);            led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(90, 90, 100);            led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(90, 90, 100);            led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(90, 90, 100);            led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(90, 90, 100);            led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(90, 90, 100);            led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(90, 90, 100);            led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()
        
            
        elif (total_hp <= 150 and total_hp > 125):
            #--------------------------------------------- H E A L T H   1 2/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(255, 0, 17);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(90, 90, 100);           led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(255, 0, 17);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(255, 0, 17);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(255, 0, 17);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(255, 0, 17);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(90, 90, 100);           led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(90, 90, 100);           led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(90, 90, 100);           led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(90, 90, 100);           led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(255, 0, 17);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(255, 0, 17);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(255, 0, 17);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(255, 0, 17);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(255, 0, 17);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(255, 0, 17);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(90, 90, 100);           led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(90, 90, 100);           led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(90, 90, 100);           led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(90, 90, 100);           led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(90, 90, 100);           led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(90, 90, 100);           led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(90, 90, 100);           led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(90, 90, 100);           led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(90, 90, 100);           led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(90, 90, 100);           led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(90, 90, 100);           led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(90, 90, 100);           led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(90, 90, 100);           led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(90, 90, 100);           led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(90, 90, 100);            led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(90, 90, 100);            led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(90, 90, 100);            led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(90, 90, 100);            led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(90, 90, 100);            led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(90, 90, 100);            led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(90, 90, 100);            led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(90, 90, 100);            led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(90, 90, 100);            led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(90, 90, 100);            led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(90, 90, 100);            led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(90, 90, 100);            led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()     
            
        elif (total_hp <= 125 and total_hp > 100):
            #--------------------------------------------- H E A L T H   1 1/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(90, 90, 100);           led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(90, 90, 100);           led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(90, 90, 100);           led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(90, 90, 100);           led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(90, 90, 100);           led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(90, 90, 100);           led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(90, 90, 100);           led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(90, 90, 100);           led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(90, 90, 100);           led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(90, 90, 100);           led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(90, 90, 100);           led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(90, 90, 100);           led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(90, 90, 100);           led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(90, 90, 100);           led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(90, 90, 100);           led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(90, 90, 100);           led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(90, 90, 100);           led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(90, 90, 100);           led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(90, 90, 100);           led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(90, 90, 100);           led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(90, 90, 100);           led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(90, 90, 100);           led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(90, 90, 100);           led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(90, 90, 100);           led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(90, 90, 100);           led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(90, 90, 100);           led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(90, 90, 100);           led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(90, 90, 100);           led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(90, 90, 100);           led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(90, 90, 100);           led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(90, 90, 100);            led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(90, 90, 100);            led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(90, 90, 100);            led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(90, 90, 100);            led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(90, 90, 100);            led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(90, 90, 100);            led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(90, 90, 100);            led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(90, 90, 100);            led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(90, 90, 100);            led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(90, 90, 100);            led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(90, 90, 100);            led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(90, 90, 100);            led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

            update()  
        
        elif (total_hp <= 100 and total_hp > 75):         
            #---------------------------------------------- H E A L T H    4/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(90, 90, 100);           led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(90, 90, 100);           led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(90, 90, 100);           led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(90, 90, 100);           led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(90, 90, 100);           led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(90, 90, 100);           led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(90, 90, 100);           led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(90, 90, 100);           led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(90, 90, 100);           led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(90, 90, 100);           led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(90, 90, 100);           led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(90, 90, 100);           led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(90, 90, 100);           led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(90, 90, 100);           led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(90, 90, 100);           led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(90, 90, 100);           led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(90, 90, 100);           led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(90, 90, 100);           led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(90, 90, 100);           led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(90, 90, 100);           led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(90, 90, 100);           led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(90, 90, 100);           led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(255, 0, 17);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(255, 0, 17);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(255, 0, 17);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(255, 0, 17);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(255, 0, 17);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(255, 0, 17);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(255, 0, 17);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(255, 0, 17);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(90, 90, 100);           led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(90, 90, 100);           led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(90, 90, 100);           led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(90, 90, 100);           led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(90, 90, 100);           led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(90, 90, 100);           led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(90, 90, 100);           led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(90, 90, 100);           led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(255, 0, 17);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(255, 0, 17);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(255, 0, 17);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(255, 0, 17);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(255, 0, 17);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(255, 0, 17);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(255, 0, 17);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(255, 0, 17);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(90, 90, 100);            led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(90, 90, 100);            led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(90, 90, 100);            led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(90, 90, 100);            led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(90, 90, 100);            led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(90, 90, 100);            led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(90, 90, 100);            led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(90, 90, 100);            led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(255, 0, 17);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(255, 0, 17);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(255, 0, 17);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(255, 0, 17);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(90, 90, 100);            led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(90, 90, 100);            led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(90, 90, 100);            led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(90, 90, 100);            led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)
            
            update()
            
            if len(times) > 0:                                #SYSTEM CHECK: Check if list has 1 element to see if animation needs to be run
                swipe(0.05)                                   #Run animation
                led_colour = [(255,255,255)]*360              #Reset background
                del times[0]                                  #Delete items from list therefore animation won't run again 
            #The statement is required to make sure if the damage taken is so low that we end up in this bracket twice, the animation doesn't run again
            
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                               #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                 led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(90, 90, 100);           led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(90, 90, 100);           led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                 led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW                               #FIFTH ROW
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                 led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(90, 90, 100);           led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(90, 90, 100);           led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(90, 90, 100);           led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(90, 90, 100);           led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(90, 90, 100);           led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(90, 90, 100);           led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(90, 90, 100);           led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(90, 90, 100);           led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                 led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                               #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                 led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(90, 90, 100);           led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(90, 90, 100);           led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(90, 90, 100);           led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(90, 90, 100);           led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(90, 90, 100);           led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(90, 90, 100);           led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(90, 90, 100);           led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(90, 90, 100);           led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(90, 90, 100);           led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(90, 90, 100);           led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(90, 90, 100);           led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(90, 90, 100);           led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                 led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                               #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                 led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(90, 90, 100);           led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(90, 90, 100);           led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(90, 90, 100);           led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(90, 90, 100);           led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(90, 90, 100);           led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(90, 90, 100);           led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(90, 90, 100);           led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(90, 90, 100);           led_colour[169]=(90, 90, 100)
            led_colour[130]=(255, 0, 17);            led_colour[150]=(90, 90, 100);           led_colour[170]=(90, 90, 100)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(90, 90, 100);           led_colour[171]=(90, 90, 100)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(90, 90, 100);           led_colour[172]=(90, 90, 100)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(90, 90, 100);           led_colour[173]=(90, 90, 100)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(90, 90, 100);           led_colour[174]=(90, 90, 100)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(90, 90, 100);           led_colour[175]=(90, 90, 100)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(90, 90, 100);           led_colour[176]=(90, 90, 100)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(90, 90, 100);           led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                 led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                              #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                  led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(90, 90, 100);            led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(90, 90, 100);            led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(90, 90, 100);            led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(90, 90, 100);            led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(90, 90, 100);            led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(90, 90, 100);            led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(90, 90, 100);            led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(90, 90, 100);            led_colour[109]=(90, 90, 100)
            led_colour[70]=(255, 0, 17);             led_colour[90]=(90, 90, 100);            led_colour[110]=(90, 90, 100)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(90, 90, 100);            led_colour[111]=(90, 90, 100)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(90, 90, 100);            led_colour[112]=(90, 90, 100)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(90, 90, 100);            led_colour[113]=(90, 90, 100)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(90, 90, 100);            led_colour[114]=(90, 90, 100)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(90, 90, 100);            led_colour[115]=(90, 90, 100)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(90, 90, 100);            led_colour[116]=(90, 90, 100)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(90, 90, 100);            led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                  led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                  led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(90, 90, 100);            led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(90, 90, 100);            led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(90, 90, 100);            led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(90, 90, 100);            led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                  led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                  led_colour[52]=(0,0,0)
            led_colour[13]=(255, 0, 17);             led_colour[33]=(90, 90, 100);            led_colour[53]=(90, 90, 100)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(90, 90, 100);            led_colour[54]=(90, 90, 100)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(90, 90, 100);            led_colour[55]=(90, 90, 100)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(90, 90, 100);            led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)
     
            update()  

        elif (total_hp <= 75 and total_hp > 50):
            #---------------------------------------------- H E A L T H    3/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                                #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(90, 90, 100);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(255, 0, 17);            led_colour[330]=(90, 90, 100);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW   
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(90, 90, 100);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(90, 90, 100);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(90, 90, 100);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(90, 90, 100);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(255, 0, 17);            led_colour[270]=(90, 90, 100);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(255, 0, 17);            led_colour[271]=(90, 90, 100);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(255, 0, 17);            led_colour[272]=(90, 90, 100);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(255, 0, 17);            led_colour[273]=(90, 90, 100);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                                #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(90, 90, 100);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(90, 90, 100);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(90, 90, 100);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(90, 90, 100);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(90, 90, 100);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(90, 90, 100);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(255, 0, 17);            led_colour[210]=(90, 90, 100);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(255, 0, 17);            led_colour[211]=(90, 90, 100);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(255, 0, 17);            led_colour[212]=(90, 90, 100);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(255, 0, 17);            led_colour[213]=(90, 90, 100);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(255, 0, 17);            led_colour[214]=(90, 90, 100);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(255, 0, 17);            led_colour[215]=(90, 90, 100);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                                #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(90, 90, 100);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(90, 90, 100);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(90, 90, 100);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(90, 90, 100);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(90, 90, 100);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(90, 90, 100);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(90, 90, 100);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(90, 90, 100);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(90, 90, 100);           led_colour[150]=(90, 90, 100);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(90, 90, 100);           led_colour[151]=(90, 90, 100);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(90, 90, 100);           led_colour[152]=(90, 90, 100);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(90, 90, 100);           led_colour[153]=(90, 90, 100);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(90, 90, 100);           led_colour[154]=(90, 90, 100);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(90, 90, 100);           led_colour[155]=(90, 90, 100);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(90, 90, 100);           led_colour[156]=(90, 90, 100);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(90, 90, 100);           led_colour[157]=(90, 90, 100);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                               #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(90, 90, 100);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(90, 90, 100);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(90, 90, 100);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(90, 90, 100);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(90, 90, 100);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(90, 90, 100);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(90, 90, 100);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(90, 90, 100);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(90, 90, 100);            led_colour[90]=(90, 90, 100);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(90, 90, 100);            led_colour[91]=(90, 90, 100);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(90, 90, 100);            led_colour[92]=(90, 90, 100);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(90, 90, 100);            led_colour[93]=(90, 90, 100);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(90, 90, 100);            led_colour[94]=(90, 90, 100);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(90, 90, 100);            led_colour[95]=(90, 90, 100);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(90, 90, 100);            led_colour[96]=(90, 90, 100);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(90, 90, 100);            led_colour[97]=(90, 90, 100);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(90, 90, 100);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(90, 90, 100);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(90, 90, 100);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(90, 90, 100);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
            led_colour[13]=(90, 90, 100);            led_colour[33]=(90, 90, 100);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(90, 90, 100);            led_colour[34]=(90, 90, 100);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(90, 90, 100);            led_colour[35]=(90, 90, 100);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(90, 90, 100);            led_colour[36]=(90, 90, 100);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)

            update()
        
        elif (total_hp <= 50 and total_hp > 25):
            #---------------------------------------------- H E A L T H    2/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                                #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
            led_colour[309]=(255, 0, 17);            led_colour[329]=(90, 90, 100);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(90, 90, 100);           led_colour[330]=(90, 90, 100);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW   
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
            led_colour[246]=(255, 0, 17);            led_colour[266]=(90, 90, 100);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(255, 0, 17);            led_colour[267]=(90, 90, 100);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(255, 0, 17);            led_colour[268]=(90, 90, 100);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(255, 0, 17);            led_colour[269]=(90, 90, 100);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(90, 90, 100);           led_colour[270]=(90, 90, 100);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(90, 90, 100);           led_colour[271]=(90, 90, 100);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(90, 90, 100);           led_colour[272]=(90, 90, 100);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(90, 90, 100);           led_colour[273]=(90, 90, 100);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                                #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
            led_colour[184]=(255, 0, 17);            led_colour[204]=(90, 90, 100);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(255, 0, 17);            led_colour[205]=(90, 90, 100);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(255, 0, 17);            led_colour[206]=(90, 90, 100);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(255, 0, 17);            led_colour[207]=(90, 90, 100);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(255, 0, 17);            led_colour[208]=(90, 90, 100);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(255, 0, 17);            led_colour[209]=(90, 90, 100);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(90, 90, 100);           led_colour[210]=(90, 90, 100);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(90, 90, 100);           led_colour[211]=(90, 90, 100);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(90, 90, 100);           led_colour[212]=(90, 90, 100);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(90, 90, 100);           led_colour[213]=(90, 90, 100);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(90, 90, 100);           led_colour[214]=(90, 90, 100);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(90, 90, 100);           led_colour[215]=(90, 90, 100);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                                #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(90, 90, 100);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(90, 90, 100);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(90, 90, 100);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(90, 90, 100);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(90, 90, 100);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(90, 90, 100);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(90, 90, 100);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(90, 90, 100);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(90, 90, 100);           led_colour[150]=(90, 90, 100);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(90, 90, 100);           led_colour[151]=(90, 90, 100);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(90, 90, 100);           led_colour[152]=(90, 90, 100);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(90, 90, 100);           led_colour[153]=(90, 90, 100);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(90, 90, 100);           led_colour[154]=(90, 90, 100);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(90, 90, 100);           led_colour[155]=(90, 90, 100);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(90, 90, 100);           led_colour[156]=(90, 90, 100);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(90, 90, 100);           led_colour[157]=(90, 90, 100);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                               #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(90, 90, 100);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(90, 90, 100);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(90, 90, 100);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(90, 90, 100);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(90, 90, 100);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(90, 90, 100);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(90, 90, 100);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(90, 90, 100);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(90, 90, 100);            led_colour[90]=(90, 90, 100);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(90, 90, 100);            led_colour[91]=(90, 90, 100);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(90, 90, 100);            led_colour[92]=(90, 90, 100);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(90, 90, 100);            led_colour[93]=(90, 90, 100);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(90, 90, 100);            led_colour[94]=(90, 90, 100);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(90, 90, 100);            led_colour[95]=(90, 90, 100);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(90, 90, 100);            led_colour[96]=(90, 90, 100);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(90, 90, 100);            led_colour[97]=(90, 90, 100);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(90, 90, 100);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(90, 90, 100);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(90, 90, 100);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(90, 90, 100);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
            led_colour[13]=(90, 90, 100);            led_colour[33]=(90, 90, 100);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(90, 90, 100);            led_colour[34]=(90, 90, 100);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(90, 90, 100);            led_colour[35]=(90, 90, 100);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(90, 90, 100);            led_colour[36]=(90, 90, 100);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)

            update()

        elif (total_hp <= 25 and total_hp > 0):
            #---------------------------------------------- H E A L T H    1/4TH ----------------------------------------------------------------------
            #--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
            #SIXTH ROW                               #SIXTH ROW                                #SIXTH ROW
            led_colour[308]=(0,0,0);                 led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
            led_colour[309]=(90, 90, 100);           led_colour[329]=(90, 90, 100);            led_colour[349]=(90, 90, 100)
            led_colour[310]=(90, 90, 100);           led_colour[330]=(90, 90, 100);            led_colour[350]=(90, 90, 100)
            led_colour[311]=(0,0,0);                 led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
            #FIFTH ROW                               #FIFTH ROW   
            led_colour[245]=(0,0,0);                 led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
            led_colour[246]=(90, 90, 100);           led_colour[266]=(90, 90, 100);            led_colour[286]=(90, 90, 100)
            led_colour[247]=(90, 90, 100);           led_colour[267]=(90, 90, 100);            led_colour[287]=(90, 90, 100)
            led_colour[248]=(90, 90, 100);           led_colour[268]=(90, 90, 100);            led_colour[288]=(90, 90, 100)
            led_colour[249]=(90, 90, 100);           led_colour[269]=(90, 90, 100);            led_colour[289]=(90, 90, 100)
            led_colour[250]=(90, 90, 100);           led_colour[270]=(90, 90, 100);            led_colour[290]=(90, 90, 100)
            led_colour[251]=(90, 90, 100);           led_colour[271]=(90, 90, 100);            led_colour[291]=(90, 90, 100)
            led_colour[252]=(90, 90, 100);           led_colour[272]=(90, 90, 100);            led_colour[292]=(90, 90, 100)
            led_colour[253]=(90, 90, 100);           led_colour[273]=(90, 90, 100);            led_colour[293]=(90, 90, 100)
            led_colour[254]=(0,0,0);                 led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
            #FORTH ROW                               #FORTH ROW                                #FORTH ROW
            led_colour[183]=(0,0,0);                 led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
            led_colour[184]=(90, 90, 100);           led_colour[204]=(90, 90, 100);            led_colour[224]=(90, 90, 100)
            led_colour[185]=(90, 90, 100);           led_colour[205]=(90, 90, 100);            led_colour[225]=(90, 90, 100)
            led_colour[186]=(90, 90, 100);           led_colour[206]=(90, 90, 100);            led_colour[226]=(90, 90, 100)
            led_colour[187]=(90, 90, 100);           led_colour[207]=(90, 90, 100);            led_colour[227]=(90, 90, 100)
            led_colour[188]=(90, 90, 100);           led_colour[208]=(90, 90, 100);            led_colour[228]=(90, 90, 100)
            led_colour[189]=(90, 90, 100);           led_colour[209]=(90, 90, 100);            led_colour[229]=(90, 90, 100)
            led_colour[190]=(90, 90, 100);           led_colour[210]=(90, 90, 100);            led_colour[230]=(90, 90, 100)
            led_colour[191]=(90, 90, 100);           led_colour[211]=(90, 90, 100);            led_colour[231]=(90, 90, 100)
            led_colour[192]=(90, 90, 100);           led_colour[212]=(90, 90, 100);            led_colour[232]=(90, 90, 100)
            led_colour[193]=(90, 90, 100);           led_colour[213]=(90, 90, 100);            led_colour[233]=(90, 90, 100)
            led_colour[194]=(90, 90, 100);           led_colour[214]=(90, 90, 100);            led_colour[234]=(90, 90, 100)
            led_colour[195]=(90, 90, 100);           led_colour[215]=(90, 90, 100);            led_colour[235]=(90, 90, 100)
            led_colour[196]=(0,0,0);                 led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
            #THIRD ROW                               #THIRD ROW                                #THIRD ROW
            led_colour[121]=(0,0,0);                 led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
            led_colour[122]=(255, 0, 17);            led_colour[142]=(90, 90, 100);            led_colour[162]=(90, 90, 100)
            led_colour[123]=(255, 0, 17);            led_colour[143]=(90, 90, 100);            led_colour[163]=(90, 90, 100)
            led_colour[124]=(255, 0, 17);            led_colour[144]=(90, 90, 100);            led_colour[164]=(90, 90, 100)
            led_colour[125]=(255, 0, 17);            led_colour[145]=(90, 90, 100);            led_colour[165]=(90, 90, 100)
            led_colour[126]=(255, 0, 17);            led_colour[146]=(90, 90, 100);            led_colour[166]=(90, 90, 100)
            led_colour[127]=(255, 0, 17);            led_colour[147]=(90, 90, 100);            led_colour[167]=(90, 90, 100)
            led_colour[128]=(255, 0, 17);            led_colour[148]=(90, 90, 100);            led_colour[168]=(90, 90, 100)
            led_colour[129]=(255, 0, 17);            led_colour[149]=(90, 90, 100);            led_colour[169]=(90, 90, 100)
            led_colour[130]=(90, 90, 100);           led_colour[150]=(90, 90, 100);            led_colour[170]=(90, 90, 100)
            led_colour[131]=(90, 90, 100);           led_colour[151]=(90, 90, 100);            led_colour[171]=(90, 90, 100)
            led_colour[132]=(90, 90, 100);           led_colour[152]=(90, 90, 100);            led_colour[172]=(90, 90, 100)
            led_colour[133]=(90, 90, 100);           led_colour[153]=(90, 90, 100);            led_colour[173]=(90, 90, 100)
            led_colour[134]=(90, 90, 100);           led_colour[154]=(90, 90, 100);            led_colour[174]=(90, 90, 100)
            led_colour[135]=(90, 90, 100);           led_colour[155]=(90, 90, 100);            led_colour[175]=(90, 90, 100)
            led_colour[136]=(90, 90, 100);           led_colour[156]=(90, 90, 100);            led_colour[176]=(90, 90, 100)
            led_colour[137]=(90, 90, 100);           led_colour[157]=(90, 90, 100);            led_colour[177]=(90, 90, 100)
            led_colour[138]=(0,0,0);                 led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
            #SECOND ROW                              #SECOND ROW                               #SECOND ROW
            led_colour[61]=(0,0,0);                  led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
            led_colour[62]=(255, 0, 17);             led_colour[82]=(90, 90, 100);             led_colour[102]=(90, 90, 100)
            led_colour[63]=(255, 0, 17);             led_colour[83]=(90, 90, 100);             led_colour[103]=(90, 90, 100)
            led_colour[64]=(255, 0, 17);             led_colour[84]=(90, 90, 100);             led_colour[104]=(90, 90, 100)
            led_colour[65]=(255, 0, 17);             led_colour[85]=(90, 90, 100);             led_colour[105]=(90, 90, 100)
            led_colour[66]=(255, 0, 17);             led_colour[86]=(90, 90, 100);             led_colour[106]=(90, 90, 100)
            led_colour[67]=(255, 0, 17);             led_colour[87]=(90, 90, 100);             led_colour[107]=(90, 90, 100)
            led_colour[68]=(255, 0, 17);             led_colour[88]=(90, 90, 100);             led_colour[108]=(90, 90, 100)
            led_colour[69]=(255, 0, 17);             led_colour[89]=(90, 90, 100);             led_colour[109]=(90, 90, 100)
            led_colour[70]=(90, 90, 100);            led_colour[90]=(90, 90, 100);             led_colour[110]=(90, 90, 100)
            led_colour[71]=(90, 90, 100);            led_colour[91]=(90, 90, 100);             led_colour[111]=(90, 90, 100)
            led_colour[72]=(90, 90, 100);            led_colour[92]=(90, 90, 100);             led_colour[112]=(90, 90, 100)
            led_colour[73]=(90, 90, 100);            led_colour[93]=(90, 90, 100);             led_colour[113]=(90, 90, 100)
            led_colour[74]=(90, 90, 100);            led_colour[94]=(90, 90, 100);             led_colour[114]=(90, 90, 100)
            led_colour[75]=(90, 90, 100);            led_colour[95]=(90, 90, 100);             led_colour[115]=(90, 90, 100)
            led_colour[76]=(90, 90, 100);            led_colour[96]=(90, 90, 100);             led_colour[116]=(90, 90, 100)
            led_colour[77]=(90, 90, 100);            led_colour[97]=(90, 90, 100);             led_colour[117]=(90, 90, 100)
            led_colour[78]=(0,0,0);                  led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
            #FIRST ROW - FIRST HALF                  #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
            led_colour[2]=(0,0,0);                   led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
            led_colour[3]=(255, 0, 17);              led_colour[23]=(90, 90, 100);             led_colour[43]=(90, 90, 100)
            led_colour[4]=(255, 0, 17);              led_colour[24]=(90, 90, 100);             led_colour[44]=(90, 90, 100)
            led_colour[5]=(255, 0, 17);              led_colour[25]=(90, 90, 100);             led_colour[45]=(90, 90, 100)
            led_colour[6]=(255, 0, 17);              led_colour[26]=(90, 90, 100);             led_colour[46]=(90, 90, 100)
            led_colour[7]=(0,0,0);                   led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
            #FIRST ROW - SECOND HALF                 #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
            led_colour[12]=(0,0,0);                  led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
            led_colour[13]=(90, 90, 100);            led_colour[33]=(90, 90, 100);             led_colour[53]=(90, 90, 100)
            led_colour[14]=(90, 90, 100);            led_colour[34]=(90, 90, 100);             led_colour[54]=(90, 90, 100)
            led_colour[15]=(90, 90, 100);            led_colour[35]=(90, 90, 100);             led_colour[55]=(90, 90, 100)
            led_colour[16]=(90, 90, 100);            led_colour[36]=(90, 90, 100);             led_colour[56]=(90, 90, 100)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)

            update()

#-------------------------------------------------------------END OF HEALTH TRANSLATION------------------------------------------------------------
                 
        #BOSS INTERFACE                                                       
        print("\n BOSS: ", name)                                                                   #Display boss name, acquired after random selection from dictionary
        print("\n HEALTH:", boss_health)                                                           #Display boss health, acquired after random selection from dictionary
        #print("\n USER HP:", total_hp)                                                            #DEBUGGING ONLY
         
        #WEAPONS MENU
        print("  __________________________________________")
        print(" |                                          |") 
        print(" |              Select Weapon:              |")
        print(" |                                          |")
        print(" | 1) The Master Sword    -  60 DMG -", weapons.get("THE MASTER SWORD"), "DUR |")
        print(" | 2) Boomerang           -   8 DMG -", weapons.get("BOOMERANG"), "DUR |")                
        print(" | 3) Knight Broadsword   -  26 DMG -", weapons.get("KNIGHT BROADSWORD"), "DUR |")
        print(" | 4) Zora Sword          -  15 DMG -", weapons.get("ZORA SWORD"), "DUR |")
        print(" | 5) Torch               -   2 DMG -", weapons.get("TORCH"), "DUR |")
        print(" | 6) Moonlight Scimitar  -  25 DMG -", weapons.get("MOONLIGHT SCIMITAR"), "DUR |")
        print(" | 7) Ancient Sword       -  40 DMG -", weapons.get("ANCIENT SWORD"), "DUR |")
        print(" | 8) Flameblade          -  24 DMG -", weapons.get("FLAMEBLADE"), "DUR |")
        print(" | 9) Guardian Sword      -  20 DMG -", weapons.get("GUARDIAN SWORD"), "DUR |")
        print(" | 10) Ice Rod            -   5 DMG -", weapons.get("ICE ROD"), "DUR |")
        print(" | 11) Korok Leaf         -   1 DMG -", weapons.get("KOROK LEAF"), "DUR |")
        print(" | 12) Boulder Breaker    -  60 DMG -", weapons.get("BOULDER BREAKER"), "DUR |")
        print(" |                                          |")
        print(" |__________________________________________|")
        raw_menu = input("\n Your choice of weapon: ")                                             #Print string and wait for user input

        #WEAPONS SELECTION
        if raw_menu.isdigit():                                                                     #INPUT CHECK: If the input is a digit continue with the choices:
            menu = int(raw_menu)                                                                   #Create new variable and store integer value of input
            #FIRST WEAPON
            if (menu == 1):                                                                        #If input is 1:
                durability("THE MASTER SWORD", 60)                                                 #Then use definition "durability" with values for the specific input
            #SECOND WEAPON
            elif (menu == 2):                                                                      #If input is 2:
                durability("BOOMERANG", 8)                                                         #Then use definition "durability" with values for the specific input
            #THIRD WEAPON
            elif (menu == 3):                                                                      #If input is 3:
                durability("KNIGHT BROADSWORD", 26)                                                #Then use definition "durability" with values for the specific input
            #FORTH WEAPON
            elif (menu == 4):                                                                      #If input is 4:
                durability("ZORA SWORD", 15)                                                       #Then use definition "durability" with values for the specific input
            #FIFTH WEAPON
            elif (menu == 5):                                                                      #If input is 5:
                durability("TORCH", 2)                                                             #Then use definition "durability" with values for the specific input
            #SIXTH WEAPON    
            elif (menu == 6):                                                                      #If input is 6:
                durability("MOONLIGHT SCIMITAR", 25)                                               #Then use definition "durability" with values for the specific input
            #SEVENTH WEAPON    
            elif (menu == 7):                                                                      #If input is 7:
                durability("ANCIENT SWORD", 40)                                                    #Then use definition "durability" with values for the specific input
            #EIGTH WEAPON    
            elif (menu == 8):                                                                      #If input is 8:
                durability("FLAMEBLADE", 24)                                                       #Then use definition "durability" with values for the specific input
            #NINTH WEAPON    
            elif (menu == 9):                                                                      #If input is 9:
                durability("GUARDIAN SWORD", 20)                                                   #Then use definition "durability" with values for the specific input
            #TENTH WEAPON    
            elif (menu == 10):                                                                     #If input is 10:
                durability("ICE ROD", 5)                                                           #Then use definition "durability" with values for the specific input
            #ELEVENTH WEAPON    
            elif (menu == 11):                                                                     #If input is 11:
                durability("KOROK LEAF", 1)                                                        #Then use definition "durability" with values for the specific input
            #TWELFTH WEAPON    
            elif (menu == 12):                                                                     #If input is 12:
                durability("BOULDER BREAKER", 60)                                                  #Then use definition "durability" with values for the specific input
            #SECRET WEAPON    
            elif (menu == 93532):                                                                  #Input required to activate secret weapon is the word "ZELDA" on a keypad
                print("\n YOU HAVE UNLOCKED ZELDA'S SECRET WEAPON - THE BOW OF LIGHT \n")
                durability("THE BOW OF LIGHT", 100)                                                #Use definition "durability" with values for the specific input
                damage(250, 250, 85, 255, 0, 17)                                                   #Activate flashing animation with selected RGB values for 2 different colours(a,b,c, d,e,f)
                secret(250, 250, 85)                                                               #Use definition "secret" to change background to yellow colour
            #OUT OF SLOT CHOICE        
            elif (menu > 12):                                                                      #INPUT CHECK: If input is higher than 12, then there's no weapon available
                print("\n No weapon available in that slot! Please choose another weapon! \n")
        else:                                                                                      #INPUT CHECK: If input is a character/string and not a digit, reset weapon choice
            print("\n You have typed a character, please insert a number for weapon selection! \n")
            
if total_hp <= 0:                                                                                  #If player's health is equal or lower to 0 then:
    print("\n GAME OVER! YOU LOST! \n")                                                            #Print "GAME OVER" string
    sound("gameover.wav")                                                                          #Use definition "sound" to play "GAME OVER" sound
    heartloss(1, 60)                                                                               #Run "GAME OVER" animation called "heartloss"

"""
01001001 00100000 01110111 01101111 01110010 01101011 01100101 01100100 00100000 00110010 00110011 00100000 01101000 01101111 01110101 01110010 01110011 00100000 
01101111 01101110 00100000 01110100 01101000 01101001 01110011 00100000 01110000 01110010 01101111 01101010 01100101 01100011 01110100 00100000 00101000 11100000
10110010 10100101 11101111 10111001 10001111 11100000 10110010 10100101 00101001 00001010 01001001 00100000 01101000 01100001 01100100 00100000 01100001 00100000
01101100 01101111 01110100 00100000 01101111 01100110 00100000 01100110 01110101 01101110 00100000 01110100 01101000 01101111 01110101 01100111 01101000

                                                                                                                                                        - Ciprian
"""  