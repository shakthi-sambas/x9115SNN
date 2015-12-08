  ## Comparison Operators to find Domination 
  
  ### I. Abstract
  
  Various optimization techniques like Simulated Annealing, MaxWalkSat and Differntial Evolution need comparison operators to establish dominance of one solution over the other. The techniques mentioned above follow different approaches to solve the problem but the way they compare intermediate solutions is similar. Broadly there are three main types of comparison operations used, (i)Type1: comparisons between candidates (here candidates are individual solutions), (ii)Type2: comparisons between set of candidates for one optimizer and (iii)Type3: comparisons between set of candidates for different optimizers. Type1 and Type2 comparison operators are used in each of the optimizers separately whereas Type3 operator is used to measure performance of different optimizers with respect to one another. In this assignment, we worked on implementing these three operators that can be used with any optimizer in an efficient way.
  
  ###II. Introduction
  
  
  
  ###III. Optimizers
  
  ####Simulated Annealing:
  
  Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a meta heuristic for approximate global optimization in a large search space. It is often used when the search space is discrete. For problems where finding the precise global optimum is less important than finding an acceptable global optimum in a fixed amount of time, simulated annealing may be preferable to alternatives such as brute-force search or gradient descent [1]. Simulated annealing starts with a seed solution from the problem space. From this seed solution, we jump randomly around the problem space looking for a solution better than seed solution on every iteration. To avoid getting stuck in local maxima or minima, the algorithm jumps to suboptimal solutions with a small probability. This probability of considering sub optimal solutions goes down as the algorithm goes through its iterations.
  
  ####MaxWalkSat:
  
  MaxWalkSat  non parametric stochastic search algorithm that samples the landscape and tries to improve the solution in one dimension at a time rather than randomly jumping around the problem space like Simulated Annealing. MaxWalkSat jumps around the problem space to find a solution and then explores the landscape around it. Then after some tries, it takes goes to the best solution that was found from the initial solution. Simulated annealing lacks the landscape exploration bit as compared to MaxWalkSat.
  
  ####Differential Evolution:
  
  
  
  ###IV. Description
  
  ###V. Threats to Validity
  
  ###VI. Results
  
  ###VII. References
  
  [1] https://en.wikipedia.org/wiki/Simulated_annealing
