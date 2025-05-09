
"""______1______PRINT LAST AND FIRST NAME________________"""
#user_name = input("What is your first and last name?") or user_name.lower() == "john"

#def main():
#    print(user_name)

#main()
"""____________PRINT LAST AND FIRST NAME CODE___________"""


"""______2____DRAW A CHICKEN____________________________"""
#print(" /\"\"\\            '  ")
#print("<>^  L__________/ |")
#print(" `) /`     '     /")
#print("  \\ ` ___'      /")
#print("   ` \'\" ; \\ )`")
#print("         _/_Y")
"""___________DRAW A CHICKEN____________________________"""


"""_____3_____PRINT NUMBERS 100 TO 200_________________ """
#def number_print():
#    i = 200
#    while i >= 100:
#        print(i)
#        i -= 1

#number_print()
"""___________PRINT NUMBERS 100 TO 200_________________ """

"""___4__FOR LOOP PRINT NUMBERS 1 TO 50 (INCLUSIVE)____ """
#for i in range(51):
#    print(i)
"""______FOR LOOP PRINT NUMBERS 1 TO 50 (INCLUSIVE)____ """

"""___5__WRITE CODE USING TWO NESTED "FOR LOOPS THAT WILL OUTPUT THE FOLLOWING____"""
# Loop from 10 down to 1 (this controls the number of columns per row)
#for i in range(10, 0, -1):  # i starts at 10 and decreases to 1
    # Loop from 0 up to (but not including) i
#    for j in range(i):  # this controls how many numbers to print on each line
#        print(j, end=" ")  # print the number j on the same line, followed by a space
#    print()  # after finishing one row, move to the next line
"""______WRITE CODE USING TWO NESTED "FOR LOOPS THAT WILL OUTPUT THE FOLLOWING____"""

"""___6__CREATE A FUNCTION THAT TAKES TWO NUMBERS AND RETURNS THE LARGEST_________"""

#def return_largest(a, b):
    #if a > b:
        #return a
    #else:
        #return b

# Call the function with two numbers and print the result
#print(return_largest(5, 10))
"""______CREATE A FUNCTION THAT TAKES TWO NUMBERS AND RETURNS THE LARGEST_________"""

"""____7_CREATE A RECURSIVE FUNCTION THAT TAKES A STRING AND PRINTS BACKWARDS_____"""

#def print_backwards(string):
#    if len(string)>1:
#        print_backwards(string[1:])
#    print(string[0], end="")

#print_backwards("mushroom")

"""______CREATE A RECURSIVE FUNCTION THAT TAKES A STRING AND PRINTS BACKWARDS_____"""

"""____8__________WRITE CODE TO PRINT FIRST AND LAST VALUES________________________"""

#list = [55,41,52,68,45,27,40,25,37,26]

#print("First value:", list[0])
#print("Last value:", list[-1])

"""_______________WRITE CODE TO PRINT FIRST AND LAST VALUES________________________"""

"""_________9_____Classes and Objects______________________________________________"""
"""_________a_____WHAT DOES THE FOLLOWING LIND OF CODE DO?__________________________"""
#class Cat(Animal):
#This creates a Cat class that gets all the methods from the Animal class.
"""_______________WHAT DOES THE FOLLOWING LIND OF CODE DO?__________________________"""

"""__________b___WHAT DOES THE FOLLOWING LINE OF CODE DO?__________________________"""
#def__init__(self):
#    Animal.__init__(self)
#This sets up the child class and makes sure the Animal class is also set up correctly.
"""______________WHAT DOES THE FOLLOWING LINE OF CODE DO?__________________________"""
# This class is called Animal. It has:
# - one attribute: name (set when you create the object)
# - one method: speak(), which prints a message using the name
#BELOW IS THE CODE
"""___________C__WRITE CODE THAT CREATES A CLASS CALLED ANIMAL GIVE IT ONE ATTRIBUTE AND ONE METHOD___________"""
class Animal:
    def __init__(self, name):
        self.name = name  #Name is the attribute

    def speak(self):
        print(f"{self.name} makes a sound.")  # This is the method

"""______________WRITE CODE THAT CREATES A CLASS CALLED ANIMAL GIVE IT ONE ATTRIBUTE AND ONE METHOD___________"""
# This class is called Cat. It inherits from Animal.
# It has its own version of the speak() method.
# Below that, we create a Cat object named "Whiskers" and call the speak() method.
#BELOW IS THE CODE
"""_________D_____WRITE CODE THAT CREATES AN INSTANCE OF CAT. SET THE ATTRIBUTE AND CALL THE METHOD___________"""
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow.")
# Create an instance of Cat and call the method
my_cat = Cat("Whiskers")
my_cat.speak()

