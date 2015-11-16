from __future__ import division
import random
import sys
import math

class Instance():
	MAX = MIN = 0
	min_base_value = max_base_value = 0

	def __init__(self, number_variables=0, min_bound=[0], max_bound=[0]):
		self.MIN = -1000000
		self.MAX = 1000000
		self.MAX_BOUND = max_bound
		self.MIN_BOUND = min_bound
		self.number_variables = number_variables

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
		self.number_variables = 1

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
		self.number_variables = 6

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
		self.number_variables = 3

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

class Golinski(Instance):
	variable_upper_bound = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
	variable_lower_bound = [2.6, 0,7, 17.0, 7.3, 7.3, 2.9, 5.0]

	def __init__(self):
		self.MIN_BOUND = self.variable_lower_bound
		self.MAX_BOUND = self.variable_upper_bound
		self.number_variables = 7

	def f1(self, x):
		return 0.7854 * x[0] * (x[1]**2) * (10*(x[2]**2)/3 + 14.933*x[2] - 43.0934) - 1.508 * x[0] * (x[5]**2 + x[6]**2) + 7.477 * (x[5]**3 + x[6]**3) + 0.7854 * (x[3] * (x[5] ** 2) + x[4] * (x[6] ** 2))

	def f2(self, x):
		x = self.check_validity(x)
		return ((745 * x[3] / (x[1] * x[2])) ** 2 + 1.69 * 10 ** 7) ** 0.5 / (0.1 * x[5] ** 3)

	def combined_function_values(self, sol):
		return self.f1(sol) + self.f2(sol)

	def generate_random_solution(self):
		while True:
  			random_solution = []
  			for low, high in zip(self.variable_lower_bound, self.variable_upper_bound):
  				random_num = random.uniform(low, high)
  				# if random_num == 0.0:
  				# 	break
  				# 	random_solution = []
  				# else:
  				random_solution.append(random_num)
  			ok, random_solution = self.constraint_check(random_solution)
			if ok:
				return random_solution
  	
  	def check_validity(self, x):
  		for n,i in enumerate(x):
  			if i == 0.0:
  				while x[n] == 0.0:
  					x[n] = random.uniform(self.variable_lower_bound[n], self.variable_upper_bound[n])
  		return x

  	def constraint_check(self, x):
  		constraints = []
  		x = self.check_validity(x)
  		constraints.append(((x[0] * (x[1] ** 2) * x[2]) ** -1 - 27 ** -1) <= 0)
  		constraints.append(((x[0] * (x[1] ** 2) * (x[2] ** 2)) ** -1 - 397.5 ** -1) <= 0)
  		constraints.append(((x[3] ** 3/(x[1] * x[2] ** 2 * x[5] ** 4)) - 1.93 ** -1) <= 0)
  		constraints.append(x[4] ** 3/(x[1] * x[2] * x[6] ** 4) - 1/1.93 <= 0)
  		constraints.append(x[1] * x[2] <= 0)
  		constraints.append((x[0] / x[1]) - 12 <= 0)
  		constraints.append(5 - (x[0] / x[1]) <= 0)
  		constraints.append(1.9 - x[3] + 1.5 * x[5] <= 0)
  		constraints.append(1.9 - x[4] + 1.1 * x[6] <= 0)
  		constraints.append(self.f2(x) <= 1300)
  		constraints.append((((745 * x[4]/(x[1] * x[2])) ** 2 + 1.575 * 10**8) ** 0.5) /(0.1 * x[6] ** 3) <= 1100)
  		return min(constraints) >= 0, x

  	def mutate(self, sol, index):
  		while True:
  			sol[index] = random.uniform(self.variable_lower_bound[index], self.variable_upper_bound[index])
  			if sol[index] != 0.0:
  				# print sol
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
	print_string = ' '

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
			print_string += '! '
		if en < e:
			s = sn 
			e = en
			print_string += '+ '
		elif P(e, en, (1 - k/kmax)) > random.random():
			s = sn
			e = en
			print_string += '? '
		else:
			print_string += '. '
		if k % 25 == 0:
			print ("%3d : %0.7f ||   %s" % (k, 1-eb, print_string))
			print_string = ' '
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
		# print str(counter)+ ' '+ str(be) + ' ' + print_string
		print ("%3d : %0.7f ||   %s" % (counter, be, print_string))

def de(model, num_candidates=100, max_repeats=100, f=0.75, cf=0.3, epsilon=0.01):
	# generate initial frontier
	# select 3 
	# probability
	
	model = model()
	model.get_baseline(1000)
	
	def candidate():
		candidate_solution = model.generate_random_solution()
		while not model.constraint_check(candidate_solution):
			candidate_solution = model.generate_random_solution()
		return candidate_solution

	def select_three_randomly(sol_index):
		random_three = []

		while len(random_three) < 3:
			random_pick = random.randint(0, num_candidates-1)
			if random_pick != sol_index and random_pick not in random_three: 
				random_three.append(random_pick)
		return random_three

	def evolve(random_three):
		while True:
			new_sol = []

			for i in range (0, model.number_variables):
				try:
					min_bound = model.MIN_BOUND[i]
					max_bound = model.MAX_BOUND[i]
				except:
					min_bound = model.MIN_BOUND[0]
					max_bound = model.MAX_BOUND[0]
				new = frontier[random_three[0]][i] + f * (frontier[random_three[1]][i] - frontier[random_three[2]][i]) 

				new_sol.append(max(min_bound, min(new, max_bound))) 
			# if model.constraint_check(new_sol):
			return new_sol


	frontier = [candidate() for _ in range(num_candidates)]

	print 'Differential Evolution Starting for ' + model.model_name()
	
	
	k = 0
	eb = 1

	sn = en = None

	while True:
		print_string = ''
		k += 1
		for n, parent in enumerate(frontier):
			
			e = model.normailzed_energy(parent)
			sn = evolve(select_three_randomly(n))
			en = model.normailzed_energy(sn)

			if en < eb:
				sb,  eb = sn, en

				print_string += '!'
			if en < e:
				frontier[n] = sn
				print_string += '+'
			else:
				print_string += '.'
		print ("%3d : %0.7f ||   %s" % (k, 1-eb, print_string))
		if k > max_repeats-1:
			break

for model in [Golinski, Schaffer, Osyczka2, Kursawe]:  
  for optimizer in [de]:
     optimizer(model)
     print ''
