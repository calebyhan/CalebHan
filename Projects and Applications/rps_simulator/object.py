import math
import random
import pygame


class Object:
    OBJECT_LENGTH = 20
    OBJECT_WIDTH = 20

    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.obj_type = random.choices(["rock", "paper", "scissor"])[0]
        self.rect = pygame.Rect(self.x, self.y, self.OBJECT_LENGTH, self.OBJECT_WIDTH)
        self.image = pygame.transform.scale(pygame.image.load("imgs/" + self.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def collide(self, check):
        if self.rect.colliderect(check.rect):
            if self.obj_type == "rock" and check.obj_type == "paper":
                self.obj_type = "paper"
                self.image = pygame.transform.scale(pygame.image.load("imgs/" + self.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            elif self.obj_type == "paper" and check.obj_type == "scissor":
                self.obj_type = "scissor"
                self.image = pygame.transform.scale(pygame.image.load("imgs/" + self.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            elif self.obj_type == "scissor" and check.obj_type == "rock":
                self.obj_type = "rock"
                self.image = pygame.transform.scale(pygame.image.load("imgs/" + self.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            elif self.obj_type == "paper" and check.obj_type == "rock":
                check.obj_type = "paper"
                check.image = pygame.transform.scale(pygame.image.load("imgs/" + check.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            elif self.obj_type == "scissor" and check.obj_type == "paper":
                check.obj_type = "scissor"
                check.image = pygame.transform.scale(pygame.image.load("imgs/" + check.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            elif self.obj_type == "rock" and check.obj_type == "scissor":
                check.obj_type = "rock"
                check.image = pygame.transform.scale(pygame.image.load("imgs/" + check.obj_type + ".png"), (self.OBJECT_LENGTH, self.OBJECT_WIDTH))
            return True

    def bounce(self, bounced=None):
        if self.x < 0:
            self.x = 0
            self.direction = math.pi - self.direction
        elif self.x > 500 - self.OBJECT_LENGTH:
            self.x = 500 - self.OBJECT_LENGTH
            self.direction = math.pi - self.direction

        if self.y < 0:
            self.y = 0
            self.direction = 2 * math.pi - self.direction
        elif self.y > 500 - self.OBJECT_WIDTH:
            self.y = 500 - self.OBJECT_WIDTH
            self.direction = 2 * math.pi - self.direction

        if bounced is not None:
            self.direction = math.atan2(self.y - bounced.y, self.x - bounced.x)
            bounced.direction = math.atan2(bounced.y - self.y, bounced.x - self.x)

            temp = self.speed
            self.speed = bounced.speed
            bounced.speed = temp
