# import function P1Random from p1_random module
from p1_random import P1Random

# declare global variables
rng = P1Random()
player_card = ""
second_card = ""
computer_card = ""
num_player = 0
num_won = 0
num_lost = 0
num_ties = 0
num_played = 0;
hand = 0
player_exit = False

# while loop which loops until player wants to exit(player_exit = true)
while not player_exit:
    # Gets random number and assigns card based on random number
    print("START GAME#", (num_played + 1))
    print()
    random_number = rng.next_int(13) + 1
    if random_number == 1:
        card = "ACE!"
    elif 2 <= random_number <= 10:
        card = str(random_number) + "!"
    elif random_number == 11:
        card = "JACK!"
    elif random_number == 12:
        card = "QUEEN!"
    elif random_number == 13:
        card = "KING!"

    # Assigns face cards with specific values
    if card == 'KING!' or card == 'QUEEN!' or card == 'JACK!':
        random_number = 10
    hand += random_number
    print("Your card is a", card)
    print("Your hand is:", hand)
    print()

    # Loop which asks player for input on how to continue game
    while not player_exit:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()
        option = int(input("Choose an option:"))
        print()
        # Assigns card based on random number and userinput.
        if option == 1:
            second_random_number = rng.next_int(13) + 1
            if second_random_number == 1:
                second_card = "ACE!"
            elif 2 <= second_random_number <= 10:
                second_card = str(second_random_number) + "!"
            elif second_random_number == 11:
                second_card = "JACK!"
            elif second_random_number == 12:
                second_card = "QUEEN!"
            elif second_random_number == 13:
                second_card = "KING!"
            if second_card == 'KING!' or second_card == 'QUEEN!' or second_card == 'JACK!':
                second_random_number = 10
            hand += second_random_number
            print("Your card is a", second_card)
            print("Your hand is:", hand)
            print()
        # Shows possible win and lose cases and breaks the outer loop
            if hand == 21:
                print("BLACKJACK! You win!")
                num_won += 1
                hand = 0
                num_played += 1
                break
            elif hand > 21:
                print("You exceeded 21! You lose.")
                num_lost += 1
                hand = 0
                num_played += 1
                break

        # Shows case where user holds hand and competes with dealer
        # Gives dealer a specific card and random number and chooses winner/loser based on conditions
        elif option == 2:
            num_played += 1
            computer_number = (rng.next_int(11) + 16)
            print("Dealer's hand:", computer_number)
            print("Your hand is:", hand)
            print()
            if computer_number > 21:
                print("You win!")
                print()
                num_won += 1
                hand = 0
                break
        # Each conditional statement updates global variables and statistics
            elif computer_number == hand:
                print("It's a tie! No one wins!")
                num_ties += 1
                hand = 0
                break
            elif computer_number > hand:
                print("Dealer wins!")
                num_lost += 1
                hand = 0
                break
            elif hand > computer_number:
                print("You win!")
                print()
                num_won += 1
                hand = 0
                break

        # Shows option where user wants to print statistics
        elif option == 3:
            if num_played == 0:
                percentage = 0

            else:
                percentage = (num_won / num_played) * 100
                percentage = str(percentage) + "%"
                print("Number of Player wins:", num_won)
                print("Number of Dealer wins:", num_lost)
                print("Number of tie games:", num_ties)
                print("Total # of games played is:", num_played)
                print("Percentage of Player wins:", percentage)
                continue
        # option where user chooses to exit the game
        elif option == 4:
            player_exit = True
            break

        # if user inputs invalid input prints error and restarts inner loop
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue








