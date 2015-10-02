from __future__ import division
import random
import sys
import math

MAX = 1000000
MIN = -1000000

def f1(x):
	return x**2

def f2(x):
	return (x-2)**2

def combined_schaffer_values(x, normalize = False, min_val=None, max_val=None):
	combined_value = f1(x) + f2(x)
	if normalize:
		return abs((combined_value - min_val)/(max_val-min_val))
	else:
		return combined_value 

def base_schaffer():
	min_base_schaffer_value = MAX ** 2
	max_base_schaffer_value = MIN
	for i in range(0, 100):
		current_value = combined_schaffer_values(random.randint(MIN, MAX))
		if current_value < min_base_schaffer_value:
			min_base_schaffer_value = current_value
		if current_value > max_base_schaffer_value:
			max_base_schaffer_value = current_value
	return min_base_schaffer_value, max_base_schaffer_value

def P(e, en, depth):
	return math.exp((e - en)/ depth**5)

def schaffer():
	epsilon = 1.1
	kmax = 1000
	emax = 1 - epsilon
	min_base_schaffer_value, max_base_schaffer_value = base_schaffer()
	
	sv = random.randint(MIN, MAX)
	sb = sv
	e = combined_schaffer_values(sv, True, min_base_schaffer_value, max_base_schaffer_value)
	eb = e

	s = sv
	k = 1
	print_string = ''
	while k < kmax and e > emax:
		sn = random.randint(MIN, MAX)
		en = combined_schaffer_values(sn, True, min_base_schaffer_value, max_base_schaffer_value)

		if en < eb:
			sb = sn
			eb = en
			print_string += "!" 

		if en < e:
			s = sn 
			e = en
			print_string += "+"

		elif  P(e, en, (1- k/kmax)) > random.random():
			s = sn
			e = en
			print_string += "?"
		else:
			print_string += "."

		if k % 25 == 0:
			print ("%3d : %0.7f ||   %s" % (k, eb, print_string))
			print_string = ''
			e = 1

		k += 1

schaffer()
	
