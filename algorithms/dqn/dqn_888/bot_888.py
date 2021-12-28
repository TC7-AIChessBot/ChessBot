# %%
import numpy as np
import chess
from ...MyChessBoard import MyChessBoard

# %%
def find_move (board: MyChessBoard, model):
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
            print(board.decodeMove(act).uci())
            print(move.uci())
            break
        except:
            continue

    return move


