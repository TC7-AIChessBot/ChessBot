# class Config:
#DEPTH = 3
import chess
import numpy as np
piece_value = {
    chess.PAWN: 10,
    chess.ROOK: 40,
    chess.KNIGHT: 20,
    chess.BISHOP: 30,
    chess.QUEEN: 50,
    chess.KING: 900
}

pawnEvalWhite =(np.array([
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, -20, -20, 10, 10,  5,
    5, -5, -10,  0,  0, -10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
])/10).tolist()
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval =(np.array( [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
])/10).tolist()

bishopEvalWhite = (np.array([
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
])/10).tolist()
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite =(np.array( [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
])/10).tolist()
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval =(np.array([
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
])/10).tolist()

kingEvalWhite =(np.array( [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
])/10).tolist()
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = (np.array([
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
])/10).tolist()
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
def convert(x,square,map):
    for i in range(8):
        for j in range(8):
            if square[i][j]==map:
                x[i][j]=1
            elif square[i][j] == -map:
                x[i][j]=-1 