def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print ("Survive your desert trek and out run the natives.")



    done = False
    while not done:
        print("A. drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead Full Speed.")
        print("D. Stop for the Night")
        print("E. Status check.")
        print("Q.Quit.")
        break
    user_choice = input("What is your choice? ")

    if user_choice.upper() == "Q":
            done =True
            print("OK, game over.")







main()

