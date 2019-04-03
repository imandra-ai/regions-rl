import tensorflow as tf

def SubtractMean():
    f = lambda x: x - tf.reduce_mean(x, axis=-1, keep_dims=True)
    return tf.keras.layers.Lambda(f)

def makeDuelingDQN(internal_layers, learning_rate):
    inputs = tf.keras.layers.Input(shape=[3,3,2])
    net = internal_layers[0](inputs)
    for layer in internal_layers[1:]:
        net = layer(net)
    # Value Head
    value = tf.keras.layers.Dense(1)(net)
    # Advantage Head
    net = tf.keras.layers.Dense(9)(net)
    advantage = SubtractMean()(net)
    # Q = Value + Advantage
    q = tf.keras.layers.Add()([value,advantage])
    q = tf.keras.layers.Reshape((3,3))(q)
    
    predict_model = tf.keras.Model(inputs=[inputs], outputs=q)

    actions_mask = tf.keras.layers.Input(shape=(3,3))
    masked = tf.keras.layers.multiply([q,actions_mask])

    train_model = tf.keras.Model(inputs=[inputs, actions_mask], outputs=masked)
    opt = tf.keras.optimizers.RMSprop(lr=learning_rate)
    train_model.compile(optimizer=opt,loss='mse')
    
    return predict_model, train_model


class DoubleDQN:
    def __init__(self, internal_layers, learning_rate):

        self.predict_model, _ = makeDuelingDQN(internal_layers, learning_rate)
        _ , self.train_model  = makeDuelingDQN(internal_layers, learning_rate)

        self.predict_model.set_weights(self.train_model.get_weights())

    def update_weights(self):
        self.predict_model.set_weights(self.train_model.get_weights())

    def train_on_sample(self, rm, size, discount, **args):
        states, actions, rewards, nstates, dones = rm.get_sample(size)

        done_idx = dones > 0.0
        targetQ = self.predict_model.predict(nstates)
        maxQ = targetQ[~done_idx].reshape((-1,9)).max(axis=1)

        targetQ[ done_idx] = rewards[ done_idx,None,None]
        targetQ[~done_idx] = maxQ[:,None,None] * discount
        targetQ = targetQ * actions

        return self.train_model.fit(x=[states,actions], y=targetQ, **args)


def layers():
    dargs = dict\
      ( kernel_initializer = 'random_uniform'
      , bias_initializer = 'random_uniform'
      , activation = 'relu'
      )

    layers = \
      [ tf.keras.layers.Flatten()
      , tf.keras.layers.Dense(32,**dargs)
      , tf.keras.layers.Dense(32,**dargs)
      ]

    return layers


