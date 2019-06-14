import numpy as np
import pandas as pd
from collections import defaultdict
from . import helicopter4x4

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
