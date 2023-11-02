from blackj.messages import welcome_message, rules_blackjack

# Menu rules/start game --------------------------------------------------------------------------------

def menu():
    """
    Display menu options and handle user's choice.
    """
    while True:
        print("\n------- Game Menu -------")
        print("\n1 - Rules")
        print("\n2 - Start the game")
        print("\n3 - Exit\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            rules_blackjack()
        elif choice == "2":
            pass
            break
        elif choice == "3":
            exit()
        else:
            print("Invalid Choice: Please choose '1', '2' or '3'")
            
