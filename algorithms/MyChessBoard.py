import chess
import sys
import numpy as np

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

        move = self.env.find_move(from_square= a,to_square= b)
        return move