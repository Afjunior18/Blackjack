
from colorama import Fore, Back, Style, init
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit, display_hand
from blackj.deck import Deck
from blackj.utilities import card_value_to_int, clear_terminal
from blackj.gameplay import calculate_points, dealer_turn, show_winner

init(autoreset=True)

def main():
    my_deck = Deck()
    player_name = welcome_message()
    player, dealer = create_players(player_name, my_deck)
    menu()
    display_hand(player, dealer)
    
    stand_or_hit(player, my_deck)
        
    player_score = calculate_points(player['hand'])
    
    print("\nDEALER'S TURN!")    
    dealer_turn(dealer, my_deck)
    
    dealer_score = calculate_points(dealer['hand'])
    
    print(f"\nPlayer's Score: {player_score} points")
    print(f"Dealer's Score: {dealer_score} points")
    
    winner_result = show_winner(player_score, dealer_score) 
    print(winner_result)

if __name__ == "__main__":

    main()
