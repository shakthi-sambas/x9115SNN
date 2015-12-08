## Comparison Operators to find Domination 
  
### I. Abstract
  
Various optimization techniques like Simulated Annealing, MaxWalkSat and Differntial Evolution need comparison operators to establish dominance of one solution over the other. The techniques mentioned above follow different approaches to solve the problem but the way they compare intermediate solutions is similar. Broadly there are three main types of comparison operations used, (i)Type1: comparisons between candidates (here candidates are individual solutions), (ii)Type2: comparisons between set of candidates for one optimizer and (iii)Type3: comparisons between set of candidates for different optimizers. Type1 and Type2 comparison operators are used in each of the optimizers separately whereas Type3 operator is used to measure performance of different optimizers with respect to one another. In this assignment, we worked on implementing these three operators that can be used with any optimizer in an efficient way.
  
###II. Introduction
  
Broadly speaking, there are three main types of comparison operators, namely - Type1, Type2 and Type3. Details about these individual operators is given in the paragraphs that follow.

Type 1 operator is at the heart of our algorithm that establishes domination of an individual solution over other. It runs for each solution generated for every generation. It is in the innermost loop and hence the execution time should be fast to enable sustainable runtimes for the algorithm as a whole. To establish dominance, the operator can use either Boolean Domination or Continuous Domination.  Boolean Domination works on the principle of “Better than atleast one” and “worse than none”. Any solution that follows the two principles has a clear view of the heaven and falls on the current pareto frontier. Unlike Binary Domination that compares on collective energies of all objective functions, Continuous Domination takes into account each objective function value for the candidate solution to determine the domination of candidate solution over other. While Binary domination is easier to implement, it works well only for functions with lower number of objective functions. Also it only returns a Boolean value for dominance. Continuous Domination on the other hand overcomes these limitations as it considers all individual objective functions in calculation of dominance. It can also provide a measure for how much one solution is dominated by the other. 

Type2 operator is used to compare two sets of eras (list of candidate solutions). This operator can be used to get a measure of how different one era is from the other and conclude if the changes in the eras are significant enough to keep running the algorithm or terminate the algorithm early. The operator takes the current era and the previous era to calculate the difference between the two. The difference between the eras is calculated using Krall’s B Stop method to know how to increment/ decrement eras. We have a threshold value of era and the operator returns an increment or decrement value depending on whether the eras we different by a certain percent. Early termination for the algorithm happens when the era count reaches zero. To calculate the difference between the eras we use A12, from Vargha and Delaney’s A12 statistic. The statistic also provides literature that supports a difference of 56% is needed for eras to be significantly different.

Type 3 operator compares sets of candidate solutions from different optimizers. The operator is run once at the end of running all optimizers to get optimizers in a ranked order. A new baseline population is used for running each optimizer and each optimizer is run multiple times to get a more confident measure. If we run the optimizer enough number of times, we can see if certain optimizers perform better than the others on a continuous basis. For this assignment, we use Scott-Knott Statistic Chart to display ranking of the optimizers.

###III. Optimizers
  
####Simulated Annealing:
  
Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a meta heuristic for approximate global optimization in a large search space. It is often used when the search space is discrete. For problems where finding the precise global optimum is less important than finding an acceptable global optimum in a fixed amount of time, simulated annealing may be preferable to alternatives such as brute-force search or gradient descent [1]. Simulated annealing starts with a seed solution from the problem space. From this seed solution, we jump randomly around the problem space looking for a solution better than seed solution on every iteration. To avoid getting stuck in local maxima or minima, the algorithm jumps to suboptimal solutions with a small probability. This probability of considering sub optimal solutions goes down as the algorithm goes through its iterations.
  
####MaxWalkSat:
  
MaxWalkSat  non parametric stochastic search algorithm that samples the landscape and tries to improve the solution in one dimension at a time rather than randomly jumping around the problem space like Simulated Annealing. MaxWalkSat jumps around the problem space to find a solution and then explores the landscape around it. Then after some tries, it takes goes to the best solution that was found from the initial solution. Simulated annealing lacks the landscape exploration bit as compared to MaxWalkSat.
  
####Differential Evolution:
Differential Evolution is a Stochastic Direct Search and Global Optimization algorithm, and is a type of an Evolutionary Algorithm from the field of Evolutionary Computation. Differential Evolution algorithm involves maintaining a population of candidate solutions subjected to iterations of recombination, evaluation, and selection. The recombination part involves combining existing candidate solutions according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.  
  
###IV. Description

In this assignment, we use the code developed in previous assignments for optimizers. We add a model for DTLZ7 to the codebase. We also use the Continuous Dominating Type1 operator, as described above, to compare dominance of individual solutions. The choice of continuous domination over boolean domination comes for the fact that the later works well for lower number of objective functions. DTLZ7 function can take multiple objective functions and decision values. We wanted our code to work well with any combination of these values. If it was for the use of just this assignment, we could have used Binary Domination as here we use a variant of DTLZ7 with 10 decisions and 2 objectives. The same Type1 operator is used across all optimizers to save coding effort.
The algorithm begins with a loop running with a termination condition. A new candidate is generated and added to the era. We compare this new candidate to the best and previous solutions that we have using Type1 operator to decide what is to done. This step is different for different optimizers. Next when a new era of 100 is created, we use the Type2 operator to check if the new era is at least 56% different as given by the A12 statistic. If not, the algorithm terminates early. These steps are repeated for all individual optimizers 20 times each. The optimizers return the last era of population. This is stored for all runs of all optimizers and at the end sent to the scott knott chart generating function as argument. The function generates a ranked graph which is included in the results section.
  
###V. Threats to Validity

All the optimizer used in this assignment use heuristics to find an optimal solution. This is done through exploration and exploitation of the landscape. Exploration refers to jumping to new areas to find new solutions and exploitation refers to exploring areas around an available solution in hope to find better solutions. These two ideas help escape the local maxima and minima on the landscape but need to be used wisely to make the algorithm perform better. So depending on how and to what extent these approaches are used, the outcome can be different. Also, as mentioned the optimizer used in this assignment use heuristics, so do not guarantee an optimal solution but the tradeoff between ease of use and reduced complexity and high probability of getting a solution very close to the optimal one makes them very useful in real world scenarios.
  
###VI. Results

The results as given by the Scott Knott charting function are included below in the screenshot. As is clear from the analysis, Differential Evolution performs better than MaxWalkSat and Simulated Annealing consistently. MaxWalkSat and Simulated Annealing perform very similar to each other with Simulated Annealing being a little better. The entire output of the algorithms is included in the file named “[result](result)”. 

<img src="/imgs/code8_1.png">
<img src="/imgs/code8_2.png">

###VIII. References
  
[1] https://en.wikipedia.org/wiki/Simulated_annealing

[2] http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html

[3] http://en.wikipedia.org/wiki/Differential_evolution
