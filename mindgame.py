import json

game_mode: int = 0

# Welcome message
print("\nWelcome to Mindgame!\nSelect your mode by inputting its number.\n")
print("1) Single Player VS AI\n2) Local 1v1\n3) Online 1v1\n")

# Game mode selection
while game_mode == 0:
    try:
        game_mode = int(input("> "))
    except ValueError:
        print("Type in the number for the game you want!")
    if game_mode < 0 or game_mode > 3:
        game_mode = 0
        print("You must choose between numbers 1 - 3!")

print("SELECTED MODE: " + str(game_mode))

print("Thank you for selecting! Try not to lose...")
print("~~~~~~~~~~END OF PROGRAM~~~~~~~~~~")