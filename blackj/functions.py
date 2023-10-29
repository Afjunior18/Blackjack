import os
from blackj.classes import Deck
from blackj import functions



# Welcome message -------------------------------------------------------------------------------------

def welcome_message():
    """
    Display a welcome message and prompt the player for their name.
    Ensure that the input is valid (letters only) and return the formatted name.
    """
    print("Blackjack Game!\n")
    try:
        name = input("What is your player's name?\n")
        name = name.capitalize()
        if not name.isalpha():
            raise ValueError("Invalid input, Please enter letters only\n")
    except ValueError as e:
        print(e)
        while True:
            name = input("Please enter your name, 'letters only'\n")
            name = name.capitalize()
            if name.isalpha():
                break
    else:
        print(f"\nWelcome {name} to the Blackjack Game!\nLet's have fun...\n")

    return name

# Rules ------------------------------------------------------------------------------------------------

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
          "A = 1\n")
    
    
# Clear terminal ---------------------------------------------------------------------------------------

def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

# Menu rules/start game --------------------------------------------------------------------------------

def menu():
    """
    Display menu options and handle user's choice.
    """
    while True:
        print("Wanna see the GAME RULES, press (1) or START GAME preesing (2)\n")
        start_game = 2
        rules_game = 1
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            rules_blackjack()
            break
        elif choice == "2":
            pass
            break
        else:
            print("Invalid Choice: Please choose '1' or '2'")
            
# Deal cards and Function Create players ---------------------------------------------------------------

def deal_cards(my_deck):
    """
    Function to deal two cards from the deck.
    Return a list containing two cards dealt from the deck.
    """
    return [my_deck.draw_card(), my_deck.draw_card()]

def create_players(player_name, my_deck):
    player = {'name': player_name, 
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}
    dealer = {'name': 'Dealer', 
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}
    
    player['hand'] = [functions.card_value_to_int(card.value) for card in player['hand']]
    dealer['hand'] = [functions.card_value_to_int(card.value) for card in dealer['hand']]
    
    return player, dealer

# Convert Card value to int ----------------------------------------------------------------------------

def card_value_to_int(card_value):
    """
    Function to convert str card_value to int
    """
    if card_value.isdigit():
        return int(card_value)
    else:
        if card_value == 'Jack':
            return 10
        elif card_value == 'Queen':
            return 10
        elif card_value == "King":
            return 10
        elif card_value == 'Ace':
            return 1
        elif card_value == '10':
            return 10
        else:
            return 0
        