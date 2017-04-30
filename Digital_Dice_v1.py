'''
-----------------------------|
Ash of [bini-tek]            |
learn \ make \ share         |
Blog: aobinitek.blogspot.com |
Thursday : April.27.2017     |
-----------------------------|

'''

import random


# UI: to generate the range of the dice
def diceRoll():
    diceRange = int(raw_input("Enter Dice Range: "))
    TheDice = random.randint(1,diceRange)
    print("You rolled a "+ str(TheDice)+"\n")

# UI: to keep rolling the dice
def keepRolling():
   while True:
       answer = raw_input("Roll? y or n : " )
       if answer == "y":
           diceRoll()
       else:
            break
    

# calling the functions
diceRoll()
keepRolling()









               
      
    
    


