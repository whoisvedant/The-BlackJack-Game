#Importing Random Module for generating the Cards for Player and Dealer
import random

#Defining the Function name as play_game()
def play_game():
    #Initially assigning all the variables to 0.
    total_games = 0
    dealer_score = 0
    player_score = 0
    print("Welcome to The BlackJack Game!")
    print("Let's Play a best of 3 Rounds")

    #Using While loop for best of 3.
    while total_games < 3 :
        print("Game " + str(total_games + 1) + " Dealing the cards ")

        #Defining the empty list
        dealer_cards = []
        player_cards = []

        #Using while loop to give dealer two cards
        while len(dealer_cards) != 2 :
            dealer_cards.append(random.randint(1,11))
            if len(dealer_cards) == 2:
                print("Dealer has X and ", dealer_cards[1])

        #Using while loop to give player two cards
        while len(player_cards) != 2 :
            player_cards.append(random.randint(1,11))
            if len(player_cards) == 2 :
                print("You have ", player_cards)

        if sum(dealer_cards) == 21 :
            dealer_score += 1
            print("Dealer has 21 and Wins! It's a BlackJack!")
        elif sum(dealer_cards) > 21 :
            player_score += 1
            print("Dealer has Lost!")

        #Game Logic Starts from here
        #Using while loop to check the sum of player cards.
        while sum(player_cards) < 21 :
            
            #Variable to take input
            action_taken = str(input("Do you want to Stay or Hit ? "))
            if action_taken == "Hit" :
                player_cards.append(random.randint(1,11))
                print("Now you have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            else:
                print("The Dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)

                if sum(dealer_cards) > sum(player_cards) :
                    dealer_score += 1
                    print("Dealer Wins!")
                else:
                    player_score += 1
                    print("You Wins!")
                #Important to break the while loop
                break

        if sum(player_cards) == 21 :
            player_score += 1
            print("You Wins!")
        elif sum(player_cards) > 21 :
            dealer_score += 1
            print("Dealer Wins!")

        print("Current best of 3 :")
        print("Dealer : " + str(dealer_score) + " games " + " -to-you : " + str(player_score) + " games")

        #Checking the Best of three Game Score to determine who wins The BlackJack Game!
        if (dealer_score) > (player_score) :
            print("Dealer Wins The BlackJack Game!")
        else:
            print("You Wins The BlackJack Game!")
        
        print("-------------Best--------- of---------- Three-----------------")
        total_games += 1

play_game()