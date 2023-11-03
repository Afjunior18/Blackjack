# Welcome message ---------------------------------------------------------------------------------

def welcome_message():
    """
    Display a welcome message and prompt the player for their name.
    Ensure that the input is valid (letters only) and return the formatted name.
    """
    print("Blackjack Game!")
    print("-------------------------------------------------------------------------\n")
    while True:
        try:
            name = input("What is your player's name?\n")
            name = name.capitalize()
            if not name.isalpha():
                raise ValueError("Invalid input, Please enter letters only\n")
            if len(name) >= 15:
                raise ValueError("\nName to long, please enter a short name.(No more than 15 caracteres)")
        except ValueError as e:
            print(e)
        else:
            print(f"Welcome {name} to the Blackjack Game!\n")
            return name

# Rules ------------------------------------------------------------------------------------------

def rules_blackjack():
    """
    Display the rules of the Blackjack game.
    """
    print("Blackjack Rules!")
    print("--------------------------------------------------------------------------------")
    print("The goal is to outscore the dealer in 5 matches per round.\n"
          "the winner is the one with the most match wins in the round.\n")
    print("Objective:")
    print("--------------------------------------------------------------------------------")
    print("Reach a total of 21pts or get as close as possible without bust it.\n")
    print("Options:")
    print("--------------------------------------------------------------------------------")
    print("1 - STAND: Keep current cards and pass the turn to the dealer.\n"
          "2 - HIT: Draw an additional card.\n")
    print("Notes:")
    print("--------------------------------------------------------------------------------")
    print("Exceeding 21 points results in a BUST.")
    print("Ace always counts as 11pts. If you start with 2 Aces, one will be replaced.\n")
    print("Player's Turn:")
    print("--------------------------------------------------------------------------------")
    print("Is required to HIT until reaching 15pts, then can choose to STAND or HIT.\n")
    print("Dealer's Turn:")
    print("--------------------------------------------------------------------------------")
    print("Dealer will always HIT until reaching 17 points or higher.\n")
    print("Scoring: 2 - 10: Face value, Jack, Quen, King: 10 pts, Ace: 11pts)")