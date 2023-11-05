
from colorama import Fore, Back, Style, init
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit, display_hand
from blackj.deck import Deck
from blackj.utilities import clear_terminal
from blackj.gameplay import card_value_to_int, calculate_points, dealer_turn, show_winner
from blackj.gameplay import result_final_winner, display_player_hand, display_dealer_hand

import random
import time

init(autoreset=True)

menu()
clear_terminal()
player_name = welcome_message()
clear_terminal()
print(f"Welcome {player_name} to the Blackjack Game!")  

def main():
    """
    Main loop of the game, totalizing 5 rounds and display at the end a winner message.
    """
    total_round = 0
    player_round = 0
    dealer_round = 0
    tie_round = 0
    
    while total_round < 5: # total rounds 
        total_round += 1
         
        my_deck = Deck() # create a deck of cards (from my class Deck)
        
        player, dealer = create_players(player_name, my_deck)
        
        print("\nBlack Jack Game!!!")
        print("--------------------------------------------------------------------------------")
        display_hand(player, dealer) # function so show up player and dealer object with initial cards
        print("\n--------------------------------------------------------------------------------")
        
        stand_or_hit(player, dealer, my_deck) # plyer's turn, has to decide if Stand or Hit a new card
        
        display_player_hand(player)
        
        player_score = calculate_points(player['hand']) # calculate the player's score
        
        print("\nDEALER'S TURN!!!----------------------------------------------------------------\n")
        
        display_dealer_hand(dealer)
        
        time.sleep(4)
        
        dealer_turn(dealer, my_deck) # Function to call dealer's turn
        
        dealer_score = calculate_points(dealer['hand'])
        
        print("\n--------------------------------------------------------------------------------")
        print(f"Player's score: {player_score} points")
        print(f"Dealer's score: {dealer_score} points")
            
        time.sleep(4)
        
        winner_result = show_winner(player_score, dealer_score)
        
        print(winner_result)
        print("--------------------------------------------------------------------------------")
    
        if "YOU WIN" in winner_result:
            player_round += 1
        elif "DEALER WINS" in winner_result:
            dealer_round += 1
        elif "TIE" in winner_result:
            tie_round += 1
        
        time.sleep(3)
            
        print(f"Played a total of: {total_round} rounds.\n")
        print(f"Player round: {player_round}")
        print(f"Dealer round: {dealer_round}")
        print(f"Tie: {tie_round}")
        print("--------------------------------------------------------------------------------")
        
        time.sleep(5)
    
        clear_terminal()
    
    clear_terminal()
    
    print(f"\nPlayed a total of: {total_round} rounds.\n")
    print("--------------------------------------------------------------------------------")
    
    final_winner = result_final_winner(player_round, dealer_round)
    
    time.sleep(3)
        
    print(f"\nPlayer wins: Total of {player_round} rounds.")
    print(f"Dealer wins: Total of {dealer_round} rounds.")
    print(f"Tie: Total of {tie_round}.")
    
    time.sleep(3)
    
    print("\n------------------------------ The WINNER IS: ----------------------------------")
    
    time.sleep(4)
    
    if final_winner == "Player":
        print("\nYou're the WINNER!!\n")
        print("--------------------------------------------------------------------------------")
    elif final_winner == "Dealer":
        print("\nYou Lose!! DEALER WINS...\n")
        print("--------------------------------------------------------------------------------")
    else:
        print("\nIt's a tie!...\n")
        print("--------------------------------------------------------------------------------")
    
    time.sleep(4)
    
    clear_terminal()
    
    menu()



if __name__ == "__main__":
    main()