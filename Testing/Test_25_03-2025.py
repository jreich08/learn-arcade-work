def give_money2(person):
    person.money += 100

    class Person:
        def __init__(self):
            self.name = ""
            self.money = 0

def main():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    give_money2(bob)
    print(bob.money)


main()
