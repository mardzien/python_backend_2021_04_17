
class Warrior:

    def __init__(self, name, strength, endurance):

        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.inventory = []
        self.equipment = []

    def pick_item(self, item):
        self.inventory.append(item)


class Item:

    def __init__(self, name, bonus_strength, bonus_endurance):
        self.name = name
        self.bonus_strength = bonus_strength
        self.bonus_endurance = bonus_endurance


class Board:

    def __init__(self, x, y, x_range, y_range):
        self.x = x
        self.y = y
        self.x_range = x_range
        self.y_range = y_range

    def go_up(self):
        self.y += 1

        if self.y > self.y_range:
            print("Jesteś poza planszą, koniec gry!")
            exit()

    def go_down(self):
        self.y -= 1

        if self.y < 1:
            print("Jesteś poza planszą, koniec gry!")
            exit()

    def go_right(self):
        self.x += 1

        if self.x > self.x_range:
            print("Jesteś poza planszą, koniec gray!")
            exit()

    def go_left(self):
        self.x -= 1

        if self.x < 1:
            print("Jesteś poza planszą, koniec gray!")
            exit()
