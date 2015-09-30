__author__ = 'Nakul'

import math
import random


xmin = 100000
xmax = 0

def compute_energy(x):

    f1 = x*x
    f2 = (x-2)*(x-2)
    emax = (((xmax*xmax)+(xmax-2)*(xmax-2))-xmin)/(xmax-xmin)
    e = ((f1+f2)-xmin)/(xmax-xmin)
    energy = e/emax
    # print 'emax = %d' % emax
    return energy

def schaffer_baseline():


    for i in range(0, 1000):

        x = random.randint(0, pow(10, 5))
        if x < xmin:
            xmin = x

        if x > xmax:
            xmax = x

        #   print 'f1+f2 = %d\n' % (f1+f2)
        print 'x=%d' % x
    # print 'xmax = %d\n' % xmax
    # print 'xmin = %d\n' % xmin


def anneal():

    return
schaffer_baseline()