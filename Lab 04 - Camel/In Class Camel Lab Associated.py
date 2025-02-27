from operator import truediv

done = False
while not done:

    quit = input("Do you want to quit?")
    if quit == "y":
        done = True
        break

    attack = input("Does your elf attack the dragon?")
    if attack == "y":
        print("Bad choice, you died.")
        done = True
        break

    if attack == "n":
        print("Good choice!")


