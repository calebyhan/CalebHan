import random
import numpy as np

DEBUG = True


class Sim:
    """
        0: 2 lanes straight (a, b)
        1: 2 lanes left, 2 lanes right (a, b)
        2: 1 lane all (a, b, c, d)
    """

    POSSIBLE_ACTIONS = ["0a", "0b", "1a", "1b", "2a", "2b", "2c", "2d"]

    def __init__(self, time):
        self.roads = []
        self.action = None
        self.time = time
        self.t = 0
        self.fill_roads()

    def fill_roads(self):
        for i in range(4):
            self.roads.append(Road(self.t))

    def idle(self):
        idle = 0
        for road in self.roads:
            for car in road.cars:
                idle += car.idle
        return idle

    def sample(self):
        return random.choice(self.POSSIBLE_ACTIONS)

    def unpack(self):
        ret = []
        for road in self.roads:
            ret_road = []
            for car in road.cars:
                ret_road.append([car.position, car.idle, car.turn, car.speed, car.acceleration])
            ret.append(ret_road)

        max_arrays = max(len(sub) for sub in ret)
        padded_ret = ret + [[]] * (max_arrays - len(ret))

        if DEBUG:
            print(padded_ret)

        ret = np.array(padded_ret)

        if DEBUG:
            print(ret)
        return ret

    def step(self, light):
        self.action = light
        for road in self.roads:
            road.run()

        if DEBUG:
            print("Road 1: ", self.roads[0])
            print("Road 2: ", self.roads[1])
            print("Road 3: ", self.roads[2])
            print("Road 4: ", self.roads[3])

        self.t += 1
        return self.unpack(), self.idle(), self.t == self.time

    def reset(self):
        self.t = 0
        self.roads = []
        self.fill_roads()
        return self.unpack()


class Road:
    def __init__(self, t):
        self.cars = []
        self.t = t
        self.x = self.create_events()
        self.signal = False

    @staticmethod
    def create_events():
        x = np.linspace(0, 200, 1000)

        frequency = 0.1
        amplitude = 1
        sin_wave = amplitude * np.sin(2 * np.pi * frequency * x)

        noise_amplitude = random.random()
        noise = noise_amplitude * np.random.randn(len(x))
        noisy_sin_wave = sin_wave + noise

        return noisy_sin_wave

    def run(self):
        if random.random() < abs(self.x[self.t]):
            self.add_car()

        for car in self.cars:
            if car.move(self.signal) == -1:
                self.cars.remove(car)

    def add_car(self):
        self.cars.append(Car())

    def __str__(self):
        return f"{self.cars}"


class Car:
    """
        0: left
        1: right
        2: straight
    """
    MAX_ACCELERATION = 1
    MAX_SPEED = 2

    def __init__(self):
        self.speed = 0
        self.acceleration = 0
        self.position = 0
        self.idle = 0
        self.turn = random.choices([0, 1, 2], [0.1, 0.1, 0.8])[0]

    def move(self, signal):
        if self.speed < self.MAX_SPEED:
            self.acceleration = self.MAX_ACCELERATION
        else:
            self.acceleration = 0

        self.speed += self.acceleration
        self.position += self.speed

        if self.position >= 50:
            self.idle = 1
            self.position = 50

        if self.idle >= 1 and signal:
            return -1

        if self.idle >= 1:
            self.idle += 1

    def __str__(self):
        return f"{self.position} {self.idle} {self.turn}"
