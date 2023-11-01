from colorama import Fore, Back, Style, init
init(autoreset=True)
import random

class Card:
    """
    Class that represents one card
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
    
    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    """
    Class that represents all thes cards in a deck.
    Will display
    """
    def __init__(self):
        suits = ['\u2665', '\u2666', '\u2663', '\u2660']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def display_deck(self):
        for card in self.cards:
            print(f"{card.value} of {card.suit}")
        
    def draw_card(self):
        return random.choice(self.cards)
    