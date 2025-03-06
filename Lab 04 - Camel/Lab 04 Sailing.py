import random


def main():
    # Variable Set
    miles_pirates_sailed = -90
    miles_sailed = 0
    rations_on_board=5
    crew_status= 100

    def half_sail_distance(half_sail_mode):
        if half_sail_mode == "B" or "b":  # Half Sail
            return random.randint(90, 100)
        return 0
    def full_sail_distance(full_sail_mode):
        if full_sail_mode == "C" or "c":  # Full Sail
            return random.randint(180, 300)
        return 0

    def distance_pirates_sail(sail_mode):
        if sail_mode == "B" or "b" or sail_mode == "C" or "c" or "D" or "d":
            return random.randint(21,300)
        return 0


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
        # Serve the Crew Rations
        if user_choice.upper() == "A":
            print("You order the chef to prepare rations for the crew. Crew morale improves.")
            rations_on_board  = rations_on_board - 1
            print("Remaining Rations",rations_on_board)

            crew_status = crew_status + random.randint(9, 24)
            print("Crew Morale:", crew_status)

        # Half Sail
        if user_choice.upper() == "B":
            print("The ships bell rings! You call out,\"Half-sail ahead men!\"")
            print("The crew hoists the main halyard and you watch the sails unfurl and fill with wind.")
            print("The ship leaps forward and begins sailing quickly.")
            distance = half_sail_distance(user_choice)
            miles_sailed += distance
            print("You sailed miles:", miles_sailed)
            pirate_distance = distance_pirates_sail(user_choice)
            miles_pirates_sailed += pirate_distance
            print("Caution pirates follow! They sailed miles:",miles_pirates_sailed)
            distance_apart = miles_sailed - miles_pirates_sailed

            if distance_apart > 0:
                print("You are ahead of the pirates by", distance_apart, "miles.")

            crew_status = crew_status - random.randint (9,24)
            print("Crew Morale:", crew_status)

       # Full Sail
        if user_choice.upper() == "C":
            print("The ships bell rings! You call out,\"full sail ahead men!\"")
            print("The crew hoists the main halyard and you watch the sails unfurl and fill with wind.")
            print("The ship leaps forward and begins sailing quickly.")
            distance = full_sail_distance(user_choice)
            miles_sailed += distance
            print("You sailed miles:", miles_sailed)
            pirate_distance = distance_pirates_sail(user_choice)
            miles_pirates_sailed += pirate_distance
            print("Caution pirates follow! They sailed miles:", miles_pirates_sailed)
            distance_apart = miles_sailed - miles_pirates_sailed

            if distance_apart > 0:
                print("You are ahead of the pirates by", distance_apart, "miles.")

            crew_status = crew_status - random.randint(19, 49)
            print("Crew Morale:", crew_status)

        # Check Status
        if user_choice.upper() == "E":
            print("My Status")
            print("Crew Morale:",crew_status)
            print("Number of Rations:",rations_on_board)
            print("Number of Miles Sailed:",miles_sailed)
            print("Number of Miles Pirates Sailed:",miles_pirates_sailed)
            distance_apart = miles_sailed - miles_pirates_sailed

            if distance_apart > 0:
                print("You are ahead of the pirates by", distance_apart, "miles.")

        if user_choice.upper() == "D":
            print("You sail into a small harbor on a passing island. You use company funds to resupply the ship.")
            rations_on_board = rations_on_board + 3
            print("Remaining Rations", rations_on_board)
            pirate_distance = distance_pirates_sail(user_choice)
            miles_pirates_sailed += pirate_distance
            print("You sailed miles:", miles_sailed)
            print("Caution pirates follow! They sailed miles:", miles_pirates_sailed)

        # Game Failure Status Player Quits
        elif user_choice.upper() == "Q":
            done=True
            print("You abandoned your voyage.")

        # Game Failure Status Pirates
        if miles_pirates_sailed >= miles_sailed:
            print("You failed to outrun the pirates! They will now butcher your crew and steal your cargo.")
            print("You lost the game, better luck next time!")
            done=True

       # Game Failure Status Morale
        if crew_status <= 0:
            print("You failed to keep your crew morale high enough.")
            print("They grew sick and tired of your leadership and threw you overboard!")
            print("You lost the game, better luck next time!")
            done = True

        # Game Victory Conditions
        if miles_sailed >= 1445:
            print("You made it to Bermuda!")
            print("You have sailed 1445 miles.")
            print("You and your crew are now safe from pirates!")
            print("You can now begin outfitting your ship for long voyage back to Holland.")
            print("Congratulations, you won the game! Good work capitan!")
            done = True

main()