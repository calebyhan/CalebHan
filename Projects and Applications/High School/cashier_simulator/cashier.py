import random


class Cashier:
    def __init__(self):
        self.line = 0
        self.speed = random.randint(10, 25)
        self.customers = []
