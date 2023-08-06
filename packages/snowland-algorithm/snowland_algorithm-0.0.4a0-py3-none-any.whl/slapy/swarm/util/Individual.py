#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: 
# @file: Agent.py
# @time: 2018/7/29 14:35
# @Software: PyCharm

from abc import ABCMeta, abstractmethod
import numpy as np

npr = np.random
npa = np.array


class Individual(object):
    __metaclass__ = ABCMeta

    def __init__(self, chromosome=None, dim=2, bound=None, fitness_function=None, *,
                 fitness_value=-np.inf, init_method='random', **kwargs):
        if chromosome:
            self._chromosome = chromosome
            self.dim = len(chromosome)
            if bound:
                bound = npa(bound)
                if len(bound.shape) == 1:
                    bound = np.repeat([bound], self.dim, axis=0)
                else:
                    m, n = bound.shape
                    if m == 1:
                        bound = np.repeat([bound], self.dim, axis=0)
                    else:
                        if self.dim is not m:
                            raise ValueError('size bound not match dim')
            else:
                bound = npa([[0, 1] for _ in range(self.dim)])
            self.bound = bound
        else:
            self.dim = dim
            if bound:
                bound = npa(bound)
                if len(bound.shape) == 1:
                    bound = np.repeat([bound], self.dim, axis=0)
                else:
                    m, n = bound.shape
                    if m == 1:
                        bound = np.repeat(bound, self.dim, axis=0)
                    else:
                        if self.dim is not m:
                            raise ValueError('size bound not match dim')
            else:
                bound = npa([[0, 1] for _ in range(self.dim)])
            self.bound = bound
            if init_method == 'rand' or init_method == 'random':
                self._chromosome = npr.random(dim) * (bound[:, 1] - bound[:, 0]).flatten() + bound[:, 0].flatten()
            else:
                self._chromosome = npr.randn(dim) * (bound[:, 1] - bound[:, 0]).flatten() + bound[:, 0].flatten()
        self._fitness_value = fitness_value
        self.fitness_function = fitness_function

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, chromosome):
        self._chromosome = chromosome

    @property
    def fitness_value(self):
        return self._fitness_value

    @fitness_value.setter
    def fitness_value(self, fitness_value):
        self._fitness_value = fitness_value

    def update(self, *args, **kwargs):
        pass

    def fitness(self, *args, **kwargs):
        self._fitness_value = self.fitness_function(self._chromosome)
        return self._fitness_value

    def __gt__(self, agent):
        return self._fitness_value > agent.fitness_value

    def __lt__(self, agent):
        return self._fitness_value < agent.fitness_value
