import itertools
import numpy as np
from .helicopter3x3 import State, Position, Status

class StateManager(State):
    
    def __init__(self, islandmap):
        nfuel, position = 1, Position(0,0)
        if not self.validate_SetState(position, islandmap, nfuel):
            raise ValueError("Invalid state initialization")
        self.receive_SetState(position, islandmap, nfuel)
    
    def encode(self, feed):
        feed[:,:,:] = np.zeros_like(feed)
        for k, v in self.islands.items():
            if not v: continue
            feed[k.x,k.y,0] = 1.0
        feed[self.position.x,self.position.y,self.fuel] = 1.0
        
    def action_mask(self, feed):
        for x, y in itertools.product(range(3), range(3)):
            feed[x,y] = self.validate_Move(Position(x,y))
    
    def get_reward(self):
        return self.reward
    
    def is_done(self):
        return self.status != Status.flying

            
            
