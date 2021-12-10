from MyChessBoard import MyChessBoard
from Alpha_Beta import find_move
import chess

class Game:
    com_color = None
    def __init__(self):
        self.board = MyChessBoard()

    def get_move(self, move, promotion=''):
        if self.com_color != self.board.turn:
            move = chess.Move.from_uci(move+promotion)
            self.board.push(move)
            if self.board.board.is_checkmate:
                return 'HUMAN_WIN'
            if self.board.board.is_variant_draw:
                return 'DRAW'
            return find_move(self.board)
        else: return None

    def new_game(self, com_color):
        self.board.newgame()
        self.com_color = com_color
        if com_color:
            return find_move(self.board)
        return None

# game = Game()
# print(game.new_game(True))
