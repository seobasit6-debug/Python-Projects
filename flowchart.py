print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You come to a crossroad. Do you go left or right? ').strip().lower()

if choice1 == "left":
    choice2 = input('You come to a lake. Do you swim or wait? ').strip().lower()

    if choice2 == "wait":
        choice3 = input('You arrive at a house with three doors: red, yellow, and blue. Which door do you choose? ').strip().lower()

        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")