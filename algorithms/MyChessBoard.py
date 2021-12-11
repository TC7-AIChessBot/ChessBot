import chess
import sys

sys.path.insert(0, './alpha_beta')
from Config import point
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

    def fit(self):
        if self.board.is_checkmate():
            if self.board.turn:
                return -9999
            else: return 9999 
            
        fen = self.board.board_fen()

        fen = fen.replace('2','11')
        fen = fen.replace('3','111')
        fen = fen.replace('4','1111')
        fen = fen.replace('5','11111')
        fen = fen.replace('6','111111')
        fen = fen.replace('7','1111111')
        fen = fen.replace('8','11111111')
        fen = fen.replace('/','')

        fitness = 0
        # diem cong dua tren vi tri quan co chi huu dung khi khai cuoc
        if self.board.fullmove_number<12:
            for i in range(64):
                fitness += (point[fen[i]]['value'] + point[fen[i]]['pos'][i])
        else: 
            for i in range(64):
                fitness += point[fen[i]]['value']

        return fitness
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
