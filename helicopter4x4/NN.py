
import copy
import numpy as np
import itertools
import helicopter4x4
import tensorflow as tf

def SubtractMean():
    f = lambda x: x - tf.reduce_mean(x, axis=-1, keep_dims=True)
    return tf.keras.layers.Lambda(f)

def makeDuelingDQN(internal_layers, learning_rate):
    inputs = tf.keras.layers.Input(shape=[4,4,2])
    net = internal_layers[0](inputs)
    for layer in internal_layers[1:]:
        net = layer(net)
    # Value Head
    value = tf.keras.layers.Dense(1)(net)
    # Advantage Head
    net = tf.keras.layers.Dense(16)(net)
    advantage = SubtractMean()(net)
    # Q = Value + Advantage
    q = tf.keras.layers.Add()([value,advantage])
    q = tf.keras.layers.Reshape((4,4))(q)
    
    predict_model = tf.keras.Model(inputs=[inputs], outputs=q)

    actions_mask = tf.keras.layers.Input(shape=(4,4))
    masked = tf.keras.layers.multiply([q,actions_mask])

    train_model = tf.keras.Model(inputs=[inputs, actions_mask], outputs=masked)
    opt = tf.keras.optimizers.RMSprop(lr=learning_rate)
    train_model.compile(optimizer=opt,loss='mse')
    
    return predict_model, train_model


# Doulbe DQN
class DoubleDQN:
    def __init__(self, internal_layers, learning_rate):
        
        self.predict_model , _ = makeDuelingDQN(internal_layers, learning_rate)
        self.doubled_model , self.train_model  = makeDuelingDQN(internal_layers, learning_rate)

        self.predict_model.set_weights(self.train_model.get_weights())
        
    def update_weights(self):
        self.predict_model.set_weights(self.train_model.get_weights())

    def prepare_target(self, rewards, nstates, dones, symbolic, discount):
        done_idx = dones > 0.0
        targetQ = self.predict_model.predict(nstates)
        predictQ = targetQ[~done_idx].reshape((-1,16))

        idxQ = self.doubled_model.predict(nstates)
        idxQ = idxQ[~done_idx].reshape((-1,16)).argsort(axis=1)[:,::-1]
        maxQ = np.zeros(predictQ.shape[0])
        
        for n, (s, qs, ixqs) in enumerate(zip(symbolic, predictQ, idxQ)):
            s = copy.deepcopy(s)
            for ixq in ixqs:
                action = np.unravel_index(ixq, (4,4))
                action = helicopter4x4.Position(*action)
                if s.receive_Move(action) is None: 
                    break
            maxQ[n] = qs[ixq]

        targetQ[ done_idx] = rewards[ done_idx,None,None]
        targetQ[~done_idx] = maxQ[:,None,None] * discount
        return targetQ
        
    def train_on_sample(self, rm, size, discount, **args):
        symbolic, states, actions, rewards, nstates, dones = rm.get_sample(size)

        targetQ = self.prepare_target(rewards, nstates, dones, symbolic, discount)
        
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


