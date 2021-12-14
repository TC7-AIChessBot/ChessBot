# %%
import numpy as np

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation, Flatten,\
#      Input,BatchNormalization, Dropout
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten,\
     Input,BatchNormalization, Dropout

# %%
STATE_SHAPE = (65, )
NB_ACTIONS = 4096

# %%
# model
model = Sequential()
model.add(Input((1, ) + STATE_SHAPE))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(NB_ACTIONS))
model.add(Activation('linear'))

# %%
model.load_weights('chess_dqn_vs_sf_model.h5')

# %%
def find_move (board):
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


