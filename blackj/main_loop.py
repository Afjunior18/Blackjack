def main_loop():
    """
    Main loop of the game, totaling 5 rounds to check at the end who's the winner.
    """
    total_round = 0
    player_points = 0
    dealer_ points = 0
    
    if total_round < 5: # total rounds 
        total_round += 1 
        my_deck = Deck() # create a deck of cards (from my class Deck)
        
        player, dealer = create_players(player_name, my_deck)
        