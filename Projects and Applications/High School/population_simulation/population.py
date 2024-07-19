import random

import person


class Population:
    def __init__(self, years, count, infant_mortality, youth_mortality, fertility_rate, disaster, fertility=None):
        if fertility is None:
            fertility = [18, 35]
        self.years = years
        self.count = count
        self.people = []
        self.infant_mortality = infant_mortality
        self.youth_mortality = youth_mortality
        self.fertility = fertility
        self.fertility_rate = fertility_rate
        self.pandemic = False
        self.disaster = disaster
        self.stats = {
            "population": [],
            # "infant_mortality": [],
            # "youth_mortality": [],
            # "fertility_rate": []
        }
        self._setup()

    def _stats(self):
        self.stats["population"].append(len(self.people))
        # self.stats["infant_mortality"].append(self.infant_mortality)
        # self.stats["youth_mortality"].append(self.youth_mortality)
        # self.stats["fertility_rate"].append(self.fertility_rate)

    def _setup(self):
        for i in range(self.count):
            self.people.append(person.Person(age=random.randint(0, 65)))
            if self.people[-1].gender == 1 and random.randint(0, 5) == 0:
                self.people[-1].pregnant = True

    def _reproduce(self):
        for human in self.people:
            if human.pregnant and self.infant_mortality < random.randint(0, 1000):
                human.pregnant = False
                for i in range(random.choices([1, 2, 3], cum_weights=(90, 7, 3))[0]):
                    self.people.append(person.Person())
            if human.gender == 1 and self.fertility[0] <= human.age <= self.fertility[1] and self.fertility_rate > random.randint(0, 100):
                human.pregnant = True

    def _run_year(self):
        if self.pandemic:
            del self.people[0:int(random.uniform(0.05, 0.2) * len(self.people))]
            if random.randint(0, 5) != 0:
                self.pandemic = False
        else:
            if random.randint(0, 1000) < 5:
                self.pandemic = True
        if self.disaster > random.randint(0, 100):
            del self.people[0:int(random.uniform(0.01, 0.2) * len(self.people))]
        for human in self.people:
            if human.age < 18 and self.youth_mortality > random.randint(0, 1000):
                self.people.remove(human)
            elif human.age < 80 and 2 > random.randint(0, 1000):
                self.people.remove(human)
            elif human.age >= 80 and ((5 * human.age) + 500) > random.randint(0, 1000):
                self.people.remove(human)
            else:
                human.age += 1
        self._reproduce()
        self._stats()

    def start(self):
        for i in range(self.years):
            self._run_year()

    def get_stats(self):
        return self.stats
