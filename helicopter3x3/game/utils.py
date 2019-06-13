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

