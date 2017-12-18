# -*- coding: utf-8 -*-
# dqn.py
# author : Robin Petit, Stanislas Gueniffey, Cedric Simar, Antoine Passemiers

from parameters import Parameters
from environment import Environment
from dqn import DQN

import numpy as np
import tensorflow as tf


class Agent:
    def __init__(self):
        
        self.environment = Environment()
        self.dqn = DQN(self.environment.get_input())


    def select_action(self, s):
        # The agent uses its experience and expertise acquired
        # through deep learning to make intelligent actions
        return np.random.randint(0, self.n_actions, size=1)[0]

Agent()