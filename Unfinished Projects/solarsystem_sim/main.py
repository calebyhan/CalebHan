import math
import random
import pygame

WIDTH, HEIGHT = 1200, 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Solar System")

CX, CY = WIDTH / 2, HEIGHT / 2
CAMX, CAMY = 0, 0

G = 6.67428e-11
ZOOM = 8e-10
TIMESTEP = 86400

OBJECTS = []


class Resources:
    font = pygame.font.SysFont('Consolas', 12)
    space_image = pygame.transform.scale(
        pygame.image.load("imgs/space.png").convert(),
        (WIDTH, WIDTH)
    )


class Object:
    def __init__(self, name, mass, x, y, r, c=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 vx=0.0, vy=0.0):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.vx = vx
        self.vy = vy

        OBJECTS.append(self)

    def vel(self):
        return math.sqrt(self.vx**2 + self.vy**2)

    def draw(self, zoom):
        x = CX + self.x * zoom
        y = CY + self.y * zoom
        pygame.draw.circle(screen, self.c, (x, y), self.r)


class Info:
    def __init__(self, sim):
        self.info = sim

    @staticmethod
    def draw(self):
        topleft_texts = []
        y = 0
        for _text in topleft_texts:
            y += 20
            text = Resources.font.render(_text, False, (255, 255, 255))
            screen.blit(text, (20, y))

        text = Resources.font.render("Zoom: " + str(ZOOM), False, (225, 225, 225))
        rect = text.get_rect()
        rect.bottomleft = (20, HEIGHT - 20)
        screen.blit(text, rect)


class Simulation:
    def __init__(self):
        self.info = Info(self)
        Object("Sun", 1.9891e30, 0, 0, 695e6, vx=1e3, vy=1e3)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            # rect = Resources.space_image.get_rect()
            # rect.center = WIDTH/2, HEIGHT/2
            # screen.blit(Resources.space_image, rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for obj in OBJECTS:
                obj.draw(1e-100)

            pygame.display.flip()
            clock.tick(60)


Simulation().run()
