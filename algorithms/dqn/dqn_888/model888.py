# %%
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Activation, Flatten, Input, BatchNormalization,\
      Conv2D, Add, ZeroPadding2D, MaxPooling2D, GlobalAveragePooling2D, Reshape
from keras.initializers import glorot_uniform


# %%
def identity_block(X, f, filters, stage, block):
   
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'
    F1, F2 = filters

    X_shortcut = X
   
    X = Conv2D(filters=F1, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2a', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2a')(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F2, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2b', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2b')(X)

    X = Add()([X, X_shortcut])# SKIP Connection
    X = Activation('relu')(X)

    return X

# %%
def convolutional_block(X, f, filters, stage, block, s=2):
   
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    F1, F2 = filters

    X_shortcut = X

    X = Conv2D(filters=F1, kernel_size=(f, f), strides=(s, s), padding='same', name=conv_name_base + '2a', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2a')(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F2, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2b', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2b')(X)

    X_shortcut = Conv2D(filters=F2, kernel_size=(f, f), strides=(s, s), padding='same', name=conv_name_base + '1', kernel_initializer=glorot_uniform(seed=0))(X_shortcut)
    X_shortcut = BatchNormalization(axis=3, name=bn_name_base + '1')(X_shortcut)

    X = Add()([X, X_shortcut])
    X = Activation('relu')(X)

    return X

# %%
def SameResNet(input_shape=(8, 8, 8)):

    X_input = Input((1, ) + input_shape)

    X = Reshape(target_shape= input_shape)(X_input)

    X = ZeroPadding2D((2, 2))(X)

    X = Conv2D(64, (8, 8), strides=(1, 1), padding='same', name='conv1', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_conv1')(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((3, 3), strides=(2, 2))(X)

    X = convolutional_block(X, f=3, filters=[64, 64], stage=2, block='a', s=1)
    X = identity_block(X, 3, [64, 64], stage=2, block='b')
    X = identity_block(X, 3, [64, 64], stage=2, block='c')


    X = convolutional_block(X, f=3, filters=[128, 128], stage=3, block='a', s=2)
    X = identity_block(X, 3, [128, 128], stage=3, block='b')
    X = identity_block(X, 3, [128, 128], stage=3, block='c')
    X = identity_block(X, 3, [128, 128], stage=3, block='d')

    X = convolutional_block(X, f=3, filters=[256, 256], stage=4, block='a', s=1)
    X = identity_block(X, 3, [256, 256], stage=4, block='b')
    X = identity_block(X, 3, [256, 256], stage=4, block='c')
    X = identity_block(X, 3, [256, 256], stage=4, block='d')
    X = identity_block(X, 3, [256, 256], stage=4, block='e')
    X = identity_block(X, 3, [256, 256], stage=4, block='f')

    X = X = convolutional_block(X, f=3, filters=[512, 512], stage=5, block='a', s=2)
    X = identity_block(X, 3, [512, 512], stage=5, block='b')
    X = identity_block(X, 3, [512, 512], stage=5, block='c')

    X = GlobalAveragePooling2D()(X)
    
    model = Model(inputs=X_input, outputs=X, name='ResNet50')

    return model

# %%
def get_model888(STATE_SHAPE = (8, 8, 8), NB_ACTIONS = 4096):
    base_model = SameResNet(input_shape = STATE_SHAPE)
    
    headModel = base_model.output
    headModel = Flatten()(headModel)
    headModel = Dense(1000,activation='softmax', name='fc2',kernel_initializer=glorot_uniform(seed=0))(headModel)
    headModel = Dense(NB_ACTIONS,activation='linear', name='fc3',kernel_initializer=glorot_uniform(seed=0))(headModel)

    model = Model(inputs=base_model.input, outputs=headModel)
    return model


