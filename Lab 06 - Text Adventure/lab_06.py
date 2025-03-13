class Room:
    def __init__(self, description, north, east, south, west):
        self.Description=description
        self.north= north
        self.east= east
        self.south= south
        self.west= west


def main():
    done=False
    current_room = 0
    room_list = []
    #0
    room = Room("You are standing on Longevity Hill. It is a well lit night from the full moon",
                 north=1,
                 east=5,
                 south=None,
                 west=3
                 )
    room_list.append(room)
    #1
    room = Room("You have walked onto the Seventeen Arch bridge. Lit by newly installed electric light.",
                 north=2,
                 east=None,
                 south=0,
                 west=None
                 )
    room_list.append(room)
    #2
    room = Room("You entered the Hall of Benevolence and Longevity it's stunning facades dimly lit by moonlight.",
                 north=None,
                 east=4,
                 south=1,
                 west=6
                 )
    room_list.append(room)
    #3
    room = Room("You enter the holy Tower of Buddhist Incense, your nose fills with the thick smoke of incense.",
                 north=None,
                 east=0,
                 south=None,
                 west=None
                 )
    room_list.append(room)
    #4
    room = Room("You walk upon a dock until you reach a small row boat, you paddle out to the tranquil Marble Boat.",
                 north=None,
                 east=None,
                 south=None,
                 west=2
                 )
    room_list.append(room)
    #5
    room = Room(
        "You walk into the Garden of Harmonious Pleasures. This garden is the pinnacle of beauty and one of your favorite places in the palace.",
        north=None,
        east=None,
        south=None,
        west=5
        )
    room_list.append(room)
    #6
    room = Room("You enter the rear Pavilion of the hall of Serenity.",
                 north=None,
                 east=2,
                 south=None,
                 west=None
                 )
    room_list.append(room)


    print(room)

    print ("The year is 1908 under the Qing Dynasty, you serve as a loyal eunuch under Emperor Guangxu.")
    print()
    print ("Our once mighty and feared Empire stands on the brink of collapse.")
    print()
    print("Your revered Emperor Guangxu has been held under house arrest by Dowager Cixi.")
    print()
    print("Something is afoot, you suspect conspiracy against your Emperor")
    print()
    print("You have your suspicions but must investigate further.")
    print()
    print("Tonight you tend to your duties at the summer Yingtai Palace, on Longevity Hill' where you overhear a woman's voice?")
    print()
    print("Talking softly she discussed her sinister plans to ensure the Emperor falls ill.")
    print()
    print("Time is short, you must find the conspirator and put and end to the plot and save the Qing Dynasty.")
    print()

    while not done:
        print(room_list[current_room].Description)





        user_choice=input("Where would you like to go? (north, south, east, west, or quit) ").lower()
        if user_choice.lower() == "north" or user_choice.lower() == "n" and room_list[current_room].north is not None:
            current_room = room_list[current_room].north
            print("You moved North")

        elif user_choice.lower() == "east" or user_choice.lower() == "e" and room_list[current_room].east is not None:
            current_room = room_list[current_room].east
            print("You moved East")

        elif user_choice.lower() == "west" or user_choice.lower() == "w" and room_list[current_room].west is not None:
            current_room= room_list[current_room].west
            print("You moved West")

        elif user_choice.lower() == "south" or user_choice.lower() == "s" and room_list[current_room].south is not None:
            current_room= room_list[current_room].south
            print("You moved South")

        elif user_choice.lower() == "quit" or user_choice.lower() == "q":
            print("You quit the game goodbye!")
            done=True

        else:
            print("You cannot go that way.")

    print()


main()


# I plan to do more with this if I have the time and potentially make my final game out of this code. As of right now it is pretty empty