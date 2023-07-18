import pygame
import pygame_gui
import world
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BOX_WIDTH = 800
BOX_HEIGHT = 800
BOX_X = (SCREEN_WIDTH - BOX_WIDTH) // 2
BOX_Y = (SCREEN_HEIGHT - BOX_HEIGHT) // 2
CELL_SIZE = 10

game = world.World(BOX_WIDTH // CELL_SIZE, BOX_HEIGHT // CELL_SIZE)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Conway's Game of Life")

pygame.freetype.init()
gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

speed_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((10, 10), (150, 30)),
    start_value=5,
    value_range=(1, 10),
    manager=gui_manager
)

clear_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((170, 50), (150, 30)),
    text="Clear",
    manager=gui_manager
)

percent_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((170, 10), (150, 30)),
    manager=gui_manager,
)

start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 50), (150, 30)),
    text="Start",
    manager=gui_manager
)

clock = pygame.time.Clock()
running = True
start_simulation = False
percent_input.set_text("10")


def toggle_tile_state(x, y):
    grid_x = (x - BOX_X) // CELL_SIZE
    grid_y = (y - BOX_Y) // CELL_SIZE
    if 0 <= grid_x < game.x and 0 <= grid_y < game.y:
        game.tiles[grid_x][grid_y].state = not game.tiles[grid_x][grid_y].state


def clear_and_randomize():
    game.clear()
    percent = float(percent_input.get_text())
    for i in range(game.x):
        for j in range(game.y):
            game.tiles[i][j].state = random.random() < (percent / 100)


while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    start_simulation = not start_simulation
                elif event.ui_element == clear_button:
                    clear_and_randomize()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if BOX_X <= event.pos[0] <= BOX_X + BOX_WIDTH and BOX_Y <= event.pos[1] <= BOX_Y + BOX_HEIGHT:
                    toggle_tile_state(event.pos[0], event.pos[1])

        gui_manager.process_events(event)

    game_speed = int(speed_slider.get_current_value())
    if start_simulation:
        game_speed = 11 - game_speed
        if game_speed < 1:
            game_speed = 1

        for _ in range(game_speed):
            game.run()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (BOX_X - 1, BOX_Y - 1, BOX_WIDTH + 2, BOX_HEIGHT + 2), 1)

    for i in range(game.x):
        for j in range(game.y):
            if game.tiles[i][j].state:
                pygame.draw.rect(screen, (255, 255, 255), (BOX_X + i * CELL_SIZE, BOX_Y + j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    gui_manager.update(dt)
    gui_manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()