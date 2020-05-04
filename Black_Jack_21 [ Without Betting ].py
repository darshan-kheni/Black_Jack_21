############################### This Code Was Created By Darshan Kheni ###############################

import random

Dealer_Card = []
Player_Card = []

print(" Welcome to BlackJack 21 ")

# Dealer CArd
while len(Dealer_Card) != 2:
    Dealer_Card.append(random.randint(1,11))
    if len(Dealer_Card) == 2:
        # print(Dealer_Card)
        print("Dealer card :: ["+str(Dealer_Card[0])+",_]")

# Player CArd
while len(Player_Card) != 2:
    Player_Card.append(random.randint(1,11))
    if len(Player_Card) == 2:
        print("Player card :: "+str(Dealer_Card))
        print(sum(Player_Card))
    if sum(Player_Card) == 21:
        print("Player Card Total :: "+sum(Player_Card))
        print("Player Is Win... You are BlackJack 21 ")

# For Player and Dealer Both
if sum(Player_Card) < 21:
    while sum(Player_Card) <= 21 or sum(Dealer_Card) <= 21:
        enter = input("Choose [H] For Hit, [S] For Stand and [Q] For Quite :: ").upper()
        if enter == 'H':
            Player_Card.append(random.randint(1, 11))
            print(Player_Card)
            print(sum(Player_Card))
            if sum(Player_Card) == 21:
                print("You Are Win The Game...")
                break
            elif sum(Player_Card) > 21:
                print("Dealer is Win...! You Are Lose The Game...")
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
                print("You are Win The game...")
                break
            else:
                if sum(Player_Card) > sum(Dealer_Card) :
                    print("You are Win The game...")
                    break
                else:
                    print("Dealer is Win The game...")
                    break

        if enter == 'Q':
            print("******** Thanks For Playing ********")
            break

        if enter != 'H' and enter != 'S' and enter != 'Q':
            print("Please Select Right Charecter.")


print("____________________ This Game Is Created By Darshan & Vivek ____________________")

