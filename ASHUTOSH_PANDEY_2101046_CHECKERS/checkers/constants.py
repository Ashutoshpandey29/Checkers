import pygame

# width and height of board
WIDTH, HEIGHT = 800, 800

# the size of rows and columns
ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)

# pieces
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# columns and rows
light = (0, 205, 205)  # light
dark = (0, 139, 139)  # dark

# shows moves
GREEN = (255, 0, 0)  # dots

# insert crown image
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
