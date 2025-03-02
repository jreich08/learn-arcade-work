import random

from pycparser.c_ast import Break


# This should provide a randomly generated travel distance

#def get_travel_distance_capitan_half_sail(half_sail_mode):
    #if half_sail_mode =="B": # Half Sail
        #return random.randint(90,100)

#def get_travel_distance_capitan_full_sail(full_sail_mode):
    #if full_sail_mode == "C": #Full Sail
        #return random.randint(180,300)

def main():
    # Variable Set
    miles_pirates_sailed = -20
    miles_sailed = 0
    rations_on_board=5
    ship_status=100
    def half_sail_distance(half_sail_mode):
        if half_sail_mode == "B":  # Half Sail
            return random.randint(90, 100)

    def full_sail_distance(full_sail_mode):
        if full_sail_mode == "C":  # Full Sail
            return random.randint(180, 300)

    def distance_pirates_sail(sail_mode):
        if sail_mode == "B" or sail_mode == "C":
            return random.randint(21,300)

    # Introduction to the Game
    print("Welcome to Full Sail!")
    print("The year is 1657 and you are a merchant Capitan for the lucrative Dutch West India Company")
    print("Word has spread to Port Royal that your ship carries a valuable haul of sugar and tobacco from Aruba.")
    print("Pirates lurk on the horizon, eager to claim their prize and make a fortune.")
    print("You must carefully manage your ship and crew to avoid pirate capture and crew mutiny.")
    print("You must sail 1,445 miles to safety in Freeport Bermuda, from their you can rest and resupply.")
    print("Can you escape the Caribbean to set sail for Holland?")


    # First Player Prompting
    done=False
    while not done:
        print("A.Serve Crew Rations.")
        print("B.Ahead Half Sail.")
        print("C.Ahead Full Sail.")
        print("D.Find a Port to Rest and Restock")
        print("E. Status check.")
        print("Q.Quit.")
        user_choice = input("What is your choice? ")

    # Defining What Each Response Means
        if user_choice.upper() == "A":
            rations_on_board  = rations_on_board - 1
        print("Remaining Rations",rations_on_board)

        if user_choice.upper() == "B":
            print("The ships bell rings! You call out,\"full sail ahead men!\"")
            print("The crew hoists the main halyard and you watch the sails unfurl and fill with wind.")
            print("The ship leaps forward and begins sailing quickly.")
            distance = half_sail_distance(user_choice)
            miles_sailed += distance
            print("You sailed miles:", miles_sailed)
            pirate_distance = distance_pirates_sail(user_choice)
            miles_pirates_sailed += pirate_distance
            print("Caution pirates follow! They sailed miles:",miles_pirates_sailed)


        if user_choice.upper() == "E":
            print("My Status")
            print("Ship Integrity:",ship_status)
            print("Number of Rations:",rations_on_board)
            print("Number of Miles Sailed:",miles_sailed)
            print("Number of Miles Pirates Sailed:",miles_pirates_sailed)


        elif user_choice.upper() == "Q":
            done=True
            print("You abandoned your voyage.")

main()