import random
# BlackJack or 21 Game
#Dealer Cards
Dealer_Cards = []
#Player Cards
Player_Cards = []
#Deal the Cards
print(" ")
print("-------Start Game---------")
print(" ")
#Display the Cards
#Dealer cards
while len(Dealer_Cards) != 2:
    Dealer_Cards.append(random.randint(1,11))
    if len(Dealer_Cards) == 2:
        print("Dealer has: ? and ", Dealer_Cards[1])

#Player Cards
while len(Player_Cards) != 2:
    Player_Cards.append(random.randint(1,11))
    if len(Player_Cards) == 2:
        print("You have ", Dealer_Cards[0],"and", Dealer_Cards[0] )

#Sum of the Dealer Cards
if sum(Dealer_Cards) == 21:
    print("Dealer has 21 and Won")
elif sum(Dealer_Cards) > 21:
    print("Dealer has Busted")

#Sum of the Player Cards~
print(" ")
while sum(Player_Cards) < 21:

    action_taken = input("Do you want to Stay or Hit? \n" )
    print(" ")
    if action_taken == "hit" or action_taken == "Hit" or action_taken == "h" or action_taken == "H" :
        Player_Cards.append(random.randint(1,11))
        print("You now have a total of", sum(Player_Cards), "from these cards",Player_Cards)
    else:
        print("The Dealer has a total of", sum(Dealer_Cards), "from these cards", Dealer_Cards[0], Dealer_Cards[1])
        print("You have a total of", sum(Dealer_Cards), "from these cards", Player_Cards[0],Player_Cards[1])
        if sum(Dealer_Cards) > sum(Player_Cards):
            print("Dealer Wins")
        else:
            print("")
            print("You Win")
            break
if sum(Player_Cards) > 21:
    print("You went bust, Dealer wins")
elif sum(Player_Cards) == 21:
    print("BLACKJACK, You Win")


#Compare The sums of the Cards Between Dealer and Player 
##If p card sum is greater than 21 = bust
##if p card sum is less than 21 = option hit of stay
##if p option Stay compare sum of Dealer vs player
##Ip p sum < 21 && >> D sum Then P Wins!

print(" ")

 