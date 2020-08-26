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

# call character (sprite)
character = pygame.image.load("/Users/don/Projects/python/pygame_dev/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# event loop
running = True # keep game running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos)) # draw character

    pygame.display.update() # keep drawing bg

# pygame close
pygame.guit()