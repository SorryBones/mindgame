from getpass import getpass
import time
import sys

p1_bank: int = 100
p2_bank: int = 100
p1_wins: int = 0
p2_wins: int = 0

# Rules
print("\nRules:\nEach player has 100 points to spend each round betting.\nIf you bet more than your opponent, you win 1 round.\nYou lose all points you bet, so you have less to bet with next round.\nWhoever wins the most rounds before somebody's points hit zero wins!")
print("NOTE: You cannot bet more than 50 points in the first round to prevent cheesing.")
print("Good luck!\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

# Main game loop
while(p1_bank > 0 and p2_bank > 0):
    
    # Bank print and bet reset
    p1_bet = 0
    p2_bet = 0
    print("Player 1 round wins: " + str(p1_wins))
    print("Player 2 round wins: " + str(p2_wins))
    print()
    print("Player 1 bank: " + str(p1_bank))
    print("Player 2 bank: " + str(p2_bank))
    print()
    
    # Player prompts
    print("Player 1, enter your secret bet: ")
    while(p1_bet == 0):
        try:
            p1_bet = int(getpass("> "))
        except ValueError:
            print("You must enter a number!")
        if (p1_bet == 0):
            print("You have to bet something. Try again!")
        elif (p1_bet < 0):
            print("You can't bet negative numbers, don't be cheeky. Try again!")
            p1_bet = 0
        elif (p1_bet > p1_bank):
            print("You don't have enough points to bet that. Try again!")
            p1_bet = 0
        elif(p1_wins == 0 and p2_wins == 0 and 50 < p1_bet):
            print("You cannot bet more than 50 points in the first round!")
            p1_bet = 0
    print("Player 2, enter your secret bet: ")
    while(p2_bet == 0):
        try:
            p2_bet = int(getpass("> "))
        except ValueError:
            print("You must enter a number!")
        if (p2_bet == 0):
            print("You have to bet something. Try again!")
        elif (p2_bet < 0):
            print("You can't bet negative numbers, don't be cheeky. Try again!")
            p2_bet = 0
        elif (p2_bet > p2_bank):
            print("You don't have enough points to bet that. Try again!")
            p2_bet = 0
        elif(p1_wins == 0 and p2_wins == 0 and 50 < p2_bet):
            print("You cannot bet more than 50 points in the first round!")
            p2_bet = 0
    
    # Round result
    print("\nDrumroll please... ", end = '')
    time.sleep(4)
    if(p1_bet > p2_bet):
        #print("\nPlayer 1 wins the round by betting " + str(p1_bet) + " against Player 2's bet of " + str(p2_bet) + "!")
        print("Player 1 wins!")
        p1_wins += 1
        p1_bank -= p1_bet
        p2_bank -= p2_bet
        time.sleep(3)
    elif(p2_bet > p1_bet):
        #print("\nPlayer 2 wins the round by betting " + str(p2_bet) + " against Player 1's bet of " + str(p1_bet) + "!")
        print("Player 2 wins!")
        p2_wins += 1
        p1_bank -= p1_bet
        p2_bank -= p2_bet
        time.sleep(3)
    elif(p1_bet == p2_bet):
        print("You bet the same exact number! It's a tie! Nobody loses any points.")
        time.sleep(3)
    print("Player 1 bet: " + str(p1_bet))
    print("Player 2 bet: " + str(p2_bet))
    time.sleep(4)
    print("\nNext round!\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    time.sleep(1)


# Win conditions met, game over
print("The game is over!")
if(p1_wins > p2_wins):
    print("Player 1 wins!")
elif(p2_wins > p1_wins):
    print("Player 2 wins!")
elif(p1_wins == p2_wins):
    print("You tied!")
time.sleep(2)
print("Player 1 round wins: " + str(p1_wins))
print("Player 2 round wins: " + str(p2_wins))
time.sleep(2)
print("\nGood game! Play again soon.\n")
sys.exit()