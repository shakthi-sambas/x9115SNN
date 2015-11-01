# Reading Assignment 8

### Title 
SBSE for software product line engineering: a survey and directions for future work,
 
M. Harman, Y. Jia, J. Krinke, W. B. Langdon, J. Petke & Y. Zhang

CREST Centre, University College London, Malet Place, London, WC1E 6BT, U.K.

## I KeyWords

#### I1. SBSE (Software based Search Engineering)
Software based search engineering means using computation search as a tool or technique to optimize software engineering problems. SBSE has been used to address challenging software engineering problems with large and complex search spaces, characterized by many conflicting competing objectives, in many software related areas.

#### I2. SPL (Software Product Lines)
Software product line is a collection of related software products all of which share some core functionality, yet each of which differs  in some specific features. These differences in the features offered by each product help the product line to capture the variability required by different users, different platforms and various operating environments.


#### I3. Genetic Programming
Genetic Programming is an evolutionary algorithm inspired by biological evolution to find computer programs that perform a user defined task.  Essentially genetic programming  is a set of instructions and a fitness function to measure how well a computer has performed a task. 


#### I4. Program Synthesis
Program synthesis is the task of automatically discovering an executable piece of code given user intent expressed using various forms of constraints such as input-output examples, demonstrations, natural language, etc. 

## II Brief Notes

#### II1. Motivational Statements
There is a tremendous upsurge in SBSE for SPL area and the author’s team did a  comprehensive work on topics like recent advances in genetic engineering, search based branch merge and Graft Genetic improvement. Based on their exhaustive study they also highlighted in the direction for future work. They mainly focused on  genetic improvements and showing how these improvements  might be exploited by SPL researchers and practitioners.


#### II2. Sampling Procedures
Real world feature models typically involve many constraints. Tracing . Tracing variability information between problems (requirements) and solutions (products) is challenging. Search based feature model selection is isomorphic to the previously studied search based requirements selection problem. Search based requirements selection seeks to find requirement selections, while respecting constraints. There are many researchers and practitioners formulate procedures and constraints to select a sampling models and features. 


#### II3. Best Practices
The product line architecture captures implementation concerns, with traceability links to the feature model and products. A product line architecture can be used to capture the core salient features, shared by all products on the product line. Colonzi and Guizzo formalized the design patterns in optimization problems primarily focusing on architectural objectives such as extensibility and modularity.

#### II4. Future Work
To incorporate the successes of genetic programming in software engineering, search based software engineers have turned to a technique that has come to be known as ‘genetic improvement’. Genetic Improvement can be used to provide Pareto frontier of programs. This Pareto program surface contains a large number of different programs (‘products’ in SPL nomenclature), each of which share the same functionality, yet all of which differ in their non-functional properties.

When the feature model grows exponentially, that will lead unmanageable  number of different product variants. This situation is called ‘branchomania’. Using SBSE develop techniques to control branchmania by identifying branch similarities, extracting parameters and subsequently searching for suitable tunings that yield individual products. A set of child branches of a shared parent could thereby be merged into a single modified parent with an additional set of parameters that capture the variability previously present in the children.In this way, a combination of parameter extraction and tuned parameter instantiation could merge several products into a single parameterised product.
	
To exploit the current improvements in hardware specifically multicore processors, Search based software engineers have realised the possibility of parallelisation as a route to scalability using computing clusters. Parallel SBSE may prove to be particularly important in scaling computational search algorithms to handle large-scale software product lines.

## III Areas of Improvement

#### III1.
The paper explains some of the topics in details and explains the other topics in an  extremely succinct manner , which leave us many questions unanswered. It could have been better if the author’s team treat all the topics more uniform manner.

#### III2. 
Although the paper give some excellent details about SBSE history, It lack important element like study instrument to suffice more depth in their study.

#### III3.
The author used so many references and it leaves none of them covered fully and leave us more questions than the solutions to some of the topics.

## References

SBSE for software product line engineering: a survey and directions for future work,
M. Harman, Y. Jia, J. Krinke, W. B. Langdon, J. Petke & Y. Zhang
CREST Centre, University College London, Malet Place, London, WC1E 6BT, U.K.

### Group Members

##### Sakthi Sambasivam
##### Nakul Shukla
##### Nitin Sharma

