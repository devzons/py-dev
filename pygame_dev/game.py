import pygame

pygame.init()

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title
pygame.display.set_caption("Net Game")

# background
background = pygame.image.load("/Users/don/Projects/python/pygame_dev/background.png")

# event loop
running = True # keep game running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((20, 139, 215))
    screen.blit(background, (0, 0)) # draw background

    pygame.display.update() # keep drawing bg

# pygame close
pygame.guit()