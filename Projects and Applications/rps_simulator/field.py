import random
import math
import object
import pygame


class Field:
    def __init__(self, length, width, n):
        self.length = length
        self.width = width

        self.objects = []
        for i in range(n):
            self.objects.append(object.Object(0, 0, 0, 0))

        self.setup()

    def setup(self):
        for obj in self.objects:
            obj.x = random.random() * self.length
            obj.y = random.random() * self.width
            obj.speed = (random.random() + 0.1) * 10
            obj.direction = random.random() * math.pi * 2

    def update(self):
        for obj in self.objects:
            obj.move()
            obj.bounce()
            obj.rect = pygame.Rect(obj.x, obj.y, obj.OBJECT_LENGTH, obj.OBJECT_WIDTH)

        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                if self.objects[i].collide(self.objects[j]):
                    self.objects[i].bounce(self.objects[j])
                    self.objects[j].bounce(self.objects[i])
