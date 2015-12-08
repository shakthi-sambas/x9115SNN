from __future__ import division
import matplotlib.pyplot as plt
import time
import numpy
import random
import sys
import math
import sk
PI = math.pi
from dtlz_1_3_5_7 import DTLZ1, DTLZ3, DTLZ5, DTLZ7

class DE_Optimizer():

    def __init__(self):
        self.MIN_BOUND = [50, 0.01, 0.6]
        self.MAX_BOUND = [150, 0.1, 1.0, 150]
        self.number_variables = len(self.MIN_BOUND)


    def eval(self, parameters):
        return ga(self.model_to_optimize, parameters)

    def model_name(self):
		return self.__class__.__name__

    def constraint_check(self, _):
        return True

    def generate_random_solution(self):
        # Generate your GA variables here within bounds
        x = list()
        for i, j in zip(self.MIN_BOUND, self.MAX_BOUND):
            if isinstance(i, int) and isinstance(j, int):
                x.append(random.randrange(i, j))
            else:
                x.append(random.uniform(i, j))

        return x

    # def get_baselines(self):
    #     return self.lo, self.hi

def de(dtlz_model, num_candidates=10, max_repeats=100, f=0.75, cf=0.3, epsilon=0.01, maximum=1):
	
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
			return new_sol

	model = DE_Optimizer()
	model.model_to_optimize = dtlz_model
	dtlz_model.get_baseline(1000)

	frontier = [candidate() for _ in range(num_candidates)]
	k = 0
	eb = model.eval(frontier[0])
	bs = frontier[0]

	for n, parent in enumerate(frontier):
		print "................................................................................................................."
		print "Exploring ", n+1 , "/", len(frontier), "on the frontier"
		random_three = select_three_randomly(n)
		first_candidate = frontier[random_three[0]]
		e = model.eval(parent)

		if cf< random.random():
			en = model.eval(first_candidate)
			if en > e:
				e = en
				frontier[n] = first_candidate
		else:
			evolved_candidate = evolve(random_three)
			en = model.eval(evolved_candidate)
			if en > e:
				e = en
				frontier[n] = evolved_candidate
		if e > eb:
			print "Previous best:", eb
			print "Parameter Values [Population Size, Mutation Rate, Crossover Probability]:", [int(parent[0]), parent[1], parent[2]]
			eb = e
			bs = frontier[n]
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "#################################################################################################################"
	print "Best Solution:" + str(bs)
	print "Best Energy:" + str(eb)
	return bs


def ga(model, parameters):
	# make initial population sample
	# make selection.
	max_generations=1000
	population_size = int(parameters [0])
	mutation_probability = parameters [1]
	crossover_probability = parameters [2]

	model.get_baseline(100)
	era_threshold = 100
	print "................................................................................................................."
	print "Running GA for parameters:"
	print "     Population:", population_size, " || Mutation Rate:", mutation_probability, " || Crossover probability:", crossover_probability

	def make_initial_population_sample():
		population_list=[]

		for i in xrange(population_size):
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

	def get_hypervolume(all_generations_list, population_size, tries = 100000):
	    number_of_generations = len(all_generations_list)

	    frontier = all_generations_list[number_of_generations - 1]

	    for _ in range(tries):
	        random_generation_index = random.randint(0, number_of_generations - 2)
	        random_frontier_index = random.randint(0, len(frontier) - 1)
	        random_population_index = random.randint(0, population_size - 1)

	        frontier_element = frontier[random_frontier_index]
	        randomly_selected_element = all_generations_list[random_generation_index][random_population_index]
	        if model.type1(frontier_element, randomly_selected_element):
	            continue
	        elif model.type1(randomly_selected_element, frontier_element):
	            frontier[random_frontier_index] = randomly_selected_element
	            all_generations_list[random_generation_index][random_population_index] = frontier_element
	        else :
	            frontier.append(randomly_selected_element)

	    for element_one in frontier:
	        for element_two in frontier:
	            if element_one == element_two:
	                continue
	            if model.type1(element_one, element_two):
	                frontier.remove(element_two)

	    hv = (number_of_generations * population_size - len(frontier)) / (number_of_generations * population_size)
	    return hv
	
	base_population = initial_population
	best_solution = initial_population[0]
	min_energy = model.combined_function_values(best_solution)
	all_generations_list = [initial_population]
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
			era_threshold += model.type2_comparison(initial_population, next_generation_population)

		if era_threshold == 0:
			print "Early Termination on Generation", generation + 1
			break
			
		
		initial_population = next_generation_population

		all_generations_list.append(initial_population)
		# plot(initial_population)
	print "Calculating HyperVolume..."
	hyper_volume = get_hypervolume(all_generations_list, population_size)
	
	print "Hyper Volume:", hyper_volume

	# if flag:
	# 	return initial_population

	# else:
	return hyper_volume




ga(DTLZ1(10,2), de(DTLZ1(10, 7)))
print "#################################################################################################################"