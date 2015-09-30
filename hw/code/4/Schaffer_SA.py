__author__ = 'Nakul'

import math
import random



def init_energy():

    xmax, xmin =schaffer_baseline()
    emax = float((((xmax*xmax)+(xmax-2)*(xmax-2))-xmin)/(xmax-xmin))

    return (xmax,xmin,emax)

def compute_energy(x, xmax, xmin, emax):

    f1 = x*x
    f2 = (x-2)*(x-2)
    e = float(((f1+f2)-xmin)/(xmax-xmin))
    energy = float(e/emax)
    # print 'emax = %d' % emax

    return energy

def schaffer_baseline():

    xmin = 100000
    xmax = 0
    for i in range(0, 1000):

        x = random.randint(0, pow(10, 5))
        if x < xmin:
            xmin = x

        if x > xmax:
            xmax = x

        #   print 'f1+f2 = %d\n' % (f1+f2)
        # print 'x=%d' % x
    # print 'xmax = %d\n' % xmax
    # print 'xmin = %d\n' % xmin

    return (xmax,xmin)

def probab(p,q, t):
    p = pow(math.e,(p-q)/t)

    return p

def anneal():
    xmax,xmin,emax = init_energy()
    s = random.randint(xmin, xmax)
    e = compute_energy(s,xmax,xmin, emax)
    sb = s
    eb = e
    count = 1
    while count < 10000 and e < (emax/emax):
        temp = (count/float(1000))
        sn = s + random.randint(-10,10)
        en = compute_energy(sn, xmax, xmin,emax)
        if en < eb:
            sb = sn
            eb = en
            print '!',
        if en < e:
            s= sn
            e= en
            print '+',
        elif probab(e, en, temp) < random.random():

            s= sn
            e= en
            print '?',
        print ".",
        count = count + 1
        if (count % 25 == 0):
            print '%d\n' % eb


anneal()