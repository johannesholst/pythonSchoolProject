import pygame

SCREEN_SIZE = WIDTH, HEIGHT = (900, 720)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Battle Sim")

background_colour = WHITE
screen.fill(background_colour)

pygame.display.flip()


def combat():
    from soldier import infantry

    print(infantry.morale)
combat()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

