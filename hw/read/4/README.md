# Reading Assignment 4

### Title 
Dynamic Test Input Generation for Web Applications,

Gary Wassermann, Zhendong Su

University of California, Davis

Dachuan Yu, Ajay Chander, Dinakar Dhurjati, Hiroshi Inamura

DoCoMo USA Labs

## I KeyWords

#### I1. Directed Random Testing
Basically Directed Random Testing is a black box software testing in which programs are executed by generating random inputs.Results of the outputs are compared against given software requirements to verify thatt the test output is pass or fail. 

#### I2. Concloic Testing
Concloic Testing is a hybrid software verification Technique in which it combines symbolic and concrete execution and more specifically using such a combination to generate test inputs to explore all possible execution paths.

#### I3. Automatic Test Genration

Automatic Test Generation is a method  which uses technology from formal methods to mechanize or automate the construction of test cases. This is a model based  development where an executable specification of the program is translated to language of model checker and it is the one generate tests automatically.

#### I4. Test Oracles
Test oracles are the ones which identify the common classes of errors when it occurred.  It basically gives the feed back of each execution of the program like whether the execution is simply passed or failed using assertion mechanism.
. 

## II Brief Notes

#### II1. Motivational Statements

Automated Test Generation frameworks has proven useful for finding bugs and improving test coverage on Languages like C and Java which is dominated by numerical values and pointer based data structures. However,  scripting languages  such as PHP promote a style of programming for developing Web applications that emphasizes String values , Objects and arrays. So the authors propose an approach for analyzing web applications by generating testing inputs for them automatically using informations from previous executions. This approach handles dynamic language features more gracefully than static analysis. They generated automated input test generation algorithm that uses runtime values to analyze code, models the semantics of  string operations In this approach they also explored some implementation trade-offs like experiment a constraint generation implementation that works as part of the runtime system, so that more can be done with- out tampering with the program.

#### II2. Data

The selected three real world PHP Web applications with Known SQL injection vulnerabilities.  The first one is Mantis 1.0.0rc2, is an open source bug tracking system, similar to Bugzilla. The top-level PHP file for this page includes transitively 27 other files for a total of 17,328 lines of PHP in the page. Second one is Mambo 4.5.3, is an open source content management system. This one includes 23 other files for a total of 13,248 lines. The last one is Utopia News Pro 1.3.0, is a news management system. This one contains 6 files for a total of 1529 lines.



#### II3. Statistical Tests




#### II4. Related Work



## III Areas of Improvement

#### III1.
The author chooses six different web applications, but apart from their size, he didn't mention how these applications qualified for experimental studies. It would have been useful if the criterias for selecting application were specified.

#### III2. 
The tests were conducted on a simple hardware setup and also tested locally. So it is difficult to generalize the testing results. It would have been more value added if they had tested this using medium size cluster and also setup remote services in a distributed envrionment.

#### III3.

All the applications chosen for the study are PHP applications. To cover major wides area of web applications they could have selected other applications implemented by other languages like Java to see the overall effectivness and efficiency of this approach.


## References


### Group Members

##### Sakthi Sambasivam
##### Nakul Shukla
##### Nitin Sharma

