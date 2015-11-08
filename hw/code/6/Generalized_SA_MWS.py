from __future__ import division
import random
import sys
import math

class Instance():
	MAX = MIN = 0
	min_base_value = max_base_value = 0

	def __init__(self, min_bound=[0], max_bound=[0]):
		self.MIN = -1000000
		self.MAX = 1000000
		self.MAX_BOUND = max_bound
		self.MIN_BOUND = min_bound

	def model_name(self):
		return self.__class__.__name__

	def get_baseline(self, tries):
		self.min_base_value = self.MAX ** 2
		self.max_base_value = self.MIN

		for i in range (0, tries):
			while True:
				sol = self.generate_random_solution()
				if self.constraint_check(sol):
					break
			current_value = self.combined_function_values(sol)
			if current_value < self.min_base_value:
				self.min_base_value = current_value
			if current_value > self.max_base_value:
				self.max_base_value = current_value
		# print self.min_base_value, self.max_base_value
		return self.min_base_value, self.max_base_value
	
	def normailzed_energy(self, sol):
		current_value = self.combined_function_values(sol)
		normailzed_energy = abs((current_value - self.min_base_value)/ (self.max_base_value - self.min_base_value))
		return normailzed_energy

	def choose_max(self, sol, index, steps):
	    sub_counter = 0 
	    bs = copy = sol
	    if index > len(self.MAX_BOUND) - 1:
	    	index = len(self.MAX_BOUND) - 1
	    diff_bw_two_sol = (self.MAX_BOUND[index] - self.MIN_BOUND[index]) / steps
	    for step in range(0, steps):
	        sub_counter = sub_counter + 1
	        copy[index] = self.MIN_BOUND[index] + diff_bw_two_sol*step
	        if self.constraint_check(copy):
	            if self.normailzed_energy(copy) > self.normailzed_energy(bs):
	                bs = copy
	    return [bs, sub_counter]

	def mutate(self, sol, index):
		return True
	########################################
	#Fucnctions to be defined by subclasses#
	########################################

	def constraint_check (self, sol):
		return True

	def generate_random_solution(self):
		return True

	def combined_function_values(self, sol):
		return True

	def mutate(self, sol, index):
		return True



class Schaffer(Instance):
	def __init__(self, min_bound=-10**5, max_bound=10**5): 
		self.MIN_BOUND= [min_bound]
		self.MAX_BOUND= [max_bound]

	def f1(self, x):
		return x**2

	def f2(self, x):
		return (x-2)**2

	def generate_random_solution(self):
		return [random.randint(self.MIN_BOUND[0], self.MAX_BOUND[0])]

	def combined_function_values(self, sol):
		return self.f1(sol[0]) + self.f2(sol[0])

	def mutate(self, sol, index=None):
		return self.generate_random_solution()

	



class Osyczka2(Instance):
	variable_upper_bound = [10,10,5,6,5,10]
	variable_lower_bound = [0,0,1,0,1,0]

	def __init__(self):
		self.MIN_BOUND= self.variable_lower_bound
		self.MAX_BOUND= self.variable_upper_bound

	def f1(self, x):
	    return (-((25*((x[0]-2)**2)) + ((x[1] - 2)**2) + (((x[2]-1)**2) * ((x[3]-4)**2)) + ((x[4]-1)**2)))

	def f2(self, x):
		return x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2 +x[5]**2

	def combined_function_values(self, sol):
		return self.f1(sol) + self.f2(sol)

  	def constraint_check (self, sol):
  		constraints = []
  		constraints.append(sol[0] + sol[1] - 2)
  		constraints.append(6 - sol[0] - sol[1])
  		constraints.append(2 - sol[1] + sol[0])
  		constraints.append(2 - sol[0] + 3 * sol[1])
  		constraints.append(4 - (sol[2] - 3) ** 2 - sol[3])
  		constraints.append((sol[4] - 3) ** 3 + sol[5] - 4)
  		return min(constraints) >= 0 

  	def generate_random_solution(self):
  		while True:
  			random_solution = []
  			for low, high in zip(self.variable_lower_bound, self.variable_upper_bound):
  				random_num = random.randrange(low, high)
  				random_solution.append(random_num)
  			if self.constraint_check(random_solution):
  				return random_solution

  	def mutate(self, sol, index):
  		sol[index] = random.randrange(self.variable_lower_bound[index], self.variable_upper_bound[index])
  		return sol


class Kursawe(Instance):
	def __init__(self, min_bound=-5, max_bound=5):
 		self.MIN_BOUND= [min_bound]
		self.MAX_BOUND= [max_bound]

	def f1(self, x):
		x1,x2,x3 = x[0], x[1], x[2] 
		t1 = math.sqrt(x1**2+x2**2)
		t2 = math.sqrt(x2**2+x3**2)
		return -10*(math.exp(-0.2*t1)+math.exp(-0.2*t2))

	def f2(self, x, a=1, b=1):
		return sum( (abs(i)**a + 5* math.sin(i)**b) for i in x)

	def combined_function_values(self, sol):
		return self.f1(sol) + self.f2(sol)

  	def generate_random_solution(self):
  		return [random.randint(self.MIN_BOUND[0], self.MAX_BOUND[0]) for x in range(0,3)]

  	def mutate(self, sol, index=None):
  		sol[index] = random.randint(self.MIN_BOUND[0], self.MAX_BOUND[0])
  		return sol


def sa(model, MIN=0, MAX=0, epsilon = 0.9, kmax = 1000):
	emax = 0.1-epsilon
	model = model()
	model.get_baseline(100)

	sv = model.generate_random_solution()
	sb = sv
	e = model.normailzed_energy(sv)
	eb = e

	s = sv
	k = 1
	print_string = ''

	print 'Simulated Annealing Starting for ' + model.model_name()

	def P(e, en, depth):
		return math.exp((e - en)/depth**5)
	
	while k < kmax and e > emax:
		# print 'in '
		sn = model.generate_random_solution()
		en = model.normailzed_energy(sn)

		if en<eb:
			sb = sn
			eb = en
			print_string += '!'
		if en < e:
			s = sn 
			e = en
			print_string += '+'
		elif P(e, en, (1 - k/kmax)) > random.random():
			s = sn
			e = en
			print_string += '?'
		else:
			print_string += '.'
		if k % 25 == 0:
			print ("%3d : %0.7f ||   %s" % (k, 1-eb, print_string))
			print_string = ''
			e = 1
		k += 1

def mws(model, trials=100, max_changes=30, p = 0.5, threshold = 5.0, step=10):
	model = model()
	counter = sub_counter = 0
	model.get_baseline(10000)

	bs = model.generate_random_solution()
	be = model.normailzed_energy(bs)

	ls, le = bs, be

	print 'MaxWalkSat Starting for ' + model.model_name()

	for i in range(0, trials):
		print_string = ''
		cs = model.generate_random_solution()

		for j in range (0, max_changes):
			trial_outcome = ''
			if model.normailzed_energy(cs) > threshold:
				print 'Threshold Reached!'
				print 'Solution: '
				print cs
				return cs
			random_index = random.randint(0, len(cs)-1)
			# print random_index
			if p < random.random():
				ds = cs
				ds = model.mutate(ds, random_index) #mutate here ds = mutate(ds, random_index)
				counter +=1
				if model.constraint_check(ds):
					cs = ds
					trial_outcome = '?'
					# print "not here"
				else:
					trial_outcome = '.'
			else:
				cs, sub_counter = model.choose_max(cs, random_index, step)
				ce = model.normailzed_energy(cs)
				counter += 1
				if ce > be:
					trial_outcome = '!'
					bs, be = cs, ce
				elif ce > le:
					trial_outcome = '+'
				else:
					trial_outcome = '.'
				ls, le = cs, ce
			print_string += ' ' + trial_outcome
		print str(counter)+ ' '+ str(be) + ' ' + print_string



for model in [Schaffer, Osyczka2, Kursawe]:  
  for optimizer in [sa, mws]:
     optimizer(model)
     print ''