import chess
import sys
import numpy as np
sys.path.insert(0, './alpha_beta')
from Config import evaluate_piece,piece_value
# from .alpha_beta.Config import point

# print(sys.path)

class MyChessBoard:

    def __init__(self):
        self.board = chess.Board()

    def legal_moves(self):
        return self.board.legal_moves

    def push(self, move):
        return self.board.push_san(move.uci())

    def pop(self):
        return self.board.pop()

    def turn(self):
        return self.board.turn
    def check_end_game(self) :
        queens = 0
        minors = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece and piece.piece_type == chess.QUEEN:
                queens += 1
            if piece and (
                piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT
            ):
                minors += 1

        if queens == 0 or (queens == 2 and minors <= 1):
            return True

        return False

    def newgame(self):
        self.board = chess.Board()
    def evaluate_board(self):
        total = 0
        end_game = self.check_end_game()

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if not piece:
                continue
            value = piece_value[piece.piece_type] + evaluate_piece(piece,square,end_game)
            total += value if piece.color == chess.WHITE else -value

        return total
    def is_draw(self):
        if self.board.is_stalemate():
            print("statlemate")
            return True
        if self.board.is_fivefold_repetition():
            print("fivefold repetition")
            return True
        if self.board.is_seventyfive_moves():
            print("75 moves")
            return True
        if self.board.is_insufficient_material():
            print("Insufficient Material")
            return True
        return False

    def is_checkmate(self):
        # If There is checkmate then it will be TRUE else FALSE.It will be a boolean value.
        return self.board.is_checkmate()
