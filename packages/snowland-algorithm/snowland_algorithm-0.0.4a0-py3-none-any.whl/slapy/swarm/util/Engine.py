#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: 
# @file: Engine.py
# @time: 2018/7/29 3:13
# @Software: PyCharm

from abc import ABCMeta, abstractmethod
from functools import wraps
import numpy as np

npa = np.array


class Engine:
    __metaclass__ = ABCMeta

    def __init__(self, population_size=100,
                 steps=100,
                 eps=0.01,
                 dim=2,
                 bound=[0, 1],
                 fitness_function=None,
                 *,
                 init_method='rand',
                 min_fitness_value=-np.inf,
                 agents=None,
                 **kwargs):
        self._population_size = population_size
        self._steps = steps
        self._eps = eps
        self.dim = dim
        self.min_fitness_value = min_fitness_value
        self.fitness_function = fitness_function
        self.agents = agents if agents else None
        self.bound = bound
        self.init_method = init_method

    @property
    def population_size(self):
        return self._population_size

    @population_size.setter
    def population_size(self, population_size):
        self._population_size = population_size

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, steps):
        self._steps = steps

    @property
    def eps(self):
        return self._eps

    @steps.setter
    def eps(self, eps):
        self._eps = eps

    def fitness(self, *args, **kwargs):
        return npa([each.fitness_value for each in self.agents])

    def minimize(self, fn):
        """
        A decorator for minimizing the fitness function.
        """
        @wraps(fn)
        def _minimize(chromosome):
            return -fn(chromosome)
        return _minimize

    def run(self, *args, **kwargs):
        self.initialize(*args, **kwargs)
        for i in range(self.steps):
            self.fitness(*args, **kwargs)
            self.record(self, *args, **kwargs)
            self.update(*args, **kwargs)
        self.fitness(*args, **kwargs)
        self.record(self, *args, **kwargs)
        self.analysis(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        [each.initialize(*args, **kwargs) for each in self.agents]

    def update(self, *args, **kwargs):
        [each.update(*args, **kwargs) for each in self.agents]

    def analysis(self, *args, **kwargs):
        pass

    def record(self, *args, **kwargs):
        pass
