user_name = input("What is your name?") or user_name.lower() == "john"
if user_name.lower() == "jack":
    print("You have a nice name.")
else:
    print("Your name is okay.")