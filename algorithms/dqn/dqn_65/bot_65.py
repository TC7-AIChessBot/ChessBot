# %%
import numpy as np
from ...MyChessBoard import MyChessBoard

# %%
def find_move (board: MyChessBoard, model):
    state = board.get_state()

    Q_val = model.predict(state.reshape((1, 1) + (65, ))).reshape(-1, )
    idx_sorted = np.argsort(Q_val)

    for act in idx_sorted:
        try:
            move = board.decodeMove(act)     
            break
        except:
            continue

    return move


