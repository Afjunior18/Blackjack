# Initialize colorama and set autoreset to ensure colors only apply to specified text
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Importing custom functions and classes from the 'blackj' package
from blackj import functions
from blackj import classes


my_deck = classes.Deck()


if __name__ == "__main__":
    
    player_name = functions.welcome_message()
    
    player, dealer = functions.create_players(player_name, my_deck)
    
    functions.menu()
    
    # my_deck.display_deck()
    
    functions.display_hand(player, dealer)

