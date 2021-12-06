from .MyChessBoard import MyChessBoard
from Alpha_Beta import find_move
import chess

class Game:
    def __init__(self, com_color):
        self.board = MyChessBoard()
        self.com_color = com_color

    def get_move(self, move_from, move_to):
        if self.com_color != self.board.turn:
            if (move_from != 'null'):
                move = chess.Move(from_square=chess.parse_square(move_from),to_square=chess.parse_square(move_to))
            else:
                move = 'nomove'
            return find_move(self.board, move)
        else: return None

    def new_game(self, com_color):
        self.board.newgame()
        self.com_color = com_color