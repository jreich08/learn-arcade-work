import random

# The line below will "roll the die" 20 times.
# Don't copy this 'for' loop into your program
# It is just here so we can try this example over and over
for i in range(20):


        if random.randrange(5) == 0:
            print("DRAGON!!")
        else:
            print("No Dragon.")

