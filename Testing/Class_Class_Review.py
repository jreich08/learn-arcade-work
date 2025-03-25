class Cat:
    def __init__(self):
        self.color = ""
        self.weight = ""

    def meow(self):
        print(self.name + " says \"meow!\"")

def main():
    my_cat = Cat()
    my_cat.name = "Milton"
    my_cat.color = "Tuxedo"
    my_cat.weight = 10
    my_cat.meow()

main()

