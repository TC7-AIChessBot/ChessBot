from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten,\
     Input,BatchNormalization, Dropout
     
def get_model65(STATE_SHAPE = (65, ), NB_ACTIONS = 4096):
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
    return model