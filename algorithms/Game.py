from .MyChessBoard import MyChessBoard
from .alpha_beta.Alpha_Beta import find_move as alpha_beta_find_move

from .dqn.dqn_65.bot_65 import find_move as dqn_65_find_move
from .dqn.dqn_65.model65 import get_model65

from .dqn.dqn_888.model888 import get_model888
from .dqn.dqn_888.bot_888 import find_move as dqn_888_find_move

from .stockfish.stockfish_bot import find_move as stockfish_find_move
import chess

# %%
# model
model65 = get_model65(STATE_SHAPE= (65, ), NB_ACTIONS= 4096)
model888 = get_model888(STATE_SHAPE= (8, 8, 8), NB_ACTIONS= 4096)

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
            return dqn_65_find_move(self.board, model65)
        elif self.bot_level == 3:
            return dqn_888_find_move(self.board, model888)
        elif self.bot_level == 4:
            return stockfish_find_move(self.board)

    def new_game(self, com_color, level = 1):
        self.board.newgame()
        self.com_color = com_color
        self.bot_level = level
        
        if level == 2:
            model65.load_weights('chess_65_model.h5')

        if level == 3:
            model888.load_weights('superbot_888_model.h5')

    def undo_moves(self):
        self.board.pop()
        self.board.pop()