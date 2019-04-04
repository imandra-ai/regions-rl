import copy
import numpy as np
import pandas as pd
from collections import defaultdict
import helicopter4x4

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
        p = np.random.uniform(size=16*len(paths)).reshape((-1,16))
    else:
        p = get_predictions(paths, predict_model).reshape((-1,16))

        # Fill with random with probability epsilon
        epsilon_choice = np.random.uniform(size=len(paths)) < epsilon
        p[epsilon_choice] = np.random.uniform(size=16*epsilon_choice.sum()).reshape((-1,16))

    # Argsort to get action ranks
    ranked_actions = p.argsort()

    # For each state in path
    alldone = True
    for n, path in enumerate(paths):
        _ , state = path[-1]
        if state.status != helicopter4x4.Status.flying:
            continue

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


