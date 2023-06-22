from .constants import *
import pygame


class Piece:

    # to maintain space between the piece and the square
    PADDING = 17
    OUTLINE = 3

    # initializes all the related attributes of piece
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == RED:
            self.direction = 1
        else:
            self.direction = -1
        self.x = 0
        self.y = 0
        self.CalculatePosition()

    # The move method updates the piece's row and column position and calls CalculatePosition to update its x and y position
    def move(self, row, col):
        self.row = row
        self.col = col
        self.CalculatePosition()

    # The draw method takes a win (window) argument and uses Pygame to draw the piece on the board
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height()))

    # calculates the position for each piece
    def CalculatePosition(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # The Convert_to_king method sets the king attribute to True.
    def Convert_to_king(self):
        self.king = True

    # The __repr__ method returns a string representation of the piece's color.
    def __repr__(self):
        return str(self.color)
