import numpy as np
import pandas as pd
from collections import defaultdict
from . import helicopter3x3

def generate_random_maps(size):
    r = np.random.uniform(0,2**9,size=size)
    r = r.astype(np.uint32).view(np.uint8)
    r = np.unpackbits(r).reshape((-1,32))[:,:9]
    r = np.argwhere(r.astype(bool))

    data = [defaultdict(lambda:[]) for _ in range(size)]
    for i in range(r.shape[0]):
        n , ix = r[i]
        p = helicopter3x3.Position(*np.unravel_index(ix,(3,3)))
        data[n][p] = True
    return data

def get_all_maps():
    r = np.arange(2**9)
    r = r.astype(np.uint32).view(np.uint8)
    r = np.unpackbits(r).reshape((-1,32))[:,:9]
    r = np.argwhere(r.astype(bool))

    data = [defaultdict(lambda:[]) for _ in range(2**9)]
    for i in range(r.shape[0]):
        n , ix = r[i]
        p = helicopter3x3.Position(*np.unravel_index(ix,(3,3)))
        data[n][p] = True
    get_all_maps.data = data
    return data



def evaluate(nnets):
    ix = np.arange(2**9)
    maps = []
    for i in range(9):
        mask = np.left_shift(np.ones_like(ix), i)
        maps.append(np.bitwise_and(mask,ix).astype(bool))
    maps = np.array(maps).T
    maps = maps.reshape((512,3,3))

    allstates = []
    ps = np.array(np.meshgrid(np.arange(3) , np.arange(3))).T
    for imap in maps:
        islands = defaultdict(lambda:False)
        for x,y in ps[np.array(imap).astype(bool)]:
            islands[helicopter3x3.Position(x,y)] = True
        state = helicopter3x3.State()
        state.receive_SetState(helicopter3x3.Position(0,0), islands, 1)
        allstates.append(state)

    allmoves = np.array(np.unravel_index(np.arange(9), (3,3))).T
    allmoves = [helicopter3x3.Position(x,y) for x,y in allmoves]

    inputs = np.zeros((512,3,3,2))

    alldone = False
    while not alldone:
        for n, state in enumerate(allstates):
            encode_state(inputs[n], state)

        predictions = nnets.predict_model.predict(inputs).reshape((-1,9))
        ranked_actions = predictions.argsort()
        alldone = True
        for n, state in enumerate(allstates):
            if state.status != helicopter3x3.Status.flying:
                continue
            alldone = False
            for m in ranked_actions[n][::-1]:
                if state.receive_Move(allmoves[m]) is None:
                    break
    ev = pd.Series([s.status for s in allstates]).value_counts().to_dict()
    crashed = ev.get(helicopter3x3.Status.crashed, 0)
    reached = ev.get(helicopter3x3.Status.reached, 0)
    return reached, crashed


