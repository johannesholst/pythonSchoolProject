import pygame

(width, height) = 1000, 800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Battle Sim")

background_colour = (255, 255, 255)
screen.fill(background_colour)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False