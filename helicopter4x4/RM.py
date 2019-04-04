import numpy as np
import copy
import itertools
import helicopter4x4
from utils import encode_state

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


