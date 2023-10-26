def welcome_message():
    print("Blackjack Game!\n")
    try:
        name = input("What is your player's name?\n")
        name = name.capitalize()
        if not name.isalpha():
            raise ValueError("Invalid input, Please enter letters only\n")
    except ValueError as e:
        print(e)
        while True:
            name = input("Please enter your name, 'letters only'\n")
            name = name.capitalize()
            if name.isalpha():
                break
    else:
        print(f"Welcome {name} to the Blackjack Game!\nLet's have fun...\n")

    return name
