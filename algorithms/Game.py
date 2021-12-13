from .MyChessBoard import MyChessBoard
from Alpha_Beta import find_move
import chess

class Game:
    com_color = None
    def __init__(self):
        self.board = MyChessBoard()

    def get_move(self, move_from='null', move_to='', promotion=''):
        if (move_from != 'null'):
            print(move_from + move_to + promotion)
            human_move = chess.Move.from_uci(move_from + move_to + promotion)
            self.board.push(human_move)
            if self.board.is_checkmate(): return 'HUMAN_WIN'
            if self.board.is_draw(): return 'DRAW'
        return find_move(self.board)

    def new_game(self, com_color):
        self.board.newgame()
        self.com_color = com_color
