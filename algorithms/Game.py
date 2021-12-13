from .MyChessBoard import MyChessBoard
from Alpha_Beta import find_move as alpha_beta_find_move
import dqn_bot
from dqn_bot import find_move as dqn_find_move
import stockfish_bot
from stockfish_bot import find_move as stockfish_find_move

import chess

class Game:
    com_color = None
    bot_level = 0
    def __init__(self):
        self.board = MyChessBoard()

    def get_move(self, move_from='null', move_to='', promotion=''):
        if (move_from != 'null'):
            print(move_from + move_to + promotion)
            human_move = chess.Move.from_uci(move_from + move_to + promotion)
            self.board.push(human_move)
            if self.board.is_checkmate(): return 'HUMAN_WIN'
            if self.board.is_draw(): return 'DRAW'
        if self.bot_level == 1:
            return alpha_beta_find_move(self.board)
        elif self.bot_level == 2:
            return dqn_find_move(self.board)
        elif self.bot_level == 3:
            return stockfish_find_move(self.board)

    def new_game(self, com_color, level = 1):
        self.board.newgame()
        self.com_color = com_color
        self.bot_level = level
