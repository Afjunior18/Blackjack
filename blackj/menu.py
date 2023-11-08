from art import *
from blackj.messages import welcome_message, rules_blackjack
from blackj.utilities import clear_terminal

# library used to colorize
from colorama import Fore, Back, Style, init
init(autoreset=True)


# Menu rules/start game -------------------------------------------------------


def menu():
    """
    Display menu options and handle user's choice.
    """
    while True:
        print(Fore.BLUE + "----------------------------------- Menu -------"
              "--------------------------------")
        print(Fore.BLUE + "       1 - Rules            2 - Start the game    "
              "   3 - Exit        ")
        print(Fore.BLUE + "---------------------------------------------------"
              "-----------------------------")

        choice = input(Fore.BLUE + "Enter your choice: ")

        if choice == "1":
            clear_terminal()
            rules_blackjack()
        elif choice == "2":
            pass
            break
        elif choice == "3":
            tprint("Good-bye!")
            exit()
        else:
            print(Fore.RED + "\nInvalid Choice: Please choose"
                  "'1', '2' or '3'\n")
