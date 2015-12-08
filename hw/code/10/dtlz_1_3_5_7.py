from __future__ import division
import matplotlib.pyplot as plt
import time
import numpy
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

	def get_objective_values(self, solution):
		assert False, 'Implement get_objective_values in subclass'


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
