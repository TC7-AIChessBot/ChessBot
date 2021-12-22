import chess
import sys
import numpy as np
sys.path.insert(0, './alpha_beta')
from Config import evaluate_piece,piece_value
# from .alpha_beta.Config import point

# print(sys.path)

class MyChessBoard:
    mapped = {
            'P': 10,     # White Pawn
            'p': -10,    # Black Pawn
            'N': 20,     # White Knight
            'n': -20,    # Black Knight
            'B': 30,     # White Bishop
            'b': -30,    # Black Bishop
            'R': 40,     # White Rook
            'r': -40,    # Black Rook
            'Q': 50,     # White Queen
            'q': -50,    # Black Queen
            'K': 900,     # White King
            'k': -900     # Black King
    }

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

    def newgame(self):
        self.board = chess.Board()

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
    def convert_board_to_int(self):
        epd_string = self.board.epd()
        list_int = np.empty((0, ))
        for i in epd_string:
            if i == " ":
                list_int = list_int.reshape((8, 8))
                return list_int
            elif i != "/":
                if i in self.mapped:
                    list_int = np.append(list_int, self.mapped[i])
                else:
                    for counter in range(0, int(i)):
                        list_int = np.append(list_int, 0)
        list_int = list_int.reshape((8, 8))
        return list_int

    def get_state(self) -> np.ndarray:
        return np.append(self.convert_board_to_int().reshape(64,), self.board.turn * 2 - 1)

    def encodeMove(self, move_uci:str):
        if len(move_uci) != 4:
            raise ValueError()
        a, b = chess.parse_square(move_uci[:2]), chess.parse_square(move_uci[2:])
        return a * 64 + b

    def decodeMove(self, move_int:int):
        a, b = move_int//64, move_int%64
        # a, b = chess.square_name(a), chess.square_name(b)

        move = self.board.find_move(from_square= a,to_square= b)
        return move
