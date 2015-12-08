## Genetic Algorithm to Optimize DTLZ Model

###Abstract

This assignment makes use of genetic algorithm to optimize problem space for DTLZ7.  On a broader scale, this assignment shows how genetic algorithms can be used for optimizing Multi Objective Evolutionary Algorithms (like DTLZ7). The report discusses how we implemented the genetic algorithm and the results we achieved.

###Introduction

A genetic algorithm (GA) is a method for solving both constrained and unconstrained optimization problems based on a natural selection process that mimics biological evolution. The algorithm repeatedly modifies a population of individual solutions. At each step, the genetic algorithm randomly selects individuals from the current population and uses them as parents to produce the children for the next generation. Over successive generations, the population "evolves" toward an optimal solution. Genetic algorithms can be used to solve problems that are not well suited for standard optimization algorithms, like problems in which the objective function is discontinuous, etc [1]. There are two main ways in which genetic algorithms differ from classical algorithms - First, a classic algorithm generates a single candidate at each iteration whereas a genetic algorithm generates a population of candidates at each iteration. The best candidate solution in a population approaches an optimal solution.

To dig deeper into genetic algorithms, we should discuss the different states the algorithm has: 
(1) Initial Population: Specified number of candidate solutions are generated and added to form initial population. 
(2) Fitness Score: Each candidate generated during the course of the algorithm has a fitness score associated with it. Fitness score gives a measure of how good a particular solution is. Fitness score is calculated by a "Fitness Function". A higher fitness score makes it more probable for the candidate to participate in "reproduction" as the algorithm progresses. The candidates with a low fitness score are eventually left out of the population space. 
(3) Selection: Selection refers to finding required number of "Fit" candidates who can participate in reproduction. The analogy comes from biological evolution where the genetic quality of offsprings depends on the genetic makeup of parents. If the genes in parents are strong, the offspring is highly likely to have good genes and in turn better of everything.  Due to the importance of selection strategy in governing the performance of genetic algorithms, a lot of research has been done in the area. Many strategies like Tournament Selection, Ranking Selection, etc have been formulated.     
For the purpose of this assignment, selection refers to selecting the best 20% candidates from a population to ensure we converge to the optimal solution. This comes from the argument that the fittest candidates in a population are closer to the optimal solution. The strategy used is binary tournament selection. The details of how we use this in the algorithm is discussed in later sections.
(4) Crossover: The concept of crossover comes from biological evolution process. It is a process in which chromosomes pair up with each other and exchange different segments of their genetic material to form new chromosomes that are passed along to the offspring. For the assignment purposes, crossover is used to combine parts of two candidates to form a new solution. Details are explained in later section.
(5) Mutation: In biological evolution, mutation refers to a permanent change of DNA sequence. Mutations result from damage to DNA which is not repaired, errors in the process of replication, or from the insertion or deletion of segments of DNA by mobile genetic elements. Mutations may or may not produce discernible changes in the observable characteristics.Mutation can result in several different types of change in sequences. For this assignment, mutation refers to changing some parts of a candidate permanently to get a new solution. Details are explained in later section.

###Algorithm Description

The genetic algorithm we implemented is inspired by [2]. The pseudocode used as reference is given below as a screenshot:

<img src="/imgs/GA_Pseudocode.png">

###Threats to Validity

###Results

###Future Work

###References

[1] http://www.mathworks.com/discovery/genetic-algorithm.html

[2] http://www.cs.ucc.ie/~dgb/courses/tai/notes/handout12.pdf

http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html

https://www.youtube.com/watch?v=zwYV11a__HQ


