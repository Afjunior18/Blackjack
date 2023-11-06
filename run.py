import random
import time

from colorama import Fore, Back, Style, init
from art import *
from blackj.messages import welcome_message, rules_blackjack
from blackj.menu import menu
from blackj.gameplay import create_players, deal_cards, stand_or_hit
from blackj.deck import Deck
from blackj.utilities import clear_terminal
from blackj.gameplay import card_value_to_int, calculate_points, dealer_turn
from blackj.gameplay import result_final_winner, display_player_hand
from blackj.gameplay import display_dealer_hand, show_winner, display_hand


init(autoreset=True)

tprint("21AJ", font="block", chr_ignore=True)

menu()
clear_terminal()
player_name = welcome_message()
clear_terminal()
print(f"Welcome {player_name} to the Blackjack Game!")


def main():
    """
    Orchestrates the core game loop, conducting 5 rounds of play,
    and determining a final winner. Each round involves the following steps:
    1. Initializing the game deck and creating player and dealer objects.
    2. Displaying the current hands of both the player and dealer.
    3. Allowing the player to choose to hit or stand until
    player reach 15pts or more.
    4. Revealing the final hand of the player and
    calculating the player's score.
    5. Initiating the dealer's turn, where they draw cards until
    dealer reach 17 points or more.
    6. Displaying the final hand of the dealer and
    calculating the dealer's score.
    7. Determining the winner of the round and updating round statistics.
    After 5 rounds, the winner is declared based on the total rounds won
    by the player and dealer.
    Displays a good bye message and give the option to play again.
    """
    total_round = 0
    player_round = 0
    dealer_round = 0
    tie_round = 0

    while total_round < 5:

        total_round += 1

        my_deck = Deck()

        player, dealer = create_players(player_name, my_deck)

        print("\nBlack Jack Game!!!")
        print("-------------------------------------------------------------\n"
              "-------------------")

        display_hand(player, dealer)

        print("\n-----------------------------------------------------------\n"
              "---------------------")

        stand_or_hit(player, dealer, my_deck)

        print("\n-----------------------------------------------------------\n"
              "---------------------")
        print("\nFinal Player's hand:")

        display_player_hand(player)

        print("-------------------------------------------------------------\n"
              "-------------------")

        time.sleep(4)

        player_score = calculate_points(player['hand'])

        print("\nDEALER'S TURN!!!-------------------------------------------\n"
              "---------------------\n")

        display_dealer_hand(dealer)

        time.sleep(4)

        dealer_turn(dealer, my_deck)

        time.sleep(4)

        print("\n-----------------------------------------------------------\n"
              "---------------------")
        print("\nFinal Dealer's hand:\n")

        display_dealer_hand(dealer)

        print("\n-----------------------------------------------------------\n"
              "---------------------")

        time.sleep(3)

        dealer_score = calculate_points(dealer['hand'])

        print(f"Player's score: {player_score} points")
        print(f"Dealer's score: {dealer_score} points")

        time.sleep(4)

        winner_result = show_winner(player_score, dealer_score)

        print(winner_result)
        print("-------------------------------------------------------------\n"
              "-------------------")

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
        print("-------------------------------------------------------------\n"
              "-------------------")

        time.sleep(5)

        clear_terminal()

    clear_terminal()

    print(f"\nPlayed a total of: {total_round} rounds.\n")
    print("-----------------------------------------------------------------\n"
          "---------------")

    final_winner = result_final_winner(player_round, dealer_round)

    time.sleep(3)

    print(f"\nPlayer wins: Total of {player_round} rounds.")
    print(f"Dealer wins: Total of {dealer_round} rounds.")
    print(f"Tie: Total of {tie_round}.")

    time.sleep(3)

    print("\n------------------------------ The WINNER IS: -----------------\n"
          "-----------------")

    time.sleep(4)

    if final_winner == "Player":
        print("\nYou're the WINNER!!\n")
        print("-------------------------------------------------------------\n"
              "-------------------")
    elif final_winner == "Dealer":
        print("\nDEALER WINS...\n")
        print("-------------------------------------------------------------\n"
              "-------------------")
    else:
        print("\nIt's a tie!...\n")
        print("-------------------------------------------------------------\n"
              "-------------------")

    time.sleep(4)

    clear_terminal()

    print(f"{player_name}!\nThank you for playing!\n"
          "We hope you had a great time.\n"
          "Would you like to play again?\n"
          "Feel free to choose from the menu below.\n"
          "Goodbye and see you next time!")

    menu()


if __name__ == "__main__":
    main()