weapons = {"THE MASTER SWORD" : 3, "BOOMERANG" : 1, "KNIGHT BROADSWORD" : 2, "ZORA SWORD" : 3, "TORCH" : 5, "MOONLIGHT SCIMITAR" : 1, 
                      "FLAMEBLADE" : 2, "GUARDIAN SWORD" : 5, "ICE ROD" : 2, "KOROK LEAF" : 1, "BOULDER BREAKER" : 2, "ANCIENT SWORD" : 3 }




for x in range(0, 4):
    durability = weapons.get("THE MASTER SWORD")
    if durability > 0:
        print(durability)
        print("Available")
        weapons.update({"THE MASTER SWORD" : durability - 1})
        durability = weapons.get("THE MASTER SWORD")
        print(durability)
    elif durability == 0:
        print("Destroyed")
