from __future__ import division
import random
import math


x = [None] * 6


def f1(x):

    return -((25(x[0]-2)**2) + ((x[1] - 2)**2) + ((x[2]-1)**2) * ((x[3]-4)**2) + ((x[4]-1)**2))

def f2(x):

    return x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2 +x[5]**2


def combined_maxwalksat_values (x, normalize = False, min_val=None, max_val=None):
	combined_value = f1(x) + f2(x)
	if normalize:
		return abs((combined_value - min_val)/(max_val-min_val))
	else:
		return combined_value

def check_constraints(x):

    if (x[0]+x[1] - 2) >= 0:
        flag = 1
    else:
        return False

    if (6 - x[0]-x[1]) >= 0:
        flag = 1
    else:
        return False
    if (2 - x[1]+x[0]) >= 0:
        flag = 1
    else:
        return False
    if (2 - x[0] + 3*x[1]) >= 0:
        flag = 1
    else:
        return False
    if (4 - (x[2] - 3)**2 - x[3]) >= 0:
        flag = 1
    else:
        return False
    if((x[4] - 3)**3 + x[5] - 4) >= 0:
        flag= 1
    else:
        return False

    if (flag == 1):
        return True


