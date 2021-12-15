# %%
import numpy as np

# %%
STATE_SHAPE = (65, )
NB_ACTIONS = 4096


# %%
# model.load_weights('chess_dqn_model.h5')

# %%
def find_move (board, model):
    state = board.get_state()

    Q_val = model.predict(state.reshape((1, 1) + STATE_SHAPE)).reshape(-1, )
    idx_sorted = np.argsort(Q_val)

    for act in idx_sorted:
        try:
            move = board.decodeMove(act)     
            break
        except:
            continue

    return move


