import pygame
from .constants import *
from .piece import Piece


class Board:

    # initializes all the attributes of class Board
    def __init__(self):
        self.board = []
        self.white_left = self.black_left = 12
        self.white_king = self.black_kings = 0
        self.create_board()

    # creates a board consisting of 12 black and white pieces
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # draws squares and fills in with the respective colour
    def DrawSquares(self, win):
        win.fill(light)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, dark, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def FetchPiece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.Convert_to_king()
            if piece.color == BLACK:
                self.black_kings += 1
            if piece.color == WHITE:
                self.white_king += 1

    def draw(self, win):
        self.DrawSquares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # THE EVALUATION FUNCTION -- No.of pieces left + no of kings for each black and white- --------------------------------------------
    def evaluate(self):
        return self.black_left * 5 + self.black_kings * 4 - self.white_left * 5 - self.white_king * 4

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    # fetches different states for each piece
    def FetchValidMoves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == WHITE or piece.king:
            moves.update(self.MOVELEFT(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.MOVERIGHT(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == BLACK or piece.king:
            moves.update(self.MOVELEFT(row + 1, min(row + 3, ROWS), 1, piece.color, left))

            moves.update(self.MOVERIGHT(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    # function to traverse in right direction
    def MOVERIGHT(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self.MOVELEFT(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self.MOVERIGHT(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    # function to traverse in left direction
    def MOVELEFT(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self.MOVELEFT(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self.MOVERIGHT(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    # function to remove a piece when it has been captured
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.black_left -= 1

    # Function to declare the winner
    def Winner_checkers(self):
        if self.white_left <= 0:
            return "BLACK"
        elif self.black_left <= 0:
            return "WHITE"
        return None
