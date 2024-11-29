import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    pygame.display.update()
