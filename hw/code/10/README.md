#Tuning Genetic Algorithm Using Differential Evolution

##Abstract

In Code 8, we implemented Differential Evolution to optimize solution space for DTLZ's. Then in code 9 we implemented a genetic algorithm to optimize DTLZ's. In this assignment, we use Differential Evolution to tune the default parameters for genetic algorithm (poulation size, mutation rate and crossover probability) to get solutions closer to heaven. 

##Introduction

####Genetic Algorithm

A genetic algorithm (GA) is a method for solving both constrained and unconstrained optimization problems based on a natural selection process that mimics biological evolution. The algorithm repeatedly modifies a population of individual solutions. At each step, the genetic algorithm randomly selects individuals from the current population and uses them as parents to produce the children for the next generation. Over successive generations, the population "evolves" toward an optimal solution. Genetic algorithms can be used to solve problems that are not well suited for standard optimization algorithms, like problems in which the objective function is discontinuous, etc [1]. There are two main ways in which genetic algorithms differ from classical algorithms - First, a classic algorithm generates a single candidate at each iteration whereas a genetic algorithm generates a population of candidates at each iteration. The best candidate solution in a population approaches an optimal solution.  

To dig deeper into genetic algorithms, we should discuss the different terminology used during the algorithm:  
(1) Initial Population: Specified number of candidate solutions are generated and added to form initial population.   
(2) Fitness Score: Each candidate generated during the course of the algorithm has a fitness score associated with it. Fitness score gives a measure of how good a particular solution is. Fitness score is calculated by a "Fitness Function". A higher fitness score makes it more probable for the candidate to participate in "reproduction" as the algorithm progresses. The candidates with a low fitness score are eventually left out of the population space.  
(3) Selection: Selection refers to finding required number of "Fit" candidates who can participate in reproduction. The analogy comes from biological evolution where the genetic quality of offspring depends on the genetic makeup of parents. If the genes in parents are strong, the offspring is highly likely to have good genes and in turn better of everything.  Due to the importance of selection strategy in governing the performance of genetic algorithms, a lot of research has been done in the area. Many strategies like Tournament Selection, Ranking Selection, etc have been formulated.   
For the purpose of this assignment, selection refers to selecting the best 20% candidates from a population to ensure we converge to the optimal solution. This comes from the argument that the fittest candidates in a population are closer to the optimal solution. The strategy used is binary tournament selection. The details of how we use this in the algorithm is discussed in later sections.  
(4) Crossover: The concept of crossover comes from biological evolution process. It is a process in which chromosomes pair up with each other and exchange different segments of their genetic material to form new chromosomes that are passed along to the offspring. For the assignment purposes, crossover is used to combine parts of two candidates to form a new solution. Details are explained in later section.  
(5) Mutation: In biological evolution, mutation refers to a permanent change of DNA sequence. Mutations result from damage to DNA which is not repaired, errors in the process of replication, or from the insertion or deletion of segments of DNA by mobile genetic elements. Mutations may or may not produce discernible changes in the observable characteristics.Mutation can result in several different types of change in sequences. For this assignment, mutation refers to changing some parts of a candidate permanently to get a new solution. Details are explained in later section.  
(6) HyperVolume: An algorithm produces a set of points in the performance space as an estimation of the Pareto frontier. A quantitative measure is needed to estimate the closeness of the estimated data points to the true Pareto front. One of such measures is the hypervolume indicator, which gives the hypervolume between the estimated Pareto front and a reference point.

####Differential Evolution:

Differential Evolution is a Stochastic Direct Search and Global Optimization algorithm, and is a type of an Evolutionary Algorithm from the field of Evolutionary Computation. Differential Evolution algorithm involves maintaining a population of candidate solutions subjected to iterations of recombination, evaluation, and selection. The recombination part involves combining existing candidate solutions according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.

##Algorithm Description

####Working of Differential Evolution:

A frontier with size 10 is generated (we keep the size small for practicality. Higher frontier sizes take very long to finish a run). DE is run once on the entire frontier. Then we randomly select three candidates and with a probability cf, the child evolves (using default formula for DE: New = X + f * (Y - Z) where New is the new candidate, and X, Y, Z are the randomly selected candidates,). The only change in the way DE works here is that the Evaluation function of DE calls the genetic algorithm with the mutated parameters. The bound for parameters is set for DE to work with.

####Working of Genetic Algorithm:

When the algorithm starts, an initial population based on the model used is generated. This is the first generation of the algorithm. So the most optimal solution at this point is the best candidate at this generation. This solution is recorded for future comparisons.

We set a maximum number of generations threshold to prevent the algorithm from going on endlessly. Then we select the top 20% fittest candidates. The fittest candidates are selected using Type1 boolean domination comparison as described in Code 8. This gives us candidates that are “Better than atleast one” and “worse than none”. These candidates are closest to the optimal solution in the current generation. Now, if the number of such candidates is less than 20% of the population size, we randomly fill in the rest of the candidates from the population. This is done to ensure that we have candidates in the selection made for further steps in the algorithm.

Once we get a selection of fittest 20% candidates from the population, we select two parents randomly from this selection. The two parents crossover with a crossover probability. During crossover, some parts from both parents are inherited by the child. This newly created child is then subjected to mutation. For mutation, we look at each element for the child and mutate it with a mutation probability. We repeat the above process to generate new children till the population is back to its original size. So now, in the new generation, 20% of the population is from the previous generation. They are the fittest candidates in the previous generation. The other 80% comes from crossing over and mutating the children from the fittest candidates.

The process of selection and generation of new population is done till we reach a maximum generation threshold or the difference in generation energies is not enough for us to repeat the process. This comparison is done through Type2 operator (described in code 8).

The last step is to calculate hypervolume. We do this to measure the closeness of the final generation generated by the algorithm to the true Frontier.  

The result is printed for each iteration of DE frontier and is included in the results section.

##Results

The Differential Evolution Tuner for Genetic Algorithm has 10 candidates on its frontier. The screenshots below show run for DE on each candidate on the frontier. It shows the default parameters used in that run. These parameters are given to the Genetic Algorithm through DE optimization. Next it shows the Generation at which genetic algorithm terminates and at the end it shows the Hypervolume measure for that generation.  
This process is repeated 10 times and then the best values for the parameters is returned back and GA is run with these parameters to give the best hypervolume during this run of the algorithm. This is shown in the last screenshot. The result report can be found in "[result](result)"

<img src="/imgs/code10_1.png">
<img src="/imgs/code10_2.png">
<img src="/imgs/code10_3.png">
<img src="/imgs/code10_4.png">

##Threats to Validity

All the optimizer used in this assignment use heuristics to find an optimal solution. This is done through exploration and exploitation of the landscape. Exploration refers to jumping to new areas to find new solutions and exploitation refers to exploring areas around an available solution in hope to find better solutions. These two ideas help escape the local maxima and minima on the landscape but need to be used wisely to make the algorithm perform better. So depending on how and to what extent these approaches are used, the outcome can be different. Also, as mentioned the optimizer used in this assignment use heuristics, so do not guarantee an optimal solution but the tradeoff between ease of use and reduced complexity and high probability of getting a solution very close to the optimal one makes them very useful in real world scenarios. Use of boolean domination may cause problems when using models with high objectives.

##Future Work

Boolean domination has its own drawbacks. In future works we plan on implementing continuous domination for type1 comparisons. Also, plotting the population in form of graphs can give better insights of how the algorithm is working. So, we plan on representing the solution in graphical manner in future.

##References

[1] http://www.mathworks.com/discovery/genetic-algorithm.html

http://en.wikipedia.org/wiki/Differential_evolution

#####COLLABORATORS

######Sakthi Sambasivam (ssambas)

######Nitin Sharma (nsharm10)

######Nakul Shukla (nshukla)
