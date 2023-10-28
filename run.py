from colorama import Fore, Back, Style, init
init(autoreset=True)

from blackj import functions
from blackj import classes


my_deck = classes.Deck()



if __name__ == "__main__":
    
    functions.welcome_message()
    functions.menu()
    
    my_deck.display_deck()