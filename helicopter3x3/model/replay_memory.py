import numpy as np

class ReplayMemory(object):
    def __init__(self, size, max_steps, state_shape, amask_shape, action_shape):
        self.nepisodes = size
        self.max_steps = max_steps
        base_shape = (self.nepisodes, self.max_steps)
        
        # Buffers for state, allowed actions, actions, rewards and is_done flags 
        self.state   = np.zeros(base_shape + state_shape)
        self.amask   = np.zeros(base_shape + amask_shape)                
        self.action  = np.zeros(base_shape + action_shape)        
        self.reward  = np.zeros(base_shape)
        self.done    = np.zeros(base_shape, dtype=bool)
        
        #
        self.data = \
          { "state"  : self.state
          , "amask"  : self.amask
          , "action" : self.action
          , "reward" : self.reward
          , "done"   : self.done
          }
        
        # Circular buffer indices
        self.idx , self.maxidx = 0, 0
        
    def get_feeds(self, size):
        if size > self.nepisodes:
            raise ValueError("Requested feed size is larger than the memory size")
        if self.idx + size > self.nepisodes:
            self.idx = 0
            
        feeds = {k:feed[self.idx:self.idx + size] for k,feed in self.data.items()}
        for feed in feeds.values(): feed.fill(0)
            
        self.idx = self.idx + size
        self.maxidx = max(self.idx, self.maxidx)
        return feeds
    
    def sample(self, size):
        # The index cuts entries after the "done" flag is up
        dones = self.done[:self.maxidx]
        idx_valid = ~dones.cumsum(axis=1).astype(bool) | dones
        max_size = idx_valid.sum()
        # Cropping the requestied size to size to validvalue
        size = min(size, max_size)
        ix = np.random.uniform(size=max_size)
        ix = np.argsort(ix)[:size]
        return { k:v[:self.maxidx][idx_valid][ix] for k,v in self.data.items()}       
