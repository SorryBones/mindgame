from getpass import getpass
import time
import sys
from ai import ai

match_ai = ai()
p1_bank: int = 100
ai_bank: int = 100
p1_wins: int = 0
ai_wins: int = 0

# Rules
print("\nRules:\nEach player has 100 points to spend each round betting.\nIf you bet more than your opponent, you win 1 round.\nYou lose all points you bet, so you have less to bet with next round.\nWhoever wins the most rounds before somebody's points hit zero wins!")
print("NOTE: You cannot bet more than 50 points in the first round to prevent cheesing.")
print("Good luck!\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

# Main game loop
while(p1_bank > 0 and ai_bank > 0):
    
    # Bank print and bet reset
    p1_bet = 0
    ai_bet = 0
    print("Player 1 round wins: " + str(p1_wins))
    print("AI round wins: " + str(ai_wins))
    print()
    print("Player 1 bank: " + str(p1_bank))
    print("AI bank: " + str(ai_bank))
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
        elif(p1_wins == 0 and ai_wins == 0 and 50 < p1_bet):
            print("You cannot bet more than 50 points in the first round!")
            p1_bet = 0
    print("The AI runs its insidious algorithms...")
    time.sleep(3)
    ai_bet = match_ai.ai_wager(ai_bank)
    
    # Round result
    print("\nDrumroll please... ", end = '')
    time.sleep(4)
    if(p1_bet > ai_bet):
        #print("\nPlayer 1 wins the round by betting " + str(p1_bet) + " against Player 2's bet of " + str(ai_bet) + "!")
        print("Player 1 wins!")
        p1_wins += 1
        p1_bank -= p1_bet
        ai_bank -= ai_bet
        time.sleep(3)
    elif(ai_bet > p1_bet):
        #print("\nPlayer 2 wins the round by betting " + str(ai_bet) + " against Player 1's bet of " + str(p1_bet) + "!")
        print("Player 2 wins!")
        ai_wins += 1
        p1_bank -= p1_bet
        ai_bank -= ai_bet
        time.sleep(3)
    elif(p1_bet == ai_bet):
        print("You bet the same exact number! It's a tie! Nobody loses any points.")
        time.sleep(3)
    print("Player 1 bet: " + str(p1_bet))
    print("Player 2 bet: " + str(ai_bet))
    time.sleep(4)
    print("\nNext round!\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    time.sleep(1)


# Win conditions met, game over
print("The game is over!")
if(p1_wins > ai_wins):
    print("Player 1 wins!")
elif(ai_wins > p1_wins):
    print("Player 2 wins!")
elif(p1_wins == ai_wins):
    print("You tied!")
time.sleep(2)
print("Player 1 round wins: " + str(p1_wins))
print("Player 2 round wins: " + str(ai_wins))
time.sleep(2)
print("\nGood game! Play again soon.\n")
sys.exit()