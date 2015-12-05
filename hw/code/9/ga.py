import random as rand
from math import sqrt, exp, sin
from util import *
from copy import deepcopy
from __future__ import print_function, division
import sys



class GA():
    def __init__(self):
        self.configs = O(
        gens = 5000,  // is too high can we use 500 or 1000
        candidates = 100,
        better = lt,
        iter = 100,
        retain = 0.2, // How much can we retain
        p_mutate= 0.05
        )


    def optimize(self, base_DTLZ):
        
        population = [base_DTLZ.createPopulation() for _ in range(self.configs.candidates)]    
        sorted_population = sorted(population,  key=lambda x: base_DTLZ.energy(x))
        e_best = base_DTLZ.energy(sorted_population[0])
          

        currentIter = []
        prevIter = [-1] * self.configs.iter

        for i in range(self.configs.gens):
            
          parents_have_fit_score = self.sampling(population, base_DTLZ, self.configs.retain)

            
            next_generation = [can for can, score in parents_have_fit_score]
            
            childrenNumber = self.configs.candidates - len(next_generation)

            for j in range(childrenNumber):
                father, mother = self.select(parents_have_fit_score)
                new_can = self.crossover([father, mother])
                new_can = self.mutate(new_can, base_DTLZ, self.configs.p_mutate)
                next_generation.append(new_can)
                e_new = base_DTLZ.energy(new_can)
            

            population = sorted(next_generation,  key=lambda x: base_DTLZ.energy(x))
            e_new = base_DTLZ.energy(population[0])
            currentIterand.append(e_new)

            if e_new < e_best:
                e_best = e_new
                print('%', end='')          
            else:
                print('*', end='')

            // TODO : Check For Early Termination
            

        # TODO: How to do Parito frontier
        
        print("\nBest  Energy Result:" + str(e_best) )

    @staticmethod
    def sampling(population, base_DTLZ, retain):

        dominated_populations = []

        //TODO Struggling to understand Dominate function also, I am not sure where to weave that code ????
        
        

    @staticmethod
    def select(sampled_population):
 
        selected = []
        for can, score in sampled_population:
            selected += [can] * score

        father = rand.choice(selected)

        while True:
            mother = rand.choice(selected)
            if mother != father: break
        
        return (father, mother)

    @staticmethod
    def mutate(new_can, base_DTLZ, mutate_prob):
        # TODO: Can we have a better muation method
        if rand.random() > p_mutate:
            return new_can

        pos = rand.randint(0, len(new_can.decs) - 1)
        new_can.decs[pos] = rand.uniform(base_DTLZ.decs[pos].low, base_DTLZ.decs[pos].high)
        return new_can

    @staticmethod
    def crossover(parents):
        pos = rand.randint(0, len(parents[0].decs) - 1)
        can = parents[0].clone()
        can.decs[pos:] = parents[1].decs[pos:]
        return can