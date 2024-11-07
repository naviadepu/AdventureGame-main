"""
WIT Gsu
Adventure Game 2024
"""

def intro(): 
    # Defines the intro function
    name = input("Enter a name for the cat: ")
    print("Welcome to the Silly Cat Adventure Game, " + name + "!")
    # Concatenates the user's inputted name into the statement.
    input("Press Enter to start...\n")
    # Pauses until Enter is pressed
    choose_action()

def search_for_clues():
  print("\nYou find a mysterious map under the sofa!\n")
  theadventure()

def take_a_nap():
  print("\nYou take a quick nap and wake up refreshed.\n")
  theadventure()

def meow_for_attention():
  print("\nYou meow, and your human gives you a nice pet.\n")
  theadventure()

def choose_action():
    while True:
        print("Choose an action:")
        print("1. Search for clues.")
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


def theadventure():
    while True:
        print("\nYou encounter a mischievous mouse! Do you want to chase it or ignore it?")
        chase_choice = input("Enter 'chase' or 'ignore': ")

        if chase_choice.lower() == "chase":
            print("\nYou give chase, but the mouse gets away.")
            end_adventure()
            break
        elif chase_choice.lower() == "ignore":
            print("\nYou ignore the mouse and continue exploring.")
            end_adventure()
            break
        else:
            print("Please choose from the given options.")

def end_adventure():
    print("\nYou meet a friendly neighbor who offers you a bowl of milk. Accept or decline?")
    milk_choice = input("Enter 'accept' or 'decline': ")
    if milk_choice.lower() == "accept":
        print("\nYou happily lap up the milk and feel refreshed for more adventures!")
    else:
        print("\nYou politely decline and return home feeling content.")
    print("\nCongratulations! You've completed your adventure!")

def main():
    intro()

if __name__ == "__main__":
    main()

