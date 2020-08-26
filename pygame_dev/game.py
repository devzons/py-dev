import pygame

pygame.init()

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title
pygame.display.set_caption("Net Game")

# event loop
running = True # keep game running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame close
pygame.guit()