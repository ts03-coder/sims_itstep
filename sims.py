import random

class Human:
    def __init__(self, name="Human", energy=100, mood=100, money=50):
        self.name = name
        self.energy = energy
        self.mood = mood
        self.money = money
        self.home = None # Поки персонаж без житла

    def info(self):
        if self.home:
            adress = self.home.adress
        else:
            adress = "Без житла"

        return f"{self.name}: Енергія: {self.energy} | Настрій: {self.mood} | Гроші: {self.money} | Дім: {adress}"

    def use(self, item):
        item.apply_to(self)

    def work(self):
        if self.energy < 30:
            print(f"{self.name} занадто втомлений(-а), щоб іти на роботу!")
            return

        self.energy -= 30
        self.mood -= random.randint(5, 10)
        self.money += random.randint(30, 59)

        print(f"{self.name} попрацював(-ла). Енергія: {self.energy}, гроші: {self.money}")

class Item:

    def __init__(self, name, energy=0, mood=0, price=0):
        self.name = name
        self.energy = energy
        self.mood = mood
        self.price = price

    def apply_to(self, human):
        if human.money < self.price:
            print(f"{human.name} не має грошей на {self.name}")
            return

        human.energy = self.energy
        human.mood = self.mood
        human.money -= self.price

        if human.energy > 100:
            human.energy = 100
        if human.mood > 100:
            human.energy = 100
        print(f"{human.name} використав(-ла) {self.name}. Енергія: {human.energy}, настрій: {human.mood}")