def lets_play_again():
    print("\nDo you want to play again? (y or n)")
    #convert the player's input to lower_case
    answer = input(">").lower()
    if answer=="y":
        start()
    else :
        exit()

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    lets_play_again()
def treasure_room():
    print ("\n You are now in a room filled with diamonds!")
    print ("\n And there is a door too!")
    print ("\n What would you do? (1 or 2)")
    print ("\n 1). there some diamonds and go through the door.")
    print ("\n 2). Just go through the door.")
    answer = input(">")
    if answer=="1":
        game_over("Diamonds is not real and i will make you die!")
    elif answer=="2":
        print("\n Congrats you win the game!")
        lets_play_again()
    else:
        game_over("Enter a number Dude!")
        
def monster_room():
    print("\n You are now in a room of monster!")
    print("\n The monster is sleeping.\n Behind the monster, there is another door. What would you do? (1 or 2)")
    print("\n 1). Go through the door silently.")
    print("\n 2). Be Brave, Kill the monster and show the courage!")
    answer = input(">")
    if answer=="1":
        treasure_room()
    elif answer=="2":
        game_over("The monster was hungry, he/it ate you!")
    else:
        game_over("Enter a number Dude!")

def snake_room(): 
    print ("\n There is a snake here.")
    print ("\n Behind the snake is another door.")
    print ("\n The snake is having aggs!")
    print ("\n What would you do? (1 or 2)")
    print ("\n 1). Take the eggs.")
    print ("\n 2). Taut the Snake.")
    answer = input(">")
    if answer=="1":
        game_over("Snake will kill you!")
    elif answer=="2":
        print("\n Good choice, You can go now through door now!")
        treasure_room()
    else:
        game_over("Enter a number Dude!")

def start():
    print("\n You are standing in the dark room.")
    print("\n There is a door to your left and right, which one do you take? (right/left)")
    answer = input(">")
    if "left" in answer:
        snake_room()
    elif "right" in answer:
        monster_room()
    else:
        game_over("Enter a number Properly!")
start()