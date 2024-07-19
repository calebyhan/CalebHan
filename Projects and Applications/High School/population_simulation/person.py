import random


class Person:
    def __init__(self, age=0):
        self.age = age
        self.gender = random.choice([0, 1])
        self.pregnant = False
