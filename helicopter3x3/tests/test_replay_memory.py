import unittest
import numpy as np

from model.replay_memory import ReplayMemory

def simulate_play(neps, steps, feeds):
    for i in range(neps):
        for j in range(steps):
            feeds['state'][i,j] = j + 1
            action = np.random.random() 
            feeds['action'][i,j] = action
            if action > 0.7:
                feeds['done'][i,j] = True 
                break

class TestIndexWrapping(unittest.TestCase):

    def test_index_wrapping_1(self):
        rm = ReplayMemory(60, 8, (), (), ())

        feeds = rm.get_feeds(20)
        simulate_play(20, 8, feeds)
        self.assertEqual((rm.idx, rm.maxidx) , (20,20))
        feeds = rm.get_feeds(30)
        simulate_play(30, 8, feeds)
        self.assertEqual((rm.idx, rm.maxidx) , (50,50))
        feeds = rm.get_feeds(20)
        simulate_play(20, 8, feeds)
        self.assertEqual((rm.idx, rm.maxidx) , (20,50))


class TestSampling(unittest.TestCase):

    def test_sampling_valid_states(self):
        rm = ReplayMemory(60, 8, (), (), ())
        feeds = rm.get_feeds(50)
        simulate_play(50, 8, feeds)

        for _ in range(10):
            sample = rm.sample(10)
            self.assertTrue( (sample['state'] > 0).all() )
            
    def test_sampling_final_actions(self):
        rm = ReplayMemory(60, 8, (), (), ())
        feeds = rm.get_feeds(50)
        simulate_play(50, 8, feeds)

        for _ in range(10):
            sample = rm.sample(10)            
            self.assertTrue( ((sample['action'] > 0.7) == sample['done']).all() )

    def test_sampling_final_next_states(self):
        rm = ReplayMemory(60, 8, (), (), ())
        feeds = rm.get_feeds(50)
        simulate_play(50, 8, feeds)

        for _ in range(10):
            sample = rm.sample(10)            
            self.assertTrue( ((sample['next_state'] - sample['state'] == 1) == (~sample['done'])).all() )
