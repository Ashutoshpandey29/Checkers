from copy import deepcopy
import pygame
from checkers.constants import *
from checkers import *


# the main algorithm used is alpha beta pruning The alpha and beta parameters represent
# the best known values for the maximizing and minimizing players respectively.

# During the search, if the alpha value becomes greater
# than or equal to the beta value, the search can be terminated early
def AlphaBetaPruning(position, alpha, beta, depth, max_player, game):
    if depth == 0 or position.Winner_checkers() != None:
        return position.evaluate(), position

    if max_player:
        evaluateMax = float('-inf')
        best_move = None
        for move in Fetchmoves(position, BLACK, game):
            evaluation = AlphaBetaPruning(move, alpha, beta, depth - 1, False, game)[0]
            # evaluateMax = max(evaluateMax, evaluation)
            if evaluation > evaluateMax:
                evaluateMax = evaluation
                best_move = move
            alpha = max(alpha, evaluateMax)
            # if evaluateMax == evaluation:
            if alpha >= beta:
                break

        return evaluateMax, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in Fetchmoves(position, WHITE, game):
            evaluation = AlphaBetaPruning(move, alpha, beta, depth - 1, True, game)[0]
            # minEval = min(minEval, evaluation)
            beta = min(beta, minEval)
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            if (beta <= alpha):
                break

        return minEval, best_move


# It returns a list of new game boards representing each possible move.
def Fetchmoves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.FetchValidMoves(piece)
        for move, skip in valid_moves.items():
            # draw_moves_on_board(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.FetchPiece(piece.row, piece.col)
            new_board = PerformMove(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def PerformMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


# This function draws the possible moves for a piece on the game board
def draw_moves_on_board(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
