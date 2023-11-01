import os

# Clear terminal -----------------------------------------------------------

def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

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

