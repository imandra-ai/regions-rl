import numpy as np

def masked_argmax(array, mask):
    shape = array.shape
    ma = np.ma.masked_array(array, ~mask.astype(bool))
    ma = ma.reshape((shape[0], -1)) 
    raveled = ma.argmax(axis=1)
    return np.unravel_index(raveled, shape[1:])

def epsilon_greedy_actions(epsilon, predict_model, states_feed, amask_feed):
    # Use model to predict Q
    Q = predict_model.predict(states_feed)
    # Replace with random values with probability epsilon
    epsilon_idx = np.random.rand(Q.shape[0]) < epsilon
    Q[epsilon_idx] = np.random.rand(epsilon_idx.sum(), *Q.shape[1:])
    # Get masked argmax indices  
    action_indices = masked_argmax(Q, amask_feed)    
    return action_indices