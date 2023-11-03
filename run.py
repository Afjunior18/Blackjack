
from colorama import Fore, Back, Style, init
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit, display_hand
from blackj.deck import Deck
from blackj.utilities import clear_terminal
from blackj.gameplay import card_value_to_int, calculate_points, dealer_turn, show_winner
from blackj.gameplay import result_final_winner

init(autoreset=True)



menu()
clear_terminal()
player_name = welcome_message()

def main():
    """
    Main loop of the game, totalizing 5 rounds to check at the end who's the winner.
    """
    total_round = 0
    player_round = 0
    dealer_round = 0
    
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
    
        if "YOU WIN" in winner_result:
            player_round += 1
        elif "DEALER WINS" in winner_result:
            dealer_round += 1
        
        print(f"Player round: {player_round}")
        print(f"Dealer round: {dealer_round}")
    
        print(f"\nPlayed a total of: {total_round} rounds.\n")
    
    final_winner = result_final_winner(player_round, dealer_round)
    print(f"\nPlayer wins: Total of {player_round} rounds.")
    print(f"Dealer wins: Total of {dealer_round} rounds.\n")
    
    print("\n-------------------------- The WINNER IS: -------------------------------")
    
    if final_winner == "Player":
        print("\nYou're the WINNER!!")
        print("-------------------------------------------------------------------------")
    elif final_winner == "Dealer":
        print("\nYou Lose!! DEALER WINS...")
        print("-------------------------------------------------------------------------")
    else:
        print("\nIt's a tie!...")
        print("-------------------------------------------------------------------------")



if __name__ == "__main__":
    main()