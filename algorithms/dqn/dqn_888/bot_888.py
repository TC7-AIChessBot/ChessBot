# %%
import imp
import numpy as np
import chess
from ...MyChessBoard import MyChessBoard
from ...stockfish.stockfish_bot import find_move as fm2

# %%
def find_move (board: MyChessBoard, model):
    if np.random.uniform() < 0.05:
        state = board.get_state_888()

        Q_val = model.predict(state.reshape((1, 1) + (8, 8, 8))).reshape(-1, )
        idx_sorted = np.argsort(Q_val)

        for act in idx_sorted:
            try:
                from_square, to_square = act//64, act%64
                if not board.board.turn:
                    from_square = (7 - from_square // 8)*8 + from_square % 8
                    to_square = (7 - to_square // 8)*8 + to_square % 8
                
                move = board.board.find_move(from_square= from_square,to_square= to_square)
                print(chess.Move(from_square= act // 64, to_square= act % 64))
                print(move.uci())
                break
            except:
                continue
        return move
    else:
        return fm2(board)



