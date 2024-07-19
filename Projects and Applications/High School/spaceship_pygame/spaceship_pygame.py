'''
Spaceship pygame
Author: Caleb Han
'''

# imports
import pygame
import random

# get keystrokoes
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# set up player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((225, 225, 225))
        self.rect = self.surf.get_rect()
    
    # move the player
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# set up enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # move enemy
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# run game
pygame.init()

# set up a clock
clock = pygame.time.Clock()

# set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# add an enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# add player
player = Player()

# set up variables
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# get main running loop
running = True
while running:
    # quit game or add enemy events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # get pressed keys and move
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    
    # move enemies
    enemies.update()
    
    # screen manipulation
    screen.fill((0, 0, 0))
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))

    # sprite manipulation
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # detect collision
    if pygame.sprite.collideandy(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(1)
