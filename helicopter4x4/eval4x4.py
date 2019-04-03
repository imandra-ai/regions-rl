import copy
import itertools 
import numpy as np
import pandas as pd

from collections import defaultdict
import helicopter4x4
import regions_tree_4x4


def generate_random_maps(size):
    r = np.random.uniform(0,2**16,size=size)
    r = r.astype(np.uint32).view(np.uint8)
    r = np.unpackbits(r).reshape((-1,32))[:,:16]
    r = np.argwhere(r.astype(bool))

    data = [defaultdict(lambda:[]) for _ in range(size)]
    for i in range(r.shape[0]):
        n , ix = r[i]
        p = helicopter4x4.Position(*np.unravel_index(ix,(4,4)))
        data[n][p] = True
    return data

def random_move():
    ix = int(np.random.uniform(16))
    move = np.unravel_index(ix, (4,4))
    return helicopter4x4.Position(*move)


counts = defaultdict(lambda: 0)
def random_move_over_regions(state):
    currentMax = random_move_over_regions.globalMax
    bestMove, bestRegion = None, None
    for _ in range(10):
        nstate = copy.deepcopy(state)
        while True:
            move1 = random_move()
            if nstate.receive_Move(move1) is None: break
        while True:
            move2 = random_move()        
            if nstate.receive_Move(move2) is None: break                
        inputs = \
            [ type("",(),{"nmap":state.islands, "pos":state.position, "nfuel": state.fuel})
            , type("",(),{"pos":move1})
            , type("",(),{"pos":move2})
            , None
            ]
        while True:
            region = regions_tree_4x4.calculate_regions(inputs)
            if region is not None:
                region = tuple(region)
                break
        visits = counts[region]
        if visits == 0: 
            bestMove = move1
            bestRegion = region
            break
        if visits < currentMax:
            currentMax = visits
            bestMove = move1
            bestRegion = region
    if bestRegion is None: 
        bestRegion , bestMove = region , move1 
    counts[bestRegion] += 1   
    if counts[bestRegion] > random_move_over_regions.globalMax:
        random_move_over_regions.globalMax = counts[bestRegion]

    return bestMove

random_move_over_regions.globalMax = 1



def generate_random_initial(size):
    states = []
    for nmap in generate_random_maps(size):
        state = helicopter4x4.State()
        pos = helicopter4x4.Position(0,0)
        state.receive_SetState(pos, nmap, 2)
        states.append(state)
    return states

def encode_state(feed, state):
    feed[:,:,:] = np.zeros_like(feed)
    for k, v in state.islands.items():
        if not v: continue
        feed[k.x,k.y,0] = 1.0
    feed[state.position.x,state.position.y,1] = state.fuel



# The network

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



# Replay memory

class ReplayMemory:
    def __init__(self, size=5000):
        self.size = size
        self.index = 0
        self.maxSize = 0
        self.symbolic = np.array([None] * size)
        self.states   = np.zeros((self.size,4,4,2))
        self.actions  = np.zeros((self.size,4,4))
        self.rewards  = np.zeros((self.size,))
        self.nstates  = np.zeros((self.size,4,4,2))
        self.done     = np.zeros((self.size,))
        
        self.data =  [self.symbolic, self.states, self.actions, self.rewards, self.nstates, self.done]
        
    def store_paths(self, paths):
        i1,i2 = itertools.tee(itertools.chain.from_iterable(paths))
        next(i2)
        for (__, s), (a, ns) in zip(i1,i2):
            if a is None: 
                continue
            self.symbolic[self.index] = copy.deepcopy(ns)
            encode_state(self.states[self.index,:,:,:], s)
            self.actions[self.index,:,:] = 0.0
            self.actions[self.index, a.x, a.y] = 1.0
            self.rewards[self.index] = ns.reward            
            encode_state(self.nstates[self.index,:,:,:], ns)
            if ns.status != helicopter4x4.Status.flying:
                self.done[self.index] = 1.0
            else:
                self.done[self.index] = 0.0
            
            self.index += 1
            if self.index >= self.size: self.index = 0
            if self.index > self.maxSize: self.maxSize = self.index
    
    def get_sample(self, size):
        ix = np.random.uniform(size=self.maxSize)
        ix = np.argsort(ix)[:size]
        return [d[ix] for d in self.data]    

def get_predictions(paths, predict_model):
    if get_predictions.feed.shape[0] != len(paths):
        get_predictions.feed = np.zeros((len(paths),4,4,2))
    for n, path in enumerate(paths):
        _ , s = path[-1]
        encode_state(get_predictions.feed[n],s)
    return predict_model.predict(get_predictions.feed)

get_predictions.feed = np.zeros((1,4,4,2))

def do_epsilon_greedy_step(paths, epsilon, predict_model):

    # Get predictions (don't query the net if epsilon == 1.0)
    if epsilon == 1.0:
        p = np.zeros((len(paths), 16)).reshape((-1,16))
    else:
        p = get_predictions(paths, predict_model).reshape((-1,16))

    # Exploration with probability epsilon
    epsilon_choice = np.random.uniform(size=len(paths)) < epsilon
    # Argsort to get action ranks
    ranked_actions = p.argsort()

    # For each state in path
    alldone = True
    for n, path in enumerate(paths):
        _ , state = path[-1]
        if state.status != helicopter4x4.Status.flying:
            continue
        if epsilon_choice[n]:
            state = copy.deepcopy(state)
            move = random_move_over_regions(state)
            state.receive_Move(move)
        else:
            # Find highest ranked valid move
            state = copy.deepcopy(state)
            for action in ranked_actions[n,::-1]:
                action = np.unravel_index(action, (4,4))
                move = helicopter4x4.Position(*action)
                if state.receive_Move(move) is None: break

        path.append((move, state))
        alldone = False
    return alldone


def evaluate(nnets,N):
    states = generate_random_initial(N)
    paths = [[(None, s)] for s in states]
    while not do_epsilon_greedy_step(paths, 0.0, nnets.predict_model):
        pass

    ev = pd.Series([p[-1][-1].status for p in paths]).value_counts().to_dict()
    crashed = ev.get(helicopter4x4.Status.crashed, 0)
    reached = ev.get(helicopter4x4.Status.reached, 0)
    return reached, crashed


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

def run(f,n,**args):
    if n == 0:
        f.write("n,epsilon,loss,reached,eval_reach,eval_crash\n")
    nnets = DoubleDQN(layers(), args['lr'])

    rmem = ReplayMemory(args['rmsize'])
    counts = defaultdict(lambda: 0)

    states = generate_random_initial(args['playouts'])
    paths = [[(None, s)] for s in states]
    while not do_epsilon_greedy_step(paths, 1.0, nnets.predict_model):
        pass
    rmem.store_paths(paths)

    for e in np.linspace(0.95,0.05,args['steps']):

        states = generate_random_initial(args['playouts'])
        paths = [[(None, s)] for s in states]
        while not do_epsilon_greedy_step(paths, e, nnets.predict_model):
            pass
        rmem.store_paths(paths)

        h = nnets.train_on_sample(rmem, args['train_size'], 0.9, epochs=args['epochs'], batch_size=args['batch_size'], verbose=0)
        nnets.update_weights()
        nreached = sum([ p[-1][-1].status == helicopter4x4.Status.reached for p in paths ])
        print("Epsilon = {:.2}, loss = {:.5}, reached = {}/{}".format(e,h.history['loss'][-1], nreached, args['playouts']))
        print("Evaluating .... ", end='')
        ereach, ecrash = evaluate(nnets, args['playouts'])
        print("reached/crashed = {}/{}".format(ereach, ecrash))
        f.write("{},{},{},{},{},{}\n".format(n,e,h.history['loss'][-1],nreached,ereach, ecrash))


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outfile",    required=True, type=str,   help="output file")
    parser.add_argument("--nruns",      required=True, type=int,   help="number of stats runs")

    parser.add_argument("--lr",         required=True, type=float, help="learning rate")
    parser.add_argument("--rmsize",     required=True, type=int,   help="replay memory size")
    parser.add_argument("--steps",      required=True, type=int,   help="epsilon steps")
    parser.add_argument("--playouts",   required=True, type=int,   help="playouts per epsilon")
    parser.add_argument("--train-size", required=True, type=int,   help="train sample size")
    parser.add_argument("--epochs",     required=True, type=int,   help="training epochs")
    parser.add_argument("--batch-size", required=True, type=int,   help="batch size")
    args = parser.parse_args()
    
    with open(args.outfile, "w") as f:
        args = vars(args)
        del args['outfile']
        for k,v in args.items():
            f.write("# {} = {}\n".format(k,v))
        for n in range(args['nruns']):
            run(f,n, **args)
            f.flush()


