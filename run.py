
from colorama import Fore, Back, Style, init
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit, display_hand
from blackj.deck import Deck
from blackj.utilities import clear_terminal
from blackj.gameplay import card_value_to_int, calculate_points, dealer_turn, show_winner

init(autoreset=True)



menu()
clear_terminal()
player_name = welcome_message()

def main():
    """
    Main loop of the game, totalizing 5 rounds to check at the end who's the winner.
    """
    total_round = 0
    player_points = 0
    dealer_points = 0
    
    while total_round < 5: # total rounds 
        total_round += 1 
        my_deck = Deck() # create a deck of cards (from my class Deck)
        
        player, dealer = create_players(player_name, my_deck)
        
        print("\nBlack Jack Game!!!")
        print("-------------------------------------------------------------------------")
        display_hand(player, dealer) # function so show up player and dealer objects with initial cards
        
        stand_or_hit(player, dealer, my_deck) # plyer's turn, has to decide if Stand or Hit a new card
        
        player_score = calculate_points(player['hand']) # calculate the player's score
        
        print("\n--------------------------- DEALER'S TURN!!! ----------------------------")
        
        dealer_turn(dealer, my_deck) # Function to call dealer's turn
        
        dealer_score = calculate_points(dealer['hand'])
        
        print(f"\nPlayer's score: {player_score} points")
        print(f"Dealer's score: {dealer_score} points")
        print("-------------------------------------------------------------------------")     
        
        winner_result = show_winner(player_score, dealer_score)
        
        print(winner_result)
        print("-------------------------------------------------------------------------")
    
        if "Player" in winner_result:
            player_points += 1
        elif "Dealer" in winner_result:
            dealer_points += 1
    
        print("\nGame Over - The wninner is: ")
        print(f"\nPlayer's total score: {player_points}")
        print(f"Dealer's total score: {dealer_points}")
    
    print("\n-------------------------- The WINNER IS: -------------------------------")
    
    if player_points > dealer_points:
        print("\nCongrats! You're the WINNER")
        print("-------------------------------------------------------------------------")
    elif player_points == dealer_points:
        print("\nIt's a tie!")
        print("-------------------------------------------------------------------------")
    else:
        print("\nYou Lose!! DEALER WINS...")
        print("-------------------------------------------------------------------------")



if __name__ == "__main__":

    main()
