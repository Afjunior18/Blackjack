from blackj.rules_blackjack import rules_blackjack

def menu():
    while True:
        print("Wanna see the GAME RULES, press (1) or START GAME preesing (2)\n")
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
