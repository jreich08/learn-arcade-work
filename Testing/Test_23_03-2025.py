class Dog:
    def __init__(self):
        self.age=0
        self.name=""
        self.weight=0

    def bark(self):
        print(self.name + " says \"Woof\"!")

#Instantisating the Dog object      
my_dog = Dog ()

my_dog.name = "Spot"
my_dog.weight = 20
my_dog.age = 3