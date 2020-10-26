while True:
    print("CALCULATOR")
    raw_x= input("Please type your first number: ")
    raw_y = input("Please type your second number: ")
    print("Select the operation required:")
    print("Type 1 for addition")
    print("Type 2 for subtraction")
    print("Type 3 for the multiplication")
    print("Type 4 for the division")
    raw_menu = input() 
    menu = int(raw_menu)    
   # if (raw_x.isalnum() and raw_y.isalnum()):  
    if (menu == 1):
          x = int(raw_x)
          y = int(raw_y)
          value = x+y
          print("Your result is: " + str(value))
          break;
    elif (menu == 2):
          x = int(raw_x)
          y = int(raw_y)
          value = x-y
          print("Your result is: " + str(value))
          break;
    elif (menu == 3):
          x = int(raw_x)
          y = int(raw_y)
          value = x*y
          print("Your result is: " + str(value))
          break;
    elif (menu == 4):
          x = int(raw_x)
          y = int(raw_y)
          value = x/y
          print("Your result is: " + str(value))
          break;
  #  else:
   #       print("You have typed a character, please insert a number")