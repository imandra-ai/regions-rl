import numpy as np

from game import helicopter3x3
from game.state_manager import StateManager
from game.utils import generate_random_maps, get_all_maps

from .utils import epsilon_greedy_actions

def evaluate(predict_model, max_steps, state_shape, amask_shape):
    states = [StateManager(m) for m in get_all_maps()]
    states_feed = np.zeros((512,) + state_shape)
    amask_feed = np.zeros((512,) + amask_shape)

    for step in range(max_steps): 
        # Encode states
        states_feed.fill(0)
        amask_feed.fill(0)
        for n, state in enumerate(states):
            state.encode(states_feed[n])
            state.action_mask(amask_feed[n])
        # Epsilon-greedy action choice
        action_indices = epsilon_greedy_actions(0.0, predict_model, states_feed, amask_feed)
        # Apply actions, store actions, rewards, dones in the feed 
        for n, (state, action_x, action_y) in enumerate(zip(states, *action_indices)):
            if state.is_done(): 
                continue
            action = helicopter3x3.Position(action_x, action_y)
            state.receive_Move(action)   
    solved = sum(s.get_reward() == 1000 for s in states)
    return solved

def generate_playouts(nepisodes, max_steps, epsilon, predict_model, feeds):
    
    states = [StateManager(m) for m in generate_random_maps(nepisodes)]

    for step in range(max_steps): 
        # Encode states
        for n, state in enumerate(states):
            state.encode(feeds['state'][n, step])
            state.action_mask(feeds['amask'][n, step])
        # Epsilon-greedy action choice
        states_feed, amask_feed = feeds['state'][:,step], feeds['amask'][:,step]
        action_indices = epsilon_greedy_actions(epsilon, predict_model, states_feed, amask_feed)
        # Apply actions, store actions, rewards, dones in the feed 
        for n, (state, action_x, action_y) in enumerate(zip(states, *action_indices)):
            if state.is_done(): 
                continue
            action = helicopter3x3.Position(action_x, action_y)
            state.receive_Move(action)   
            feeds['action'][n,step][action_x, action_y] = 1 
            feeds['reward'][n,step] = state.get_reward()
            if state.is_done():
                feeds['done'][n,step] = True


from model.replay_memory import ReplayMemory
from model.nn import DoubleDQN, layers


def log(feeds):
    print("- maps solved {}".format((feeds['reward'] == 1000).sum()))
    avsteps = ((1 - (feeds['done'].cumsum(axis=1) - feeds['done'])).sum(axis=1)).mean()
    print("- average number of steps steps {}".format(avsteps))
    
                
def run_training(**args):
    state_shape = (3,3,2)
    amask_shape = (3,3)
    action_shape = (3,3)
        
    dqn = DoubleDQN(layers, args['lr'])
    rm = ReplayMemory( args['rmsize'], max_steps, state_shape, amask_shape, action_shape)
    
    train_size = args['train_size']
    nepisodes, max_steps = args['nepisodes'], args['max_steps']
    discount = args['discount']
    eps_steps, update_every = args['eps_steps'], args['update_every']
    batch_size, epochs = args['batch_size'], args['epochs']

    # Pre-fill replay memory with random plays
    epsilon = 1
    for _ in range(5):
        feeds = rm.get_feeds(nepisodes)
        generate_playouts(nepisodes, max_steps, epsilon, dqn.predict_model, feeds)

    for n, epsilon in enumerate(np.linspace(0.95,0.05,eps_steps)):
        
        # Generating playouts
        print("# Epsilon {}".format(epsilon))
        feeds = rm.get_feeds(nepisodes)
        generate_playouts(nepisodes, max_steps, epsilon, dqn.predict_model, feeds)
        log(feeds)
        
        # Sample from RM and train
        sample = rm.sample(train_size)
        dqn.train_on_sample(sample, discount, epochs=epochs, batch_size=batch_size, verbose=0)
        if n != 0 and n % update_every == 0:
            dqn.update_weights()
        
        
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outfile",    required=True, type=str,   help="output file")
    parser.add_argument("--nruns",      required=True, type=int,   help="number of stats runs")

    parser.add_argument('--regions',    dest='regions', action='store_true')
    parser.add_argument('--no-regions', dest='regions', action='store_false')
    parser.set_defaults(regions=True)

    parser.add_argument("--lr",           required=True, type=float, help="learning rate")
    parser.add_argument("--discount",     required=True, type=float, help="discount factor")    
    parser.add_argument("--rmsize",       required=True, type=int,   help="replay memory size")
    parser.add_argument("--eps-steps",    required=True, type=int,   help="epsilon steps")
    parser.add_argument("--update-every", required=True, type=int,   help="how often update predictor net weights")    
    parser.add_argument("--nepisodes",    required=True, type=int,   help="playouts per epsilon")
    parser.add_argument("--max-steps",    required=True, type=int,   help="playout horizon")    
    parser.add_argument("--train-size",   required=True, type=int,   help="train sample size")
    parser.add_argument("--epochs",       required=True, type=int,   help="training epochs")
    parser.add_argument("--batch-size",   required=True, type=int,   help="batch size")
    args = parser.parse_args()
    
    with open(args.outfile, "w") as f:
        args = vars(args)
        del args['outfile']
        for k,v in args.items():
            f.write("# {} = {}\n".format(k,v))
        for n in range(args['nruns']):
            run(f,n, **args)
            f.flush()