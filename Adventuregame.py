"""
WIT Gsu
Adventure Game 2024
"""

def intro(): #def keyword is used to define a fucntion then followed by the name of the function, 
#parentheses to spcify any arguments, then a colon to indicate start of the function.
    name = input("Enter a name for the cat: ")
    print("Welcome to the Silly Cat Adventure Game, " + name + "!")
    #a plain string that concatnates the user's inputed name into the statement.
    input("Press Enter to start...\n")
    #pausing until something is given, in this case pressing the enter key
    choose_action()

def choose_action():
    while True:
        print("Choose an action:")
        print("1. Look for clues.")
        print("2. Take a nap.")
        print("3. Meow for attention.")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            search_for_clues()
            break
        elif choice == "2":
            take_a_nap()
            break
        elif choice == "3":
            meow_for_attention()
            break
        else:
            print("Invalid choice. Try again.")

def search_for_clues():
    print("\nYou find a mysterious map under the sofa!\n")
    theadventure()

def take_a_nap():
    print("\nYou take a quick nap and wake up refreshed.\n")
    theadventure()

def meow_for_attention():
    print("\nYou meow, and your human gives you a nice pet.\n")
    theadventure()


def theadventure():
    while True:
        print("\nYou encounter a mischievous mouse! Do you want to chase it or ignore it?")
        chase_choice = input("Enter 'chase' or 'ignore': ")
        
        if chase_choice.lower() == "chase":
            print("\nYou give chase, but the mouse gets away.")
            sillyadventure()
            break
        elif chase_choice.lower() == "ignore":
            print("\nYou ignore the mouse and decide to restart your adventure.")
            main()  # Restart the game
            break
        else:
            print("Please choose from the given options.")

def sillyadventure():
    while True:
        print("\nYou hear a noise from the kitchen. Investigate or continue?")
        investigate_choice = input("Enter 'investigate' or 'continue': ")
        
        if investigate_choice.lower() == "investigate":
            print("\nYou find your human making a sandwich and get a treat!")
            sillyevent()
            break
        elif investigate_choice.lower() == "continue":
            sillyevent()
            break
        else:
            print("Please choose a correct option.")

def sillyevent():
    print("\nYou find a neighbor offering a bowl of milk. Accept or decline?")
    milk_choice = input("Enter 'accept' or 'decline': ")
    if milk_choice.lower() == "accept":
        print("\nYou enjoy the milk!")
    else:
        print("\nYou politely decline.")
    print("\nCongratulations! You've completed your adventure!")

def main():
    intro()

if __name__ == "__main__":
    main()
