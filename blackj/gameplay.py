# library used to obtain game cards randomly
import random
# llibrary used to time each stage of the game
import time

from blackj.deck import Deck
from blackj.deck import Card

# library used to colorize
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Function Create players ------------------------------------------------


def create_players(player_name, my_deck):
    """
    Create player and dealer objects with initial cards.
    Convert card values to a format suitable for display.
    Return player and dealer objects.
    If player or dealer starts with 22pts (two Aces), the deck is shuffled
    and new player and dealer objects are created.
    """
    player = {'name': player_name,
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}
    dealer = {'name': 'Dealer',
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}

    player['hand'] = [(card.value, card.suit) for card in player['hand']]
    dealer['hand'] = [(card.value, card.suit) for card in dealer['hand']]

    # If steatment to check if player or dealer has started with 22pts

    if calculate_points(player['hand']) == 22:
        my_deck.shuffle()
        player, dealer = create_players(player_name, my_deck)

    if calculate_points(dealer['hand']) == 22:
        my_deck.shuffle()
        player, dealer = create_players(player_name, my_deck)

    return player, dealer

# Deal cards and Function Create players ----------------------------------


def deal_cards(my_deck):
    """
    Function to deal two cards from the deck.
    Return a list containing two cards dealt from the deck.
    """
    return [my_deck.draw_card(), my_deck.draw_card()]

# Convert str card_value to int --------------------------------------------


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
            return 11
        elif card_value == '10':
            return 10
        else:
            return 0


# Stand or Hit function -------------------------------------------------------


def stand_or_hit(player, dealer, my_deck):
    """
    Function to handle the player's turn. Choice between Stand (s) or Hit (h)
    If HIT is chosen, a card is drawn and added to the player's hand.
    If Stand is chosen, player keep with his hand and is dealer's turn.
    """
    while True:

        player_sum = calculate_points(player['hand'])

        if player_sum >= 15:
            choice = input(Fore.BLUE + f"{player['name']}, Do you want to STAND (s)"
                           " or HIT (h)?\n------------------------------------"
                           "--------------------------------------------\n")
        else:
            time.sleep(3)
            print(Fore.RED + "You need to drawn a card (until you get 15 points or more)")
            print("-----------------------------------------------------------"
                  "---------------------")
            time.sleep(3)
            choice = 'h'

        if choice == 's':
            break
        elif choice == 'h':
            drawn_card = my_deck.draw_card()
            player['hand'].append((drawn_card.value, drawn_card.suit))
            print(f"\n{player['name']}, You drawn: {drawn_card.value}"
                  f" of {drawn_card.suit}\n")
            player_sum = calculate_points(player['hand'])
            if player_sum > 21:
                print(Fore.RED + "\nYOU BUST!!... dealer's turn...\n")
                return
            elif player_sum == 21:
                print(Fore.YELLOW +"\nYou've got 21 points! dealer's turn\n")
                return
        else:
            print(Fore.RED + "Invalid input, please (s) for stand or (h) for hit\n")


# Dealer's turn----------------------------------------------------------------

def dealer_turn(dealer, my_deck):
    """
    Dealer turn.
    while loop for hit a new card until get <= 17pts or more.
    """
    while calculate_points(dealer['hand']) <= 17:
        draw_card = my_deck.draw_card()
        dealer['hand'].append((draw_card.value, draw_card.suit))
        print(f"\nDealer drew: {draw_card.value} of {draw_card.suit}")
    return dealer

# Function to show the winner -------------------------------------------------


def show_winner(player_score, dealer_score):
    """
    Determines the winner of the game based on player and dealer scores.
    Display a message indicating the outcome of the game.
    """
    if player_score > 21 and dealer_score > 21:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nYou both bust... it's a TIE\n"
    elif player_score > 21:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nYou bust... DEALER WINS!\n"
    elif dealer_score > 21:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nDealer busts... YOU WIN!\n"
    elif player_score < dealer_score:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nDEALER WINS!\n"
    elif player_score > dealer_score:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nYOU WIN!\n"
    else:
        print("---------------------------------------------------------------"
              "-----------------")
        return "\nIt's a TIE!\n"

# Display player and dealer's hand --------------------------------------------


def display_hand(player, dealer):
    """
    Display player and dealer hands
    """
    player_hand = [f"{card} of {suit}" for card, suit in player['hand']]
    dealer_hand = [f"{card} of {suit}" for card, suit in dealer['hand']]

    print(f"\n{player['name']}'s hand: {', '.join(player_hand)}\n")
    print(f"{dealer['name']}'s hand: {', '.join(dealer_hand)}")

# Display player's hand -------------------------------------------------------


def display_player_hand(player):
    """
    Display player's hand
    """
    player_hand = [f"{card} of {suit}" for card, suit in player['hand']]

    print(f"\n{player['name']}'s hand: {', '.join(player_hand)}\n")

# Display dealer's hand -------------------------------------------------------


def display_dealer_hand(dealer):
    """
    Display dealer's hand
    """
    dealer_hand = [f"{card} of {suit}" for card, suit in dealer['hand']]

    print(f"{dealer['name']}'s hand: {', '.join(dealer_hand)}")

# Calculate the point ---------------------------------------------------------


def calculate_points(hand):
    """
    Function to calculate the points
    """
    player_points = 0

    for card_value, _ in hand:
        player_points += card_value_to_int(card_value)

    return player_points

# Calculate final winner after 5 rounds ---------------------------------------


def result_final_winner(player_round, dealer_round):
    """
    Display a final winner message based on 5 rounds played
    """
    if player_round > dealer_round:
        return "Player"
    elif player_round < dealer_round:
        return "Dealer"
    else:
        return "Its a tie"
