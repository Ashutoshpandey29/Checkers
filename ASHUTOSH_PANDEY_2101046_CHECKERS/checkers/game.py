import pygame
from .constants import *
from .gameboard import Board


class Game:
    # initialises all of its attributes
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win

    # This method UPDATE the game window with the current state of the game board and valid moves.
    def UPDATE(self):
        self.board.draw(self.win)
        self.drawValidMove(self.valid_moves)
        pygame.display.update()

    def _init(self):

        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    # This method is called when a player clicks on a square of the game board
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.FetchPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.FetchValidMoves(piece)
            return True
        return False

    # This method ResetBoards the game state to its default values.
    def ResetBoard(self):
        self._init(self)

    # This method switches the turn to the other player and ResetBoards the valid_moves attribute.
    def AlterTurns(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    # This method is called when the player tries to move the selected piece to a new square
    def _move(self, row, col):
        piece = self.board.FetchPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.AlterTurns()
        else:
            return False

        return True

    # This method draws red circles on the game board to indicate valid moves for the selected piece
    def drawValidMove(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    # This method returns the winner of the game. I
    def Winner_checkers(self):
        return self.board.Winner_checkers()

    def get_board(self):
        return self.board

    # defines the move of the AI
    def AI_move(self, board):
        self.board = board
        self.AlterTurns()
