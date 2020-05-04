############################### This Code Was Created By Darshan Kheni ###############################

import random

Dealer_Card = []
Player_Card = []

print("Welcome to BlackJack 21 ")

# For Betting
Bet = float(input("Enter Your Bet [0.1$], [1$], [5$], [10$], [25$], [50$], [100$] :: "))

# Dealer CArd
while len(Dealer_Card) != 2:
    Dealer_Card.append(random.randint(1,11))
    if len(Dealer_Card) == 2:
        # print(Dealer_Card)
        print("Dealer card :: ["+str(Dealer_Card[0])+", _]")

# Player CArd
while len(Player_Card) != 2:
    Player_Card.append(random.randint(1,11))
    if len(Player_Card) == 2:
        print("Player card :: "+str(Dealer_Card))
        print(sum(Player_Card))
    if sum(Player_Card) == 21:
        print("Player Card Total :: "+sum(Player_Card))
        print("Player Is Win... You are BlackJack 21 ")

# After Betting
if Bet == 0.1 or Bet == 1 or Bet == 5 or Bet == 10 or Bet == 25 or Bet == 50 or Bet == 100:

    # For Player and Dealer Both
    if sum(Player_Card) < 21:
        while sum(Player_Card) <= 21 or sum(Dealer_Card) <= 21:
            enter = input("Choose [H] For Hit, [S] For Stand and [Q] For Quite :: ").upper()
            if enter == 'H':
                Player_Card.append(random.randint(1, 11))
                print(Player_Card)
                print(sum(Player_Card))
                if sum(Player_Card) == 21:
                    print("You Are Win The Game... By {}$".format(Bet+Bet))
                    break
                elif sum(Player_Card) > 21:
                    print("Dealer is Win...! You Are Lose The Game... By {}$".format(Bet))
                    break

            if enter == 'S':
                Dealer_Card.append(random.randint(1,11))
                print("Dealer Card : ",str(Dealer_Card))
                print("Player Card : ",str(Player_Card))
                print("Sum of Dealer Card : ",sum(Dealer_Card))
                print("Sum of Player Card : ",sum(Player_Card))
                if sum(Dealer_Card) == sum(Player_Card):
                    print("OOPs, It's Draw")
                    break
                if sum(Dealer_Card) > 21 :
                    print("You are Win The game... By {}$".format(Bet+Bet))
                    break
                else:
                    if sum(Player_Card) > sum(Dealer_Card) :
                        print("You are Win The game... By {}$".format(Bet+Bet))
                        break
                    else:
                        print("Dealer is Win...! You Are Lose The Game... By {}$".format(Bet))
                        break

            if enter == 'Q':
                print("******** Thanks For Playing ********")
                break

            if enter != 'H' and enter != 'S' and enter != 'Q':
                print("Please Select Right Charecter.")

else:
    print("Please Select Right Value.")

print("\n"*3)
print("____________________ This Game Is Created By Darshan & Vivek ____________________")

