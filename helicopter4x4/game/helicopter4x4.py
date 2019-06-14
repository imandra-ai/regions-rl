from enum import Enum, unique
from typing import NamedTuple , Dict
from collections import defaultdict

@unique
class Status(Enum):
    flying = 1
    crashed = 2
    reached = 3

class Position(NamedTuple):
    x : int
    y : int
 
class State:
    def __init__(self):
        self.status   : Status = Status.flying
        self.fuel     : int = 2
        self.position : Position = Position(0,0)
        self.islands  : Dict[Position,bool] = defaultdict(lambda: False, {})
            
        self.ndiscount : int = 0
        self.reward    : int = 0

            
    def validate_Move(self, pos:Position):     
        if self.status != Status.flying: return False
        if pos.x == self.position.x and pos.y == self.position.y : return False
        if pos.x < 0 or pos.x > 3 : return False
        if pos.y < 0 or pos.y > 3 : return False
        if abs(self.position.x - pos.x) + abs(self.position.y - pos.y) > 2: return False
        return True
        
            
    def receive_Move(self, pos:Position):     
        
        adx: int = abs(self.position.x - pos.x)
        ady: int = abs(self.position.y - pos.y)
        
        used_fuel : int = adx + ady
                        
        self.position : Position = pos        
        if used_fuel > self.fuel:
            self.reward : int = 0 - 10 # Unary minus not implemented :(
            self.status : Status = Status.crashed
            return
        
        if self.position.x == 3 and self.position.y == 3:
            self.reward : int = 1000 
            self.status : Status = Status.reached
            return
            
        if self.islands[self.position]:
            self.islands[self.position] = False
            self.fuel : int = 2
        else:
            self.fuel : int = self.fuel - used_fuel
        
        if self.fuel == 0:
            self.reward : int = 0 - 10 # Unary minus not implemented :(
            self.status : Status = Status.crashed
            return
        
        self.ndiscount : int = self.ndiscount + 1


    def validate_SetState(self, pos:Position, nmap:Dict[Position,bool], nfuel:int):
        if nfuel <= 0 or nfuel > 2 : return False
        if pos.x < 0 or pos.x > 3 : return False
        if pos.y < 0 or pos.y > 3 : return False
        return True
                    
            
    def receive_SetState(self, pos:Position, nmap:Dict[Position,bool], nfuel:int):
        self.fuel : int = nfuel
        self.position : Position = pos
        self.islands : Dict[Position,bool] = nmap
        self.status : Status = Status.flying 
        self.ndiscount : int = 0
        self.reward    : int = 0
