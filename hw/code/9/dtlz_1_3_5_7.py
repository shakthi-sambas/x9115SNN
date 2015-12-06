import math
from copy import deepcopy
import random as rand
#from util import *

##We can either use this wrapper classes or we can use gadget classes




class Dec():
    def __init__(self, name, high, low):
        self.name = name
        self.high = high
        self.low = low


class Obj():
    def __init__(self, name, function, better=lt):
        self.name = str(name)
        self.function = function
        self.better = better

class Can(object):
    "A candidate decision values, objective scores, and energy"
    def __init__(self, decs = [], obj_fit_score = [], energy = None):
        self.decs = decs
        self.obj_fit_score = obj_fit_score
        self.energy = energy

    def createCandidate(self):
        new_can = Can()
        new_can.decs = deepcopy(self.decs)
        new_can.obj_fit_score = self.obj_fit_score[:]
        new_can.energy = self.energy
        return new_can

class Base_DTLZ(object):
    def __init__(self):
        self.decs = []
        self.objs = []

    def objectives(self):
        return []  

    def energy(self, can):
        can.objs_score = [obj.function(can) for obj in i.objs]
        return sum(can.objs_score)



    def createPopulation(self):
        count = 0
        while True:
            decs = [rand.uniform(d.low, d.high) for d in self.decs]
            one = Can(decs = decs)
            count += 1
            return one

   




class DTLZ_1(Base_DTLZ):
    def __init__(self, n=10, m=2):
        self.n = n
        self.m = m       
        self.decs = [Dec(name=d, low=0, high=1) for d in range(self.n)]
        self.objs = self.objectives
    
    def objectives(self):
        
        objectives = []

        def g(can):
            temp = 0
            for x in can.decs:
                temp += (x - 0.5)**2 - math.cos(20*math.pi*(x - 0.5))
            g = 100 * (len(can.decs) + temp)
            return g
        def f0(can):
            f_ = 0.5 * (1 + g(can))
            for p in range(self.m - 1): f_ *= can.decs[p] 
            return f_

        objectives.append(Obj(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= can.decs[q]
                f_ *= 1 - can.decs[self.m - (q+1)]
                return f_
            objectives.append(Obj(name = q, function = f))

        def fm(can):
            return 0.5 *  (1 - can.decs[0]) * (1.0 + g(can))
        
        objectives.append(Obj(name = self.m-1, function = fm))
        
        return objectives[:]

    ##//?? Do we need To String method here Shakthi


class DTLZ_3(Base_DTLZ):
    
    def __init__(self, n=10, m=2):
        self.n = n
        self.m = m       
        self.decs = [Dec(name=d, low=0, high=1) for d in range(self.n)]
        self.objs = self.objectives()

    def objectives(self):
     
        objectives = [] 

        def g(can):
            temp = 0
            for x in can.decs:
                temp += (x - 0.5)**2 - math.cos(20*math.pi*(x - 0.5))
            g = 100 * (len(can.decs) + temp)
            return g


        def f0(can):
            f_ = 0.5 * (1 + g(can))
            for p in range(self.m - 1): f_ *= math.cos(can.decs[p] * math.pi * 0.5)
            return f_
        objectives.append(Obj(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= math.cos(can.decs[r] * math.pi * 0.5)
                f_ *= math.sin( can.decs[self.m - (q+1)] * 0.5 )
                return f_
            objectives.append(Obj(name = q, function = f))


        def fm(can):
            return math.sin(can.decs[0] * math.pi * 0.5) * (1.0 + g(can))
        objectives.append(Obj(name = self.m-1, function = fm))
        
        return objectives[:]


       ## //Do we need a toString method here........


class DTLZ_5(Base_DTLZ):
    def __init__(self, n=10, m=2):
        self.n = n
        self.m = m       
        self.decs = [Dec(name=d, low=0, high=1) for d in range(self.n)]
        self.objs = self.object()

    def objectives(self):
     
        objectives = []
        
        def g(can):
            g_ = 0
            for p in range(self.m):
                g_ += (can.decs[p] - 0.5)**2
            return g_

        def theta(can, p):
            x = pi * (1 + 2 * g(can) * can.decs[p]) / (4 * (1 + g(can)))
            return x

        def f0(can):
            f_ = (1 + g(can))
            for x in range(self.m - 1):
                f_ *= math.cos( theta(can, x) * math.pi * 0.5)
            return f_

        objectives.append(Obj(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= math.cos(theta(can, r) * math.pi * 0.5)
                f_ *= math.sin( theta(can, self.m - (q+1)) * 0.5 )
                return f_
            objectives.append(Obj(name = q, function = f))

        def fm(can):
            return math.sin(theta(can, 0) * math.pi * 0.5) * (1.0 + g(can))

        objectives.append(Obj(name = self.m-1, function = fm))
        return objectives[:]

class DTLZ_7(Base_DTLZ):
    def __init__(self, n=10, m=2:
        self.n = n
        self.m = m       
        self.decs = [Dec(name=x, low=0, high=1) for x in range(self.n)]
        self.objs = self.objectives()   #

    def objectives(self):

        objectives = [] 

        def g(can):
            g = 1 + 9.0 / len(can.decs) * sum(can.decs)
            return g

        for p in range(self.m - 1):
            
            def f(can):
                return can.decs[0]
            objectives.append(Obj(name = p, function = f))

        
        def fm(can):
            summ = 0.0
            for p in range(self.m - 1):
                q_i = can.decs[p]
                summ += (q_i / (1 + g(can))) * (1 + sin(3 * pi * q_i))
            h = (self.m - summ)
            return (1 + g(can)) * h

        objectives.append(Obj(name = self.m-1, function = fm))
        
        return objectives[:]
    
    # TODO: Need to implement toString method for printing and debugging


if __name__ == '__main__':
    dtl_1 = DTLZ_1(6, 3)
    print(dtl_1)