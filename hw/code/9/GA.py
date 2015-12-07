from __future__ import division
import matplotlib.pyplot as plt

import random
import sys
import math
import sk
PI = math.pi

class Instance():
	MAX = 1000000
	MIN = -1000000
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
		self.min_energy_value = self.MAX ** 2
		self.max_energy_value = self.MIN
		# print self.min_energy_value
		# print self.max_energy_value
		# for i in range (0, tries):
		# 	while True:
		# 		sol = self.generate_random_solution()
		# 		if self.constraint_check(sol):
		# 			break
			
		# 	current_energy = self.normailzed_energy(sol)
		# 	if current_energy < self.min_energy_value:
		# 		self.min_energy_value = current_energy
		# 	if current_energy > self.max_energy_value:
		# 		self.max_energy_value = current_energy
		# return self.min_energy_value, self.max_energy_value
		for i in range(100):
			random_solution = self.generate_random_solution()
			energy_value = self.combined_function_values(random_solution)

			if energy_value < self.min_energy_value:
				self.min_energy_value = energy_value
			if energy_value > self.max_energy_value:
				self.max_energy_value = energy_value
		return self.max_energy_value, self.min_energy_value   


	def normailzed_energy(self, sol):
		current_value = self.combined_function_values(sol)
		normailzed_energy = abs((current_value - self.min_energy_value)/ (self.max_energy_value - self.min_energy_value))
		return normailzed_energy

	def get_objective_values(self, solution):
		assert False, 'Implement get_objective_values in subclass'

	def type1(self, solution, state_best):
		solution_objective_list = self.get_objective_values(solution)
		state_best_objective_list = self.get_objective_values(state_best)

		for i, j in zip(solution_objective_list, state_best_objective_list):
			if i > j:
				return False
		return True

	def get_objectives_list(self, era_list=[]):
		objectives_list = []
		for value in era_list:
			for objective in self.objectives:
				objectives_list.append(objective(value))
		return objectives_list

	def type2_comparison(self, current_era, previous_era):
		curr_era_objectives = self.get_objectives_list(current_era)
		prev_era_objectives = self.get_objectives_list(previous_era)
		# print sk.a12(curr_era_objectives, prev_era_objectives)
		if (sk.a12(curr_era_objectives, prev_era_objectives) > 0.08):
			return 5
		return -1

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

class DTLZ7(Instance):
	def __init__(self, num_decisions, num_objectives):
		self.num_decisions = num_decisions
		self.num_objectives = num_objectives
		self.MIN_BOUND = [0.0 for _ in range (self.num_decisions)]
		self.MAX_BOUND = [1.0 for _ in range (self.num_decisions)]
		self.number_variables = self.num_decisions
		self.objectives = self.get_objectives()
	
	def func_g(self, value):
		sol=0.0
		for i in range(0, self.number_variables):
			sol += value[i]
		return 9*sol/self.number_variables

	def func_h(self, f, g_value, value):
		sol=0.0

		for i in range(0, self.num_objectives - 1):
			sol += (f[i](value) / (1 + g_value)) * (1 + math.sin(3 * math.pi * f[i](value)))
		
		return self.num_objectives - sol

	def last_obj(self, value, f):
		g_value = 1 + self.func_g(value)
		res = (1 + g_value) * self.func_h(f, g_value, value)
		return res

	def objective_value(self, value, index):
		return value[index]

	def get_objective_values(self, solution):
		objective_values_list = []
		for i in self.objectives:
			objective_values_list.append(i(solution))
		return objective_values_list

	def get_objectives(self):
		objectives_list = [None] * self.num_objectives

		for i in range(0, self.num_objectives):
			objectives_list[i] = lambda value : self.objective_value(value, i)
		objectives_list[self.num_objectives - 1] = lambda value : self.last_obj(value, objectives_list)

		return objectives_list

	def combined_function_values(self, sol, e=0):
		for objective in self.get_objectives():
			e += objective(sol)
		return e

	def generate_random_solution(self):
  		while True:
  			random_solution = []
  			for low, high in zip(self.MIN_BOUND, self.MAX_BOUND):
  				random_num = random.uniform(low, high)
  				random_solution.append(random_num)
  			if self.constraint_check(random_solution):
  				# print random_solution
  				return random_solution

  	def mutate(self, sol, index):
  		sol[index] = random.uniform(self.MIN_BOUND[index], self.MAX_BOUND[index])
  		return sol

class DTLZ5(Instance):
	def __init__(self, num_decisions, num_objectives):
		self.num_decisions = num_decisions
		self.num_objectives = num_objectives
		self.MIN_BOUND = [0.0 for _ in range (self.num_decisions)]
		self.MAX_BOUND = [1.0 for _ in range (self.num_decisions)]
		self.number_variables = self.num_decisions
		self.objectives = self.get_objectives()
	
	def func_g(self, value):
		sol=0.0
		for i in range(0, self.number_variables):
			sol += math.pow(value[i] -  0.5, 2)
		return sol

	def func_h(self, f, g_value, value):
		sol=0.0

		for i in range(0, self.num_objectives - 1):
			sol += (f[i](value) / (1 + g_value)) * (1 + math.sin(3 * math.pi * f[i](value)))
		
		return self.num_objectives - sol

	def last_obj(self, value, f):
		g_value = 1 + self.func_g(value)
		res = (1 + g_value) * self.func_h(f, g_value, value)
		return res

	def objective_value(self, value, index):
		result = 1 + self.func_g(value)
		for i in range(0, self.num_objectives - (index + 1)):
			result *= math.cos(self.theta(value, i) * PI * 0.5)
		if (index != 0):
			result *= math.sin(self.theta(value, self.num_objectives - (index + 1)) * PI * 0.5)
		return result
	
	def theta(self, value, index):
		if (index == 0):
			return value[0]
		else:
			value_g = self.func_g(x) 
			return (1 / (2 * (1 + value_g))) + ((value_g * value[index]) / (1 + value_g))

	def get_objective_values(self, solution):
		objective_values_list = []
		for i in self.objectives:
			objective_values_list.append(i(solution))
		return objective_values_list

	def get_objectives(self):
		objectives_list = [None] * self.num_objectives

		for i in range(0, self.num_objectives ):
			objectives_list[i] = lambda value : self.objective_value(value, i)
		
		return objectives_list

	def combined_function_values(self, sol, e=0):
		for objective in self.get_objectives():
			e += objective(sol)
		return e

	def generate_random_solution(self):
  		while True:
  			random_solution = []
  			for low, high in zip(self.MIN_BOUND, self.MAX_BOUND):
  				random_num = random.uniform(low, high)
  				random_solution.append(random_num)
  			if self.constraint_check(random_solution):
  				# print random_solution
  				return random_solution

  	def mutate(self, sol, index):
  		sol[index] = random.uniform(self.MIN_BOUND[index], self.MAX_BOUND[index])
  		return sol

class DTLZ3(Instance):
	def __init__(self, num_decisions, num_objectives):
		self.num_decisions = num_decisions
		self.num_objectives = num_objectives
		self.MIN_BOUND = [0.0 for _ in range (self.num_decisions)]
		self.MAX_BOUND = [1.0 for _ in range (self.num_decisions)]
		self.number_variables = self.num_decisions
		self.objectives = self.get_objectives()
	
	def func_g(self, value):
		sol=0.0
		for i in range(0, self.number_variables):
			sol += math.pow(value[i] - 0.5, 2) - math.cos(20 * PI * (value[i] - 0.5))
		return 100* (sol + self.number_variables)

	def objective_value(self, value, index):
		result = 1 + self.func_g(value)
		for j in range(0, self.num_objectives - (index + 1)):
			result *= math.cos(value[j] * PI * 0.5)
		if (index != 0):
			result *= math.sin(value[self.num_objectives - (index + 1)] * PI * 0.5)
		return result

	def get_objective_values(self, solution):
		objective_values_list = []
		for i in self.objectives:
			objective_values_list.append(i(solution))
		return objective_values_list

	def get_objectives(self):
		objectives_list = [None] * self.num_objectives

		for i in range(0, self.num_objectives):
			objectives_list[i] = lambda value : self.objective_value(value, i)
		return objectives_list

	def combined_function_values(self, sol, e=0):
		for objective in self.get_objectives():
			e += objective(sol)
		return e

	def generate_random_solution(self):
  		while True:
  			random_solution = []
  			for low, high in zip(self.MIN_BOUND, self.MAX_BOUND):
  				random_num = random.uniform(low, high)
  				random_solution.append(random_num)
  			if self.constraint_check(random_solution):
  				# print random_solution
  				return random_solution

  	def mutate(self, sol, index):
  		sol[index] = random.uniform(self.MIN_BOUND[index], self.MAX_BOUND[index])
  		return sol


class DTLZ1(Instance):
	def __init__(self, num_decisions, num_objectives):
		self.num_decisions = num_decisions
		self.num_objectives = num_objectives
		self.MIN_BOUND = [0.0 for _ in range (self.num_decisions)]
		self.MAX_BOUND = [1.0 for _ in range (self.num_decisions)]
		self.number_variables = self.num_decisions
		self.objectives = self.get_objectives()
	
	def func_g(self, value):
		sol=0.0
		for i in range(0, self.number_variables):
			sol += math.pow(value[i] - 0.5, 2) - math.cos(20 * PI * (value[i] - 0.5))
		return 100* (sol + self.number_variables)

	def objective_value(self, value, index):
		result = 0.5*(1 + self.func_g(value))
		for j in range(0, self.num_objectives - (index + 1)):
			result *= value[j]
		if (index != 0):
			result *= 1-value[self.num_objectives - (index +1)]
		return result

	def get_objective_values(self, solution):
		objective_values_list = []
		for i in self.objectives:
			objective_values_list.append(i(solution))
		return objective_values_list

	def get_objectives(self):
		objectives_list = [None] * self.num_objectives

		for i in range(0, self.num_objectives):
			objectives_list[i] = lambda value : self.objective_value(value, i)
		return objectives_list

	def combined_function_values(self, sol, e=0):
		for objective in self.get_objectives():
			e += objective(sol)
		return e

	def generate_random_solution(self):
  		while True:
  			random_solution = []
  			for low, high in zip(self.MIN_BOUND, self.MAX_BOUND):
  				random_num = random.uniform(low, high)
  				random_solution.append(random_num)
  			if self.constraint_check(random_solution):
  				# print random_solution
  				return random_solution

  	def mutate(self, sol, index):
  		sol[index] = random.uniform(self.MIN_BOUND[index], self.MAX_BOUND[index])
  		return sol

def ga(model, num_decisions, num_objectives, population_size = 100, mutation_probability=0.5, crossover_probability=0.9, max_generations=1000):

	# make initial population sample
	# make selection.

	model = model(num_decisions, num_objectives)
	print model.model_name()
	model.get_baseline(100)
	era = 100

	print "Running GA for : " + model.model_name() + "  for " + str(num_decisions) + "  Decisions and " + str(num_objectives) + "  Objectives"

	def make_initial_population_sample():
		population_list=[]
		for i in range(population_size):
			while True:
				random_candidate = model.generate_random_solution()
				if model.constraint_check(random_candidate):
					break

			population_list.append(random_candidate)
		return population_list
		
	initial_population = make_initial_population_sample()

	def fittest_selection(population, base_population):
		fittest_candidates_number_list = []
		dominated_candidates_number_list = []
		dominated_population = []
		# print len(population)
		for candidate_one in range(len(population) - 1):
			if candidate_one not in dominated_candidates_number_list:
				for candidate_two in range (len(population) - 1):
					if candidate_one != candidate_two and model.type1(population[candidate_one], population[candidate_two]):
						if candidate_one not in fittest_candidates_number_list:
							fittest_candidates_number_list.append(candidate_one)
						if candidate_two not in dominated_candidates_number_list:
							dominated_candidates_number_list.append(candidate_two)
							dominated_population.append(population[candidate_two])
						try:
							fittest_candidates_number_list.remove(candidate_two)
						except:
							pass
		return fittest_candidates_number_list, dominated_population
	
	def get_fittest_selection(population, base_population):
		fittest_candidates_number_list, dominated_population = fittest_selection(population, base_population)
		# # print dominated_population
		# required_population = (0.2 * len(population)) 
		# while True:
		# 	if (len(fittest_candidates_number_list) < required_population):
		# 		now_fittest, dominated_population = fittest_selection(dominated_population, base_population)
		# 		for i in now_fittest:
		# 			if (len(fittest_candidates_number_list) < required_population) and i not in fittest_candidates_number_list:
		# 				fittest_candidates_number_list.append(i)
		# 	else:
		# 		break
		if len(fittest_candidates_number_list)<20:
			while True:
				random_index = random.randint(0, len(population)-1)
				if random_index not in fittest_candidates_number_list:
					fittest_candidates_number_list.append(random_index)
				if len(fittest_candidates_number_list) == 20:
					break
		return fittest_candidates_number_list

	def crossover(parents):
		mom = initial_population[parents[0]]
		dad = initial_population[parents[1]]
		child = dad
		random_crossover_point = random.randint(0, len(initial_population[parents[0]]))
		child[random_crossover_point:] = mom[random_crossover_point:]
		return child

	def mutate(kid):
		for i in range(model.number_variables):
			random_prob = random.random()
			if random_prob < mutation_probability:
				# print "mutating"
				# print kid
				lower_bound, upper_bound = model.MIN_BOUND[i], model.MAX_BOUND[i]
				kid[i] = random.uniform(lower_bound, upper_bound)
				# print kid
		return kid

	def get_population(candidates):
		population = []
		for i in candidates:
				population.append(initial_population[i])
		return population

	def plot(population, maxX=True, maxY=True):
		x = []
		for child in population:
			x.append(model.normailzed_energy(child))
		y = []
		for i in x:
			y_value = 4 - (i * (1 + math.sin(3*PI*i)))
			y.append(y_value)
		sorted_list = sorted([[x[i], y[i]] for i in range(len(x))], reverse=False)
		pareto_front = [sorted_list[0]]
		
		for pair in sorted_list[1:]:
			if maxY:
				if pair[1] < pareto_front[-1][1]:
					pareto_front.append(pair)
			else:
				if pair[1] >= pareto_front[-1][1]:
					pareto_front.append(pair)
		'''Plotting process'''
		
		for j, k in zip(x, y):
			# print j, k
			plt.scatter(x, y)	
		# pf_X = [pair[0] for pair in pareto_front]
		# pf_Y = [pair[1] for pair in pareto_front]
		# plt.plot(pf_X, pf_Y)
		plt.xlabel("Objective 1")
		plt.ylabel("Objective 2")
		plt.show()


	
	base_population = initial_population
	best_solution = initial_population[0]
	min_energy = model.combined_function_values(best_solution)

	for generation in range(max_generations):
		fittest_candidates = get_fittest_selection(initial_population, base_population)
		# print (fittest_candidates)

		next_generation_population = get_population(fittest_candidates)

		new_kids = []

		########################
		#Crossover and Mutation#
		########################

		child = []
		while True:
			parents = random.sample(set(fittest_candidates), 2)

			if crossover_probability > random.random():
				crossovered_child = crossover(parents)
				# print crossovered_child  
				child = mutate(crossovered_child)
				if crossovered_child == child:
					pass
					# print "mutation didnt work"
				new_kids.append(child)
				if len(next_generation_population) + len(new_kids) == len(initial_population):
					# print "crossing over"
					break
				try:
					child_energy = model.combined_function_values(child)
				except:
					print child
				if child_energy < min_energy:
					min_energy = child_energy

		for new_kid in new_kids:
			next_generation_population.append(new_kid)
		# next_generation_population = next_generation_population + new_kids
		if generation > 10:
			era += model.type2_comparison(initial_population, next_generation_population)

		if era == 0:
			print "Early Termination on Generation: ", generation + 1
			return min_energy, initial_population
			
		
		initial_population = next_generation_population
		# plot(initial_population)

	return min_energy, initial_population



era_list=[]
for model in [DTLZ1, DTLZ3, DTLZ5, DTLZ7]:
	for dec in [10, 20, 40]:
		for obj in [2, 4, 6, 8]:
			m = model(dec, obj)
			best_energy, last_population = ga(model, dec, obj)
			objective_list = m.get_objectives_list(last_population)
			objective_list.insert(0, m.model_name() + "_"+str(dec)+ "_"+str(obj))
			print "Best Energy: ", best_energy

			era_list.append(objective_list)




print sk.rdivDemo(era_list)