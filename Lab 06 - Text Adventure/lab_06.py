class Room:
    def __init__(self, description,north=0,east=0,south=0 ,west=0):
        self.Description=description
        self.North= north
        self.East= east
        self.South= south
        self.West= west


def main():
    done=False
    current_room = 0

    room0 = Room("You are standing on Longevity Hill. It is a well lit night from the full moon",
                 north=1,
                 east=5,
                 south=None,
                 west=3
                 )
    room1 = Room("You have walked onto the Seventeen Arch bridge. Lit by newly installed electric light.",
                 north=2,
                 east=None,
                 south=0,
                 west=None
                 )
    room2 = Room("You entered the Hall of Benevolence and Longevity it's stunning facades dimly lit by moonlight.",
                 north=None,
                 east=4,
                 south=1,
                 west=6,
                 )
    room3 = Room("You enter the holy Tower of Buddhist Incense, your nose fills with the thick smoke of incense.",
                 north=None,
                 east=0,
                 south=None,
                 west=None,
                 )
    room4 = Room("You walk upon a dock until you reach a small row boat, you paddle out to the tranquil Marble Boat",
                 north=None,
                 east=None,
                 south=None,
                 west=2
                 )
    room5 = Room(
        "You walk into the Garden of Harmonious Pleasures. This garden is the pinnacle of beauty and one of your favorite places in the palace.",
        north=None,
        east=None,
        south=None,
        west=5
        )
    room6 = Room("You enter the rear Pavilion of the hall of Serenity.",
                 north=None,
                 east=2,
                 south=None,
                 west=None
                 )

    room_list = [room0, room1, room2, room3, room4, room5, room6]
    print(room0)

    print ("The year is 1908 under the Qing Dynasty, you serve as a loyal eunuch under Emperor Guangxu.")
    print ("Our once mighty and feared Empire stands on the brink of collapse.")
    print("Your revered Emperor Guangxu has been held under house arrest by Dowager Cixi.")
    print("Something is afoot, you suspect conspiracy against your Emperor")
    print("You have your suspicions but must investigate further.")
    print("Tonight you tend to your duties at the summer Yingtai Palace, on Longevity Hill' where you overhear a woman's voice?")
    print("Talking softly she discussed her sinister plans to ensure the Emperor falls ill.")
    print("Time is short, you must find the conspirator and put and end to the plot and save the Qing Dynasty.")

    while not done:
        print(room_list[current_room].Description)





        user_choice=input("Where would you like to go? (north, south, east, west, or quit)").lower()
        if user_choice == "north" or "NORTH" or "N" or "n" or "North" and room_list[current_room].North is not None:
            current_room = room_list[current_room].North
            print("You moved North")
        elif user_choice == "east" and room_list[current_room].East is not None:
            current_room = room_list[current_room].North
            print("You moved East")

    print()


main()