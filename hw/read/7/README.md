#Reading Assignment 7

###Reference  

####The Seed is Strong: Seeding Strategies in Search-Based Software Testing 

######Presented in :  
2012 IEEE Fifth International Conference on Software Testing, Verification and Validation  
######Authored By:  
Gordon Fraser (fraser@cs.uni-saarland.de)   
Andrea Arcuri (arcuri@simula.no)

###Key Words  

######ii1 Seeding:  
In this paper, seeding refers to any technique that exploits previous related knowledge to help solve the 
testing problem at hand. The previous knowledge however is not required and the problem is solvable without using 
such knowledge as well. In the context of search-based software testing (SBST), the most common case of 
seeding regards the case when testing targets are sought one at a time.

######ii2 Control Dependence Graph:   
The control dependence graph in seeding can be used to choose an 
order in which the targets are sought, and so reusing input data from previous runs when there is a need to 
cover a dependent target.

######ii3 Seeding Constants:  
When project branches are dependent on particular values, the program code contains values that are 
similar to the sought values. Paper presents an idea to make use of such information by collecting constant values 
from the source code, and then seeding the search with these values. These constants are called seeding constants. 

######ii4 Search Budget:  
Search budget gives a constraint for the program to finish executing. In the paper, the EVOSUITE tool
developed is stopped after either executing one million statements or a 10 minute timeout. The choice of search budget
can have a large impact on the comparison of algorithms and their variants.

### Brief Notes    
######iii1 Hypotheses:

Search Based Software Testing is not widely adopted partially due to current limitations in these techniques and because many of the different parameters that influence it are not well understood. This paper considers the aspect of the initial population of the search, and presents and studies a series of techniques to improve search-based test data generation for object-oriented software. The ultimate goal is to reduce the number of test cases generated that maximize the branch coverage and at the same time have as low secondary objectives as possible, as these need manual verification.

######iii2 Patterns:  

* Use timeouts to make sure that all experiments finish within a known time bound. In the paper a timeout of 10 minutes is used.
* Repeat experiments multiple times to account for randomness of employed algorithms. For experimentation purposes in the paper, all experiments were repeated 30 times.
* Use number of statements as stopping criterion as it reduces the threats to internal validity regarding the implementation details of the developed research prototypes.

######iii3 Tools:

In the experiments described in the paper, EVOSUITE test generation tool is used. It uses a GA to derive test suites for classes. The EVOSUITE tool operates on bytecode. In all the experiments the default settings of EVOSUITE is used.

######iii4 Future Works:

Study the interactions/relations of the different parameter configurations of EVOSUITE (e.g., population size
and crossover probability) with the seeding strategies and the chosen search budget.

### Improvements  
######iv1 Give importance to length of test suite:
In this paper, the length of test suite generated is given secondary priority. This might lead to generation of larger
test suits with not much increase in achieved coverage.

######iv2 Make evaluation of test cases easier:  
The paper does not take into account how difficult it would be to evaluate the test cases manually to test correctness of output. 

######iv3 Test more parameter settings for EVOSUITE tool:
The paper claims that seeding strategies help EVOSUITE to achieve higher code coverage. But, it is possible that
there exists parameter combinations for seeding strategies and search budget, that can perform better. So more parameter 
settings should be tried.


###Contributors
Sakthi Sambasivam  
Nitin Sharma  
Nakul Shukla
