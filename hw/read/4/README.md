# Reading Assignment 4

### Title 
Dynamic Test Input Generation for Web Applications,

Gary Wassermann, Zhendong Su

University of California, Davis

Dachuan Yu, Ajay Chander, Dinakar Dhurjati, Hiroshi Inamura

DoCoMo USA Labs

## I KeyWords

#### I1. Directed Random Testing
Directed Random Testing is a black box software testing in which programs are executed by generating random inputs. Results of the outputs are compared against given software requirements to verify that the test output is pass or fail. 

#### I2. Concloic Testing
Concloic Testing is a hybrid software verification technique in which it combines symbolic and concrete execution and more specifically uses such a combination to generate test inputs to explore all possible execution paths.

#### I3. Automatic Test Genration

Automatic Test Generation is a method  that uses technology from formal methods to mechanize or automate the construction of test cases. This is a model based  development where an executable specification of the program is translated to language of model checker and it is the one that generate tests automatically.

#### I4. Test Oracles
Test oracles are the ones which identify the common classes of errors when it occurs.  It basically gives the feed back of each execution of the program if an execution simply passed or failed using assertion mechanism.


## II Brief Notes

#### II1. Motivational Statements

Automated Test Generation frameworks have proven useful for finding bugs and improving test coverage on Languages like C and Java which is dominated by numerical values and pointer based data structures. However, scripting languages  such as PHP promote a style of programming for developing web applications that emphasizes string values, objects and arrays. So the authors propose an approach for analyzing web applications by generating testing inputs for them automatically using informations from previous executions. This approach handles dynamic language features more gracefully than static analysis. They generated automated input test generation algorithm that uses runtime values to analyze code, models the semantics of  string operations. In this approach they also explored some implementation trade-offs like they want to experiment a constraint generation implementation that works as part of the runtime system, so that more can be done without tampering the program.

#### II2. Data

They selected three real world PHP Web applications with Known SQL injection vulnerabilities.  The first one is Mantis 1.0.0rc2, is an open source bug tracking system, similar to Bugzilla. The top-level PHP file for this page includes transitively 27 other files for a total of 17,328 lines of PHP in the page. Second one is Mambo 4.5.3, is an open source content management system. This one includes 23 other files for a total of 13,248 lines. The last one is Utopia News Pro 1.3.0, is a news management system. This one contains 6 files for a total of 1529 lines.



#### II3. Base Line Results

In the first phase of their analysis the authors' team perform source to source translation of PHP so that they can write results in a file to trace the execution (like log file). They recorded the results of execution times and corresponding log sizes for one of the Application (Mantis). They also evaluated how long it took in terms of number of test inputs generated and the total time to generate them. In their observation two applications required relatively few test inputs before they generated an attack.


#### II4. Related Work

Test Input Generation: Test input generation that leverages runtime values, or concolic testing, has been pursued by Various groups. The other groups main idea is to gather both symbolic constraints and concrete values from program executions, and use the concrete values to help resolve the constraints to generate the next input. This approach works better for programming languages like C and Java, but certainly not appropriate for scripting languages like PHP.

Web Application Testing: In the Web application testing most of the groups focusses on static pages and the coverage metric (Page Coverage). Some other group explores sequence of links in Web applications by nondeterministically exploring action sequences. Most of the testing mechanisms provide more reliable code coverage, but they repeatedly prompt the user for new inputs, so they sacrifice automation.

There is also work done in Static analysis of web applications similar to authors work in finding the same classes bug using a similar approach.

## III Areas of Improvement

#### III1.
The author just chooses three different real world web applications, but apart from some preliminary details, he didn't mention how these applications qualified for experimental studies. It would have been useful if the criterias for selecting applications were specified.

#### III2. 
The author and his team chosen only PHP Web application for analyzing generating test inputs. It could have been better if they consider other scripting languages like Java Script to generalize their idea.

#### III3.
Their implementation lags few important requirements such as requiring full automation but still requring some manual procedures like loading the pages and invoking analyzers etc.

## References
Dynamic Test Input Generation for Web Applications
Gary Wassermann, Dachuan Yu, Ajay Chander, Dinakar Dhurjati,
Hiroshi Inamura, Zhendong Su

### Group Members

##### Sakthi Sambasivam
##### Nakul Shukla
##### Nitin Sharma

