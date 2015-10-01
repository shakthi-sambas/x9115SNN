__author__ = 'Nakul'

import math
import random

fmin = 0
fmax = 0


def ener_calc(x, normalize):

    f1 = math.pow(x,2)
    f2 = math.pow((x-2),2)

    if normalize:
        return ((f1+f2) - fmin)/(fmax - fmin)
    else:
        return f1+f2




def schaffer_baseline():

    global fmin
    global fmax
    x = random.randint(0, pow(10,5))
    fmin = fmax = ener_calc(x, False)
    for i in range(0, 100):

        x = random.randint(0, pow(10, 5))
        fx= ener_calc(x,False)
        if fx < fmin:
            fmin = fx

        if fx > fmax:
            fmax = fx


    print (fmax,fmin)

def probab(oldE,newE, temp):

    p = pow(math.e,(oldE-newE)/temp)
    # print (p)
    return p

def anneal():

    schaffer_baseline()
    s_init = random.randint(0, pow(10,5))
    e_init = ener_calc(s_init, True)
    print (e_init)
    sb = s_init
    eb = e_init
    emax = -1
    count = 1
    while count < 1000 and e_init > emax:
        temp = (count/float(1000))
        sn = random.randint(0, pow(10, 5))
        en = ener_calc(sn, True)
        # print (en,eb)
        if en < eb:
            sb = sn
            eb = en
            print '!',
        if en < e_init:
            s= sn
            e= en
            print '+',
        elif probab(e_init, en, temp) < random.random():

            s_init = sn
            e_init = en
            print '?',
        print ".",
        count = count + 1
        if (count % 25 == 0):
            print '%d\n' % float(eb)


anneal()