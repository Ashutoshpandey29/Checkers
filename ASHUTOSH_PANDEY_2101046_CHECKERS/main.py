import pygame
from checkers.constants import *
from checkers.gameboard import Board
from checkers.game import *
from alphabeta.algo import *
from alphabeta.algoWithoutPruning import *
import time

FPS = 55
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers-ASHUTOSH PANDEY 2101046')


# function to fetch the positions of pieces as x and y
def Fetch_pos_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# driver code
def main():
    run = True
    game = Game(WIN)
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        if game.Winner_checkers() != None:
            print(game.Winner_checkers())

        if game.turn == BLACK:
            start = time.time()
            value, new_board = AlphaBetaPruning(game.get_board(), float('-inf'), float('+inf'), 5, BLACK, game)
            game.AI_move(new_board)
            end = time.time()
            print("\nAI of this game took", end - start, end=" ")
            print("seconds in order to make a move\n")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = Fetch_pos_mouse(pos)
                game.select(row, col)
        game.UPDATE()
    pygame.quit()


main()
