from blackj.deck import Deck
from blackj.deck import Card
from blackj.utilities import card_value_to_int

# Function Create players ---------------------------------------------------------------

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
    
    return player, dealer

# Deal cards and Function Create players ------------------------------------------------

def deal_cards(my_deck):
    """
    Function to deal two cards from the deck.
    Return a list containing two cards dealt from the deck.
    """
    return [my_deck.draw_card(), my_deck.draw_card()]


# Stand or Hit function -----------------------------------------------------------------

def stand_or_hit(player, my_deck):
    """
    Function to handle the player's turn. Choice between Stand (s) or Hit (h)
    If HIT is chosen, a card is drawn and added to the player's hand.
    If Stand is chosen, player keep with his hand and is dealer's turn.
    """
    while True:
        choice = input(f"\n\n{player['name']}, Do you want to STAND (s) or HIT (h)?\n")
        if choice == 's':
            break
        elif choice == 'h':
            drawn_card = my_deck.draw_card()
            player['hand'].append((drawn_card.value, drawn_card.suit))
            print(f"\n{player['name']}: {player['hand']}\n")
        else:
            print("Invalid input, please (s) for stand or (h) for hit")

# Dealer's turn--------------------------------------------------------------------------

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

# Function to show the winner ------------------------------------------------------

def show_winner(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "Booom!! You both burst"
    elif player_score > 21:
        return "Booom!! You burst... DEALER WINS!"
    elif dealer_score > 21:
        return "Booom!! Dealer burst... YOU WIN!"
    elif player_score < dealer_score:
        return "DEALER WINS!"
    elif player_score > dealer_score:
        return "YOU WIN!"
    else:
        return "It's a tie!"

# Display player's hand and dealer's hand -----------------------------------------------

def display_hand(player, dealer):
    """
    Display player and dealer hands
    """
    player_hand = [f"{card} of {suit}" for card, suit in player['hand']]
    dealer_hand = [f"{card} of {suit}" for card, suit in dealer['hand']]

    print(f"\n{player['name']}'s hand: {', '.join(player_hand)}\n")
    print(f"{dealer['name']}'s hand: {', '.join(dealer_hand)}")

# Calculate the point -------------------------------------------------------------------

def calculate_points(hand):
    """
    Function to calculate player's hand
    """
    player_points = 0
    for card_value, _ in hand:
        player_points += card_value_to_int(card_value)
    
    return player_points