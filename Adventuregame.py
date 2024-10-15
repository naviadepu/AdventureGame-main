"""
WIT Gsu 
Adventure Game 2024
"""

#This the Introduction Function 
def intro():
    #This function helps u choose your name
    name = input("Enter what name would u like to chose for the cat:")
    print(name)
    print("Welcome to the Silly Cat Adventure Game!")
    print("OHH!! I see so your name is {}.".format(name)) 
    print("Your goal is to find legendary cat treasures.")
    input("Press Enter to start...")
    print("\nYou find yourself in your cozy cat bed, ready for the adventure!\n")
    #This line means that at the end of the function,it will play the next function
    choose_action()

def search_for_clues():
    print("\nYou start searching for clues around the house.")
    print("You sniff around the living room, the kitchen, and even the bathroom!")
    print("Suddenly, you find a mysterious map under the sofa!")
    print("It seems to lead to the legendary cat treasure.")
    print("You must follow this map!\n")
    theadventure()

def take_a_nap():
    print("\nYou decide to take a quick nap before the adventure.")
    print("Zzz... Zzz...")
    print("\nYou wake up feeling refreshed and ready for your adventure!\n")
    theadventure()

def meow_for_attention():
    print("\nYou let out a loud meow for attention.")
    print("Your human hears you and comes over to pet you.")
    print("You purr with contentment.\n")
    theadventure()

def choose_action():
    #While fucntion is like a loop, if there is no vaild choice the function will stay 
    while True:
        print("\nWhat do you want to do?")
        print("1. Look for clues around the house.\n")
        print("2. Take a nap before the adventure.\n")
        print("3. Meow loudly for attention.\n")
        choice = input("Enter the number of your choice (1, 2, or 3): ")

        if (choice == "1"):
            search_for_clues()
            break
        elif (choice == "2"):
            take_a_nap()
            break
        elif (choice == "3"):
            meow_for_attention()
            break
        else:
            print("Invalid choice. Try again.")

def theadventure():       
    while True:    
        print("\nAs you follow the map, you encounter a mischievous mouse!")
        print("Do you want to chase the mouse or ignore it?")
        chase_choice = input("Enter 'chase' or 'ignore': ")
        
        if (chase_choice.lower() == "chase"):
            print("\nYou give chase to the mouse, but it quickly scampers away.")
            print("Oh well, it was worth a try!")
            sillyadventure()
            break
                
        elif (chase_choice.lower()=='ignore'):
            print("You continue following the map")
            sillyadventure()
            break
        
        else:
            print("Please choose from the given option")         
        
def sillyadventure():     
    while True:      
        print("\nSuddenly, you hear a loud noise coming from the kitchen.")
        print("Do you investigate the noise or continue following the map?")
        investigate_choice = input("Enter 'investigate' or 'continue': ")
        
        if (investigate_choice.lower() == "investigate"):    
            print("\nYou cautiously approach the kitchen and find... your human making a sandwich!")
            print("You decide to beg for some tuna and get a tasty treat!")
            sillyevent()
            break
        
        elif(investigate_choice.lower()=="contiune"):
            print("You ignore the nosie and conitune on your adventure")
            sillyevent()
            break
        
        else:
                print("Please choose a correct option")
                

def sillyevent():
            print("\nWhile exploring, you stumble upon a friendly neighbor who offers you a bowl of milk!")
            print("Do you accept the milk or politely decline?")
            milk_choice = input("Enter 'accept' or 'decline': ")
            if (milk_choice.lower() == "accept"):
                print("\nYou happily lap up the milk, feeling grateful for the unexpected treat!")
            else:
                print("\nYou politely decline the milk and continue your adventure.")
                print("\nCongratulations! You've completed your adventure and found the legendary cat treasure. You return home triumphant, ready for your next silly adventure!")
                
                    
                    
def main():
    #Calling my functions in main 
    intro()
#Running my main function 
if (__name__ == "__main__"):
    main()
    
    
                        
