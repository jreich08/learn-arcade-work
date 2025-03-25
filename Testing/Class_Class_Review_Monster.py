import random


class Monster:
    def __init__(self):
        self.name = ""
        self.health = 100
    def decrease_health(self, lost_health):
        self.health  -= lost_health
        if self.health < 1:
            print("Your monster has died!")
        else:
            print(self.health, "is your monsters health")

def main():
    my_monster = Monster()
    my_monster.name = "Mean Monster"
    my_monster.decrease_health(random.randrange(110))

main()
