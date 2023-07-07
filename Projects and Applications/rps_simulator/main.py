import field
import pygame

LENGTH = 500
WIDTH = 500

game = field.Field(LENGTH, WIDTH, 50)

pygame.init()
screen = pygame.display.set_mode((LENGTH, WIDTH))

pygame.display.set_caption("Rock Paper Scissors")

font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()

    screen.fill((255, 255, 255))
    for obj in game.objects:
        screen.blit(obj.image, (obj.x, obj.y))
    pygame.display.flip()

    clock.tick(60)
