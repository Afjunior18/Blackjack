
from colorama import Fore, Back, Style, init
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit, display_hand
from blackj.deck import Deck
from blackj.utilities import card_value_to_int, clear_terminal
from blackj.gameplay import calculate_points

init(autoreset=True)

def main():
    my_deck = Deck()
    player_name = welcome_message()
    player, dealer = create_players(player_name, my_deck)
    menu()
    display_hand(player, dealer)
    
    stand_or_hit(player, my_deck)
        
    player_score = calculate_points(player['hand'])
    dealer_score = calculate_points(dealer['hand'])
    
    print(f"\nPlayer's Score: {player_score}")
    print(f"Dealer's Score: {dealer_score}")


if __name__ == "__main__":
    main()
