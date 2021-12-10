import chess
import sys

sys.path.insert(0, './alpha_beta')
from Config import point
# from .alpha_beta.Config import point

# print(sys.path)
piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

<<<<<<< HEAD
=======
piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

>>>>>>> 3cc4c369cc6be61c10ac7a555e72aaf0e14408b0
pawnEvalWhite = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, -20, -20, 10, 10,  5,
    5, -5, -10,  0,  0, -10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

def evaluate_piece(piece, square, end_game):
        piece_type = piece.piece_type
        mapping = []
        if piece_type == chess.PAWN:
            mapping = pawnEvalWhite if piece.color == chess.WHITE else pawnEvalBlack
        if piece_type == chess.KNIGHT:
            mapping = knightEval
        if piece_type == chess.BISHOP:
            mapping = bishopEvalWhite if piece.color == chess.WHITE else bishopEvalBlack
        if piece_type == chess.ROOK:
            mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
        if piece_type == chess.QUEEN:
            mapping = queenEval
        if piece_type == chess.KING:
            # use end game piece-square tables if neither side has a queen
            if end_game:
                mapping = (
                    kingEvalEndGameWhite
                    if piece.color == chess.WHITE
                    else kingEvalEndGameBlack
                )
            else:
                mapping = kingEvalWhite if piece.color == chess.WHITE else kingEvalBlack

        return mapping[square]

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
    def evaluate_board(self):
        total = 0
        end_game = self.check_end_game

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
