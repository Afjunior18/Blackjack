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
    print("Blackjack Rules!\n")
    print("Blackjack Rules!\n\n"
          "The goal of the game is to outscore the dealer.\n"
          "Each round consists of 5 matches.\n"
          "The champion is the one who wins the most matches in the round.\n\n"
          "The objective is to either reach a total of 21 points or get as close as possible without exceeding it.\n\n"
          "At the beginning of a round. The player has two options:\n")
    print("1 - The player can either STAND their current cards and pass the turn to the dealer\n" 
          "2 - The player can HIT an additional card\n\n")
    print('"Its important to note that going over 21 points results in a BUST"\n\n'
          "During the dealer's turn, they decide whether to maintain their current point total\n"
          "or request an additional card, following the same rule as the player.\n\n"
          "Once both have made their decisions.\n"
          "The points for each player are calculated, and a message indicates the winner of the round.\n\n")
    print("Card Values:\n"
          "2 = 2\n"
          "3 = 3\n"
          "4 = 4\n"
          "5 = 5\n"
          "6 = 6\n"
          "7 = 7\n"
          "8 = 8\n"
          "9 = 9\n"
          "10 = 10\n"
          "J = 10\n"
          "Q = 10\n"
          "K = 10\n"
          "A = 11\n")