import math
from copy import deepcopy
import random as rand
from util import *

//We can either use this wrapper classes or we can use gadget classes 




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
        new_can = Candidate()
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

   




class DTLZ_1(base_DTLZ):
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
                temp += (x - 0.5)**2 - cos(20*pi*(x - 0.5)) 
            g = 100 * (len(can.decs) + temp)
            return g
        def f0(can):
            f_ = 0.5 * (1 + g(can))
            for p in range(self.m - 1): f_ *= can.decs[p] 
            return f_

        objectives.append(Objective(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= can.decs[q]
                f_ *= 1 - can.decs[self.m - (q+1)]
                return f_
            objectives.append(Objective(name = q, function = f))

        def fm(can):
            return 0.5 *  (1 - can.decs[0]) * (1.0 + g(can))
        
        objectives.append(Objective(name = self.m-1, function = fm))   
        
        return objectives[:]

    //?? Do we need To String method here Shakthi


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
                temp += (x - 0.5)**2 - cos(20*pi*(x - 0.5)) 
            g = 100 * (len(can.decs) + temp)
            return g


        def f0(can):
            f_ = 0.5 * (1 + g(can))
            for p in range(self.m - 1): f_ *= cos(can.decs[p] * pi * 0.5)
            return f_
        objectives.append(Objective(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= cos(can.decs[r] * pi * 0.5)
                f_ *= sin( can.decs[self.m - (q+1)] * 0.5 )
                return f_
            objectives.append(Objective(name = j, function = f))


       def fm(can):
            return sin(can.decs[0] * pi * 0.5) * (1.0 + g(can))
        objectives.append(Objective(name = self.m-1, function = fm))
        
        return objectives[:]


        //Do we need a toString method here........


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
                f_ *= cos( theta(can, x) * pi * 0.5)
            return f_

        objectives.append(Objective(name = 0, function = f0))

        for q in range(1, self.m - 1):
            def f(can):
                f_ = 0.5 * (1 + g(can))
                for r in range(self.m - (q+1)):
                    f_ *= cos(theta(can, r) * pi * 0.5)
                f_ *= sin( theta(can, self.m - (q+1)) * 0.5 )
                return f_
            objectives.append(Objective(name = q, function = f))

        def fm(can):
            return sin(theta(can, 0) * pi * 0.5) * (1.0 + g(can))

        objectives.append(Objective(name = self.m-1, function = fm))
        return objectives[:]



if __name__ == '__main__':
    dtl_1 = DTLZ_1(6, 3)
    print(dtl_1)