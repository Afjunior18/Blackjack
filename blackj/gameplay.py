from blackj.deck import Deck
from blackj.deck import Card
import time

# Function Create players ------------------------------------------------

def create_players(player_name, my_deck):
    """
    Create player and dealer objects with initial cards.
    Convert card values to a format suitable for display.
    Return player and dealer objects.
    """
    player = {'name': player_name, 
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}
    dealer = {'name': 'Dealer', 
              'hand': [my_deck.draw_card(), my_deck.draw_card()]}
    
    player['hand'] = [(card.value, card.suit) for card in player['hand']]
    dealer['hand'] = [(card.value, card.suit) for card in dealer['hand']]
    
    #Check if player or dealer starts with 22 points (two Aces)
     
    if calculate_points(player['hand']) == 22:
        # Replace one Ace with a new card
        player['hand'] = [card for card in player['hand'] if card[0] != 'Ace']
        player['hand'].append((my_deck.draw_card().value, my_deck.draw_card().suit))
        
    if calculate_points(dealer['hand']) == 22:
        # Replace one Ace with a new card
        dealer['hand'] = [card for card in dealer['hand'] if card[0] != 'Ace']
        dealer['hand'].append((my_deck.draw_card().value, my_deck.draw_card().suit))

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


# Stand or Hit function ------------------------------------------------------------

def stand_or_hit(player, dealer, my_deck):
    """
    Function to handle the player's turn. Choice between Stand (s) or Hit (h)
    If HIT is chosen, a card is drawn and added to the player's hand.
    If Stand is chosen, player keep with his hand and is dealer's turn.
    """
    while True:
        
        player_sum = calculate_points(player['hand'])
        
        if player_sum >= 15:
            choice = input(f"\n{player['name']}, Do you want to STAND (s) or HIT (h)?")
        else:
            time.sleep(3)
            print("You need to drawn a card (until upu get 15 points or more)")
            time.sleep(3)
            choice = 'h'
            
        if choice == 's':
            break
        elif choice == 'h':
            drawn_card = my_deck.draw_card()
            player['hand'].append((drawn_card.value, drawn_card.suit))
            print(f"\n{player['name']}, You drawn: {drawn_card.value} of {drawn_card.suit}\n")
            player_sum = calculate_points(player['hand'])
            if player_sum > 21:
                print("\nYOU BUST!!... dealer's turn...")
                return
            elif player_sum == 21:
                print("\n You've got 21 points! dealer's turn")
                return
        else:
            print("Invalid input, please (s) for stand or (h) for hit")
    

# Dealer's turn-----------------------------------------------------------------------

def dealer_turn(dealer, my_deck):
    """
    Function dealer turn.
    while loop for hit a new card until get <= 17 points
    """
    while calculate_points(dealer['hand']) <= 17:
        draw_card = my_deck.draw_card()
        dealer['hand'].append((draw_card.value, draw_card.suit))
        print(f"\nDealer drew: {draw_card.value} of {draw_card.suit}")
    return dealer

# Function to show the winner --------------------------------------------------------

def show_winner(player_score, dealer_score):
    """
    Determines the winner of the game based on player and dealer scores.
    Display a message indicating the outcome of the game.
    """
    if player_score > 21 and dealer_score > 21:
        print("-------------------------------------------------------------------------")
        return "\nYou both bust... it's a TIE\n"
    elif player_score > 21:
        print("-------------------------------------------------------------------------")
        return "\nYou bust... DEALER WINS!\n"
    elif dealer_score > 21:
        print("-------------------------------------------------------------------------")
        return "\nDealer bust... YOU WIN!\n"
    elif player_score < dealer_score:
        print("-------------------------------------------------------------------------")
        return "\nDEALER WINS!\n"
    elif player_score > dealer_score:
        print("-------------------------------------------------------------------------")
        return "\nYOU WIN!\n"
    else:
        print("-------------------------------------------------------------------------")
        return "\nIt's a TIE!"

# Display player's hand and dealer's hand -----------------------------------------------

def display_hand(player, dealer):
    """
    Display player and dealer hands
    """
    player_hand = [f"{card} of {suit}" for card, suit in player['hand']]
    dealer_hand = [f"{card} of {suit}" for card, suit in dealer['hand']]

    print(f"\n{player['name']}'s hand: {', '.join(player_hand)}\n")
    print(f"{dealer['name']}'s hand: {', '.join(dealer_hand)}")

# Function to count Aces in the player's hand--------------------------------------------

"""
def count_aces(hand):

    ace_count = 0
    for card in hand:
        if card[0] == 'Ace':
            ace_count += 1
    
    return ace_count
"""

# Calculate the point -------------------------------------------------------------------

def calculate_points(hand):
    """
    Function to calculate player's hand
    """
    player_points = 0
    # num_aces = count_aces(hand)
    
    for card_value, _ in hand:
        player_points += card_value_to_int(card_value)
    
    # while player_points > 21 and num_aces > 0:
        # player_points -= 10
    
    return player_points

# Calculate final winner after 5 rounds ---------------------------------------------------

def result_final_winner(player_round, dealer_round):
    """
    """
    if player_round > dealer_round:
        return "Player"
    elif player_round < dealer_round:
        return "Dealer"
    else:
        return "Its a tie"
        
    
