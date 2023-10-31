from blackj.messages import welcome_message, rules_blackjack

# Menu rules/start game --------------------------------------------------------------------------------

def menu():
    """
    Display menu options and handle user's choice.
    """
    while True:
        print("Would you like to check the GAME RULES, press (1) or START GAME press (2)?\n")
        start_game = 2
        rules_game = 1
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            rules_blackjack()
            break
        elif choice == "2":
            pass
            break
        else:
            print("Invalid Choice: Please choose '1' or '2'")