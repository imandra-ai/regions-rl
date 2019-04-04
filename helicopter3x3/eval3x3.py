import copy
import itertools 
import numpy as np
import pandas as pd

from collections import defaultdict
import helicopter3x3
import regions_tree_3x3

from utils import *
from NN import layers, DoubleDQN 
from RM import ReplayMemory 



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
            region = regions_tree_3x3.calculate_regions(inputs)
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

def do_epsilon_greedy_step(paths, epsilon, predict_model):
    
    # Get predictions (don't query the net if epsilon == 1.0)
    if epsilon == 1.0:
        p = np.random.uniform(size=9*len(paths)).reshape((-1,9))
    else:
        p = get_predictions(paths, predict_model).reshape((-1,9))

        # Fill with random with probability epsilon
        epsilon_choice = np.random.uniform(size=len(paths)) < epsilon
        p[epsilon_choice] = np.random.uniform(size=9*epsilon_choice.sum()).reshape((-1,9))

    # Argsort to get action ranks
    ranked_actions = p.argsort()
    
    # For each state in path 
    alldone = True
    for n, path in enumerate(paths):
        _ , state = path[-1]
        if state.status != helicopter3x3.Status.flying:
            continue

        # Find highest ranked valid move
        state = copy.deepcopy(state)
        for action in ranked_actions[n,::-1]:
            action = np.unravel_index(action, (3,3))
            move = helicopter3x3.Position(*action)
            if state.receive_Move(move) is None: break

        path.append((move, state))
        alldone = False
    return alldone



def do_epsilon_greedy_step_regions(paths, epsilon, predict_model):

    # Get predictions (don't query the net if epsilon == 1.0)
    if epsilon == 1.0:
        p = np.zeros((len(paths), 9)).reshape((-1,9))
    else:
        p = get_predictions(paths, predict_model).reshape((-1,9))

    # Exploration with probability epsilon
    epsilon_choice = np.random.uniform(size=len(paths)) < epsilon
    # Argsort to get action ranks
    ranked_actions = p.argsort()

    # For each state in path
    alldone = True
    for n, path in enumerate(paths):
        _ , state = path[-1]
        if state.status != helicopter3x3.Status.flying:
            continue
        if epsilon_choice[n]:
            state = copy.deepcopy(state)
            move = random_move_over_regions(state)
            state.receive_Move(move)
        else:
            # Find highest ranked valid move
            state = copy.deepcopy(state)
            for action in ranked_actions[n,::-1]:
                action = np.unravel_index(action, (3,3))
                move = helicopter3x3.Position(*action)
                if state.receive_Move(move) is None: break

        path.append((move, state))
        alldone = False
    return alldone


def fill_playouts(rmem, nnets, epsilon, size, regions):

    if regions:
        step_function = do_epsilon_greedy_step_regions
    else:
        step_function = do_epsilon_greedy_step

    states = generate_random_initial(args['playouts'])
    paths = [[(None, s)] for s in states]
    while not step_function(paths, epsilon, nnets.predict_model):
        pass
    rmem.store_paths(paths)



def run(f,n,**args):
    if n == 0:
        f.write("n,epsilon,loss,eval_reach,eval_crash\n")
    nnets = DoubleDQN(layers(), args['lr'])

    rmem = ReplayMemory(args['rmsize'])
    counts = defaultdict(lambda: 0)
    random_move_over_regions.globalMax = 1

    fill_playouts(rmem, nnets, 1.0, args['playouts'], args['regions'])

    for e in np.linspace(0.95,0.05,args['steps']):

        fill_playouts(rmem, nnets, e, args['playouts'], args['regions'])

        h = nnets.train_on_sample(rmem, args['train_size'], 0.9, epochs=args['epochs'], batch_size=args['batch_size'], verbose=0)
        nnets.update_weights()
        print("Epsilon = {:.2}, loss = {:.5}".format(e,h.history['loss'][-1]))
        print("Evaluating .... ", end='')
        ereach, ecrash = evaluate(nnets)
        print("reached/crashed = {}/{}".format(ereach, ecrash))
        f.write("{},{},{},{},{}\n".format(n,e,h.history['loss'][-1],ereach, ecrash))

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outfile",    required=True, type=str,   help="output file")
    parser.add_argument("--nruns",      required=True, type=int,   help="number of stats runs")

    parser.add_argument('--regions',    dest='regions', action='store_true')
    parser.add_argument('--no-regions', dest='regions', action='store_false')
    parser.set_defaults(regions=True)

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


