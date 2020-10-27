#LIBRARIES
import opc
import random
from time import sleep
client = opc.Client('localhost:7890')

#DEFINITIONS
def update():
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

def weapon(dmg, wpn):
    global remaining_boss_health; global boss_health; global total_hp; global remaining_hp
    attack = random.randint(5, 25)    
    
    remaining_boss_health = boss_health - dmg; boss_health = remaining_boss_health    
    remaining_hp = total_hp - attack; total_hp = remaining_hp
      
    print("\n You used", wpn, "and dealt", dmg, "damage! \n")
    print("\n The enemy dealt", attack, "damage! \n")
    
#BACKGROUND
led_colour = [(255,255,255)]*360

#BOSSES DICTIONARY
bosses = { "GANNON" : 400, "NAYDRA" : 300, "MORPHA" : 200, "GANONDORF" : 500, "TWINROVA" :  250 }

#VARIABLES FOR HEALTH SYSTEM
boss_health = int()
remaining_boss_health = int()
total_hp = 300
remaining_hp = int()

#LOGO
logo = """               
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
"""; print(logo)

#MAIN CODE      
while total_hp > 0 and boss_health <= 0:
    #END GAME
    if len(bosses) == 0 and boss_health <= 0:
        print("\n Congratulations, you completed the game! \n")
        break
       
    #BOSS SELECTION  
    boss_selected = random.choice(list(bosses.items()))                       #Select a random "boss"(key) from the defined dictionary
    name = boss_selected[0]                                                   #Attribute the 1st value from the dictionary to the variable representing boss name
    boss_health = boss_selected[1]                                            #Attribute the 2nd value from the dictionary to the global variable representing boss health       
    del bosses[name]                                                          #Remove the "already fought"(generated) bosses from the dictionary
    #print(bosses)                                                            #DEBUGGING ONLY
       
    while boss_health > 0 and total_hp > 0:  
    #---------------------------------------------------- HEALTH TO LED TRANSLATION ------------------------------------------------------------------- 
        if (total_hp <= 300 and total_hp > 275):
            #--------------------------------------------- H E A L T H    F U L L  --------------------------------------------------------------------
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
            led_colour[130]=(255, 0, 17);            led_colour[150]=(255, 0, 17);            led_colour[170]=(255, 0, 17)
            led_colour[131]=(255, 0, 17);            led_colour[151]=(255, 0, 17);            led_colour[171]=(255, 0, 17)
            led_colour[132]=(255, 0, 17);            led_colour[152]=(255, 0, 17);            led_colour[172]=(255, 0, 17)
            led_colour[133]=(255, 0, 17);            led_colour[153]=(255, 0, 17);            led_colour[173]=(255, 0, 17)
            led_colour[134]=(255, 0, 17);            led_colour[154]=(255, 0, 17);            led_colour[174]=(255, 0, 17)
            led_colour[135]=(255, 0, 17);            led_colour[155]=(255, 0, 17);            led_colour[175]=(255, 0, 17)
            led_colour[136]=(255, 0, 17);            led_colour[156]=(255, 0, 17);            led_colour[176]=(255, 0, 17)
            led_colour[137]=(255, 0, 17);            led_colour[157]=(255, 0, 17);            led_colour[177]=(255, 0, 17)
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
            led_colour[70]=(255, 0, 17);             led_colour[90]=(255, 0, 17);             led_colour[110]=(255, 0, 17)
            led_colour[71]=(255, 0, 17);             led_colour[91]=(255, 0, 17);             led_colour[111]=(255, 0, 17)
            led_colour[72]=(255, 0, 17);             led_colour[92]=(255, 0, 17);             led_colour[112]=(255, 0, 17)
            led_colour[73]=(255, 0, 17);             led_colour[93]=(255, 0, 17);             led_colour[113]=(255, 0, 17)
            led_colour[74]=(255, 0, 17);             led_colour[94]=(255, 0, 17);             led_colour[114]=(255, 0, 17)
            led_colour[75]=(255, 0, 17);             led_colour[95]=(255, 0, 17);             led_colour[115]=(255, 0, 17)
            led_colour[76]=(255, 0, 17);             led_colour[96]=(255, 0, 17);             led_colour[116]=(255, 0, 17)
            led_colour[77]=(255, 0, 17);             led_colour[97]=(255, 0, 17);             led_colour[117]=(255, 0, 17)
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
            led_colour[13]=(255, 0, 17);             led_colour[33]=(255, 0, 17);             led_colour[53]=(255, 0, 17)
            led_colour[14]=(255, 0, 17);             led_colour[34]=(255, 0, 17);             led_colour[54]=(255, 0, 17)
            led_colour[15]=(255, 0, 17);             led_colour[35]=(255, 0, 17);             led_colour[55]=(255, 0, 17)
            led_colour[16]=(255, 0, 17);             led_colour[36]=(255, 0, 17);             led_colour[56]=(255, 0, 17)
            led_colour[17]=(0,0,0);                  led_colour[37]=(0,0,0);                  led_colour[57]=(0,0,0)

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
        print("\n BOSS: ", name)
        print("\n HEALTH:", boss_health) 
        #print("\n USER HP:", total_hp)                                       #DEBUGGING ONLY
         
        #WEAPONS MENU
        weapons_menu = """
         ____________________________________
        |                                    |
        |           Select weapon:           |
        |                                    |
        |  1) The Master Sword    -  60 DMG  |
        |  2) Boomerang           -   8 DMG  |
        |  3) Knight Broadsword   -  26 DMG  |
        |  4) Zora Sword          -  15 DMG  |
        |  5) Torch               -   2 DMG  |
        |  6) Moonlight Scimitar  -  25 DMG  |
        |  7) Ancient Sword       -  40 DMG  |
        |  8) Flameblade          -  24 DMG  |
        |  9) Guardian Sword      -  20 DMG  |
        |  10) Ice Rod            -   5 DMG  |
        |  11) Korok Leaf         -   1 DMG  |
        |  12) Boulder Breaker    -  60 DMG  |        
        |____________________________________|
        """ 
        print(weapons_menu)
        raw_menu = input("\n Your choice of weapon: ")
        menu = int(raw_menu)

        #FIRST WEAPON
        if (menu == 1):
           weapon(60, "THE MASTER SWORD")
        #SECOND WEAPON
        elif (menu == 2):
            weapon(8, "BOOMERANG")
        #THIRD WEAPON
        elif (menu == 3):
            weapon(26, "KNIGHT BROADSWORD")
        #FORTH WEAPON
        elif (menu == 4):
            weapon(15, "ZORA SWORD")
        #FIFTH WEAPON
        elif (menu == 5):
            weapon(2, "TORCH")
        #SIXTH WEAPON    
        elif (menu == 6):
            weapon(25, "MOONLIGHT SCIMITAR")
        #SEVENTH WEAPON    
        elif (menu == 7):
            weapon(40, "ANCIENT SWORD")
        #EIGTH WEAPON    
        elif (menu == 8):
            weapon(24, "FLAMEBLADE")
        #NINTH WEAPON    
        elif (menu == 9):
            weapon(20, "GUARDIAN SWORD")
        #TENTH WEAPON    
        elif (menu == 10):
            weapon(5, "ICE ROD")
        #ELEVENTH WEAPON    
        elif (menu == 11):
            weapon(1, "KOROK LEAF")
        #TWELFTH WEAPON    
        elif (menu == 12):
            weapon(60, "BOULDER BREAKER")
        #SECRET WEAPON    
        elif (menu == 93532):
            print("\n YOU HAVE UNLOCKED ZELDA'S SECRET WEAPON - THE BOW OF LIGHT \n")
            weapon(100, "THE BOW OF LIGHT")   
        #OUT OF SLOT CHOICE        
        elif (menu > 12):
            print("\n No weapon available in that slot! \n")

#---------------------------------- H E A L T H    F U L L Y    D E P L E T E D -----------------------------------------------------------
#--- F I R S T    H E A R T ----------------- S E C O N D    H E A R T ----------------- T H I R D    H E A R T ---------------------------    
#SIXTH ROW                                #SIXTH ROW                                #SIXTH ROW
led_colour[308]=(0,0,0);                  led_colour[328]=(0,0,0);                  led_colour[348]=(0,0,0)
led_colour[309]=(90, 90, 100);            led_colour[329]=(90, 90, 100);            led_colour[349]=(90, 90, 100)
led_colour[310]=(90, 90, 100);            led_colour[330]=(90, 90, 100);            led_colour[350]=(90, 90, 100)
led_colour[311]=(0,0,0);                  led_colour[331]=(0,0,0);                  led_colour[351]=(0,0,0)
#FIFTH ROW                                #FIFTH ROW   
led_colour[245]=(0,0,0);                  led_colour[265]=(0,0,0);                  led_colour[285]=(0,0,0)
led_colour[246]=(90, 90, 100);            led_colour[266]=(90, 90, 100);            led_colour[286]=(90, 90, 100)
led_colour[247]=(90, 90, 100);            led_colour[267]=(90, 90, 100);            led_colour[287]=(90, 90, 100)
led_colour[248]=(90, 90, 100);            led_colour[268]=(90, 90, 100);            led_colour[288]=(90, 90, 100)
led_colour[249]=(90, 90, 100);            led_colour[269]=(90, 90, 100);            led_colour[289]=(90, 90, 100)
led_colour[250]=(90, 90, 100);            led_colour[270]=(90, 90, 100);            led_colour[290]=(90, 90, 100)
led_colour[251]=(90, 90, 100);            led_colour[271]=(90, 90, 100);            led_colour[291]=(90, 90, 100)
led_colour[252]=(90, 90, 100);            led_colour[272]=(90, 90, 100);            led_colour[292]=(90, 90, 100)
led_colour[253]=(90, 90, 100);            led_colour[273]=(90, 90, 100);            led_colour[293]=(90, 90, 100)
led_colour[254]=(0,0,0);                  led_colour[274]=(0,0,0);                  led_colour[294]=(0,0,0)
#FORTH ROW                                #FORTH ROW                                #FORTH ROW
led_colour[183]=(0,0,0);                  led_colour[203]=(0,0,0);                  led_colour[223]=(0,0,0)
led_colour[184]=(90, 90, 100);            led_colour[204]=(90, 90, 100);            led_colour[224]=(90, 90, 100)
led_colour[185]=(90, 90, 100);            led_colour[205]=(90, 90, 100);            led_colour[225]=(90, 90, 100)
led_colour[186]=(90, 90, 100);            led_colour[206]=(90, 90, 100);            led_colour[226]=(90, 90, 100)
led_colour[187]=(90, 90, 100);            led_colour[207]=(90, 90, 100);            led_colour[227]=(90, 90, 100)
led_colour[188]=(90, 90, 100);            led_colour[208]=(90, 90, 100);            led_colour[228]=(90, 90, 100)
led_colour[189]=(90, 90, 100);            led_colour[209]=(90, 90, 100);            led_colour[229]=(90, 90, 100)
led_colour[190]=(90, 90, 100);            led_colour[210]=(90, 90, 100);            led_colour[230]=(90, 90, 100)
led_colour[191]=(90, 90, 100);            led_colour[211]=(90, 90, 100);            led_colour[231]=(90, 90, 100)
led_colour[192]=(90, 90, 100);            led_colour[212]=(90, 90, 100);            led_colour[232]=(90, 90, 100)
led_colour[193]=(90, 90, 100);            led_colour[213]=(90, 90, 100);            led_colour[233]=(90, 90, 100)
led_colour[194]=(90, 90, 100);            led_colour[214]=(90, 90, 100);            led_colour[234]=(90, 90, 100)
led_colour[195]=(90, 90, 100);            led_colour[215]=(90, 90, 100);            led_colour[235]=(90, 90, 100)
led_colour[196]=(0,0,0);                  led_colour[216]=(0,0,0);                  led_colour[236]=(0,0,0)
#THIRD ROW                                #THIRD ROW                                #THIRD ROW
led_colour[121]=(0,0,0);                  led_colour[141]=(0,0,0);                  led_colour[161]=(0,0,0)
led_colour[122]=(90, 90, 100);            led_colour[142]=(90, 90, 100);            led_colour[162]=(90, 90, 100)
led_colour[123]=(90, 90, 100);            led_colour[143]=(90, 90, 100);            led_colour[163]=(90, 90, 100)
led_colour[124]=(90, 90, 100);            led_colour[144]=(90, 90, 100);            led_colour[164]=(90, 90, 100)
led_colour[125]=(90, 90, 100);            led_colour[145]=(90, 90, 100);            led_colour[165]=(90, 90, 100)
led_colour[126]=(90, 90, 100);            led_colour[146]=(90, 90, 100);            led_colour[166]=(90, 90, 100)
led_colour[127]=(90, 90, 100);            led_colour[147]=(90, 90, 100);            led_colour[167]=(90, 90, 100)
led_colour[128]=(90, 90, 100);            led_colour[148]=(90, 90, 100);            led_colour[168]=(90, 90, 100)
led_colour[129]=(90, 90, 100);            led_colour[149]=(90, 90, 100);            led_colour[169]=(90, 90, 100)
led_colour[130]=(90, 90, 100);            led_colour[150]=(90, 90, 100);            led_colour[170]=(90, 90, 100)
led_colour[131]=(90, 90, 100);            led_colour[151]=(90, 90, 100);            led_colour[171]=(90, 90, 100)
led_colour[132]=(90, 90, 100);            led_colour[152]=(90, 90, 100);            led_colour[172]=(90, 90, 100)
led_colour[133]=(90, 90, 100);            led_colour[153]=(90, 90, 100);            led_colour[173]=(90, 90, 100)
led_colour[134]=(90, 90, 100);            led_colour[154]=(90, 90, 100);            led_colour[174]=(90, 90, 100)
led_colour[135]=(90, 90, 100);            led_colour[155]=(90, 90, 100);            led_colour[175]=(90, 90, 100)
led_colour[136]=(90, 90, 100);            led_colour[156]=(90, 90, 100);            led_colour[176]=(90, 90, 100)
led_colour[137]=(90, 90, 100);            led_colour[157]=(90, 90, 100);            led_colour[177]=(90, 90, 100)
led_colour[138]=(0,0,0);                  led_colour[158]=(0,0,0);                  led_colour[178]=(0,0,0)
#SECOND ROW                               #SECOND ROW                               #SECOND ROW
led_colour[61]=(0,0,0);                   led_colour[81]=(0,0,0);                   led_colour[101]=(0,0,0)
led_colour[62]=(90, 90, 100);             led_colour[82]=(90, 90, 100);             led_colour[102]=(90, 90, 100)
led_colour[63]=(90, 90, 100);             led_colour[83]=(90, 90, 100);             led_colour[103]=(90, 90, 100)
led_colour[64]=(90, 90, 100);             led_colour[84]=(90, 90, 100);             led_colour[104]=(90, 90, 100)
led_colour[65]=(90, 90, 100);             led_colour[85]=(90, 90, 100);             led_colour[105]=(90, 90, 100)
led_colour[66]=(90, 90, 100);             led_colour[86]=(90, 90, 100);             led_colour[106]=(90, 90, 100)
led_colour[67]=(90, 90, 100);             led_colour[87]=(90, 90, 100);             led_colour[107]=(90, 90, 100)
led_colour[68]=(90, 90, 100);             led_colour[88]=(90, 90, 100);             led_colour[108]=(90, 90, 100)
led_colour[69]=(90, 90, 100);             led_colour[89]=(90, 90, 100);             led_colour[109]=(90, 90, 100)
led_colour[70]=(90, 90, 100);             led_colour[90]=(90, 90, 100);             led_colour[110]=(90, 90, 100)
led_colour[71]=(90, 90, 100);             led_colour[91]=(90, 90, 100);             led_colour[111]=(90, 90, 100)
led_colour[72]=(90, 90, 100);             led_colour[92]=(90, 90, 100);             led_colour[112]=(90, 90, 100)
led_colour[73]=(90, 90, 100);             led_colour[93]=(90, 90, 100);             led_colour[113]=(90, 90, 100)
led_colour[74]=(90, 90, 100);             led_colour[94]=(90, 90, 100);             led_colour[114]=(90, 90, 100)
led_colour[75]=(90, 90, 100);             led_colour[95]=(90, 90, 100);             led_colour[115]=(90, 90, 100)
led_colour[76]=(90, 90, 100);             led_colour[96]=(90, 90, 100);             led_colour[116]=(90, 90, 100)
led_colour[77]=(90, 90, 100);             led_colour[97]=(90, 90, 100);             led_colour[117]=(90, 90, 100)
led_colour[78]=(0,0,0);                   led_colour[98]=(0,0,0);                   led_colour[118]=(0,0,0)
#FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF                   #FIRST ROW - FIRST HALF
led_colour[2]=(0,0,0);                    led_colour[22]=(0,0,0);                   led_colour[42]=(0,0,0)
led_colour[3]=(90, 90, 100);              led_colour[23]=(90, 90, 100);             led_colour[43]=(90, 90, 100)
led_colour[4]=(90, 90, 100);              led_colour[24]=(90, 90, 100);             led_colour[44]=(90, 90, 100)
led_colour[5]=(90, 90, 100);              led_colour[25]=(90, 90, 100);             led_colour[45]=(90, 90, 100)
led_colour[6]=(90, 90, 100);              led_colour[26]=(90, 90, 100);             led_colour[46]=(90, 90, 100)
led_colour[7]=(0,0,0);                    led_colour[27]=(0,0,0);                   led_colour[47]=(0,0,0)
#FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF                  #FIRST ROW - SECOND HALF
led_colour[12]=(0,0,0);                   led_colour[32]=(0,0,0);                   led_colour[52]=(0,0,0)
led_colour[13]=(90, 90, 100);             led_colour[33]=(90, 90, 100);             led_colour[53]=(90, 90, 100)
led_colour[14]=(90, 90, 100);             led_colour[34]=(90, 90, 100);             led_colour[54]=(90, 90, 100)
led_colour[15]=(90, 90, 100);             led_colour[35]=(90, 90, 100);             led_colour[55]=(90, 90, 100)
led_colour[16]=(90, 90, 100);             led_colour[36]=(90, 90, 100);             led_colour[56]=(90, 90, 100)
led_colour[17]=(0,0,0);                   led_colour[37]=(0,0,0);                   led_colour[57]=(0,0,0)

update()

if total_hp < 0: print("\n GAME OVER! YOU LOST! \n")         



