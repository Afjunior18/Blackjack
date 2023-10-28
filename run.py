from blackj.welcome_message import welcome_message
from blackj.clear_terminal import clear_terminal
from blackj.rules_blackjack import rules_blackjack
from blackj.menu import menu
from blackj.classes import Card
from blackj.classes import Deck


my_deck = Deck()


if __name__ == "__main__":
    
    welcome_message()
    menu()
    
    my_deck.display_deck()