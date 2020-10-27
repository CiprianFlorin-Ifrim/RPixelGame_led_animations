import random

bosses = { "GANNON" : 400, "NAYDRA" : 300, "MORPHA" : 200, "GANONDORF" : 500, "TWINROVA" :  250 }

boss_health = int()
remaining_boss_health = int()


while boss_health <= 0:
    #BOSS SELECTION
    boss_selected = random.choice(list(bosses.items()))
    name = boss_selected[0]
    boss_health = boss_selected[1]

    while boss_health > 0:  
         
        print(name)
        print(boss_health) 
         
        #WEAPONS MENU
        weapons_menu = """
         _____________________
        |                     |
        |    Select weapon:   |
        |                     |
        | The Master Sword    |
        | Boomerang           |
        | Knight's Broadsword |
        | Zora Sword          |
        | Torch               |
        |_____________________|
        """ 
        print(weapons_menu)

        raw_menu = input("You choice of weapon: ")
        menu = int(raw_menu)

        if (menu == 1):
            print('\n You chose THE MASTER SWORD and dealth 50 damage! \n')
            remaining_boss_health = boss_health - 50
            boss_health = remaining_boss_health
            print("Remaining boss health: ", remaining_boss_health)
            
            
    print("\n Congratulations, you completed the game! \n")   
    break
    

  