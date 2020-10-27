#LIBRARIES
import random

#DEFINITIONS
def weapon(dmg, wpn):
    global remaining_boss_health; global boss_health; global total_hp; global remaining_hp 
    
    remaining_boss_health = boss_health - dmg; boss_health = remaining_boss_health    
    remaining_hp = total_hp - random.randint(30, 50); total_hp = remaining_hp
      
    print("\n You used", wpn, "and dealt", dmg, "damage! \n")
    
#BOSSES DICTIONARY
bosses = { "GANNON" : 400, "NAYDRA" : 300, "MORPHA" : 200, "GANONDORF" : 500, "TWINROVA" :  250 }

#VARIABLES FOR HEALTH SYSTEM
boss_health = int()
remaining_boss_health = int()
total_hp = 300
remaining_hp = int()

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
    print(bosses)                                                            #DEBUGGING ONLY

        
    while boss_health > 0 and total_hp > 0:  
         
                 
        #BOSS INTERFACE        
        print("\n BOSS: ", name)
        print("\n HEALTH:", boss_health) 
        print("\n USER HP:", total_hp)                                       #DEBUGGING ONLY
         
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
                
if total_hp < 0:                    
    print("\n GAME OVER! YOU LOST! \n")
    
    

  