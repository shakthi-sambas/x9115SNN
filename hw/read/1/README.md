# Reading Assignment 1

## I KeyWords

#### I1. Hill Climbing
Hiil climbing is basically a local search algorithm used in SBSE for testing. A random solution is evuluated after that neighbouring solutions of that random solution are evaulated iteratively to find the better solution.

#### I2. Near Miss Seeding (NMS)
During each iteration we collect the input values that are near misses, and create near vector. Using this near values instead of random values for inializing search is called Near Miss Seeding.

#### I3. Static Constant Seeding

Instead of using Random values as input we use constant values which are collected  from the source code (by making few modifications the constants)  of the application in the search process. This process is called Static Constant Seeding.

#### I4. Dynamically Mined Value Seeding
The approach of collecting values dynamically from predicates is called Dynamically Mined Value Seeding. It is  very useful because these collected values are not only specific to application, but also specific to predicates, so it can be used in search space when targetting associated branches. 

## II Brief Notes

#### II1. Motivational Statements

The main idea of this paper is how to improve automated web application testing by increasing branch coverage with reduction in testing effort. This paper introduces threes algorithms and a tool called "SWAT" and explains the positive impact of these algorithms in efficiency and effectiveness of traditional search based techniques exploiting both static and dynamic analysis. Each improvement is separately evaluated in an empirical study on 6 real world web applications.

#### II2. Delivery Tools

Authors Team developed a Tool called Search Based Web Application Tester (SWAT) to cover the various testing approaches. SWAT consitsts of two major tools: 1. Search based Tester and 2.Test Harness.The Search based Tester uses the transformed source code and the analysis data to implement the input generation described in three different Algorithms.The Test Harness uses the generated test data to run the tests on the original source code and to produce coverage and bug data. Both Search based tool and Test Harness are implemented in Perl and use the HTTP, HTML and LWP libraries.


#### II3. Statistical Tests
The author conducted testing using three different versions of SWAT. Each version uses various approches to cover the wide area of branches. Also each branch was allocated the same budget of fitness evaluations for each version of the tool, so that they can evaluate the effectiveness of each version on the unaugmented traditional search based approach. Basically each version targets the following areas: 1.How it affects branch coverage 2. How it improves efficiency 3. How it affects fault finding ability.



#### II4. Related Work
Although there is lots of research made in Search based software engineering, Search based test data generation is used for these studies specifically for web applications. The other teams used this approach for Ajax based web applications using Hill climbing Algorithm. Also the other team  introduced an algorithm that uses symbolic execution of the source code to group inputs into interfaces. This approach is for applied to Java applications where as the authors team's mainl focus is on PHP applications.


## III Areas of Improvement

#### III1.
The author chooses six different web applications, but apart from their size, he didn't mention how these applications qualified for experimental studies. It would have been useful if the criterias for selecting application were specified.

#### III2. 
The tests were conducted on a simple hardware setup and also tested locally. So it is difficult to generalize the testing results. It would have been more value added if they had tested this using medium size cluster and also setup remote services in a distributed envrionment.

#### III3.

All the applications chosen for the study are PHP applications. To cover major wides area of web applications they could have selected other applications implemented by other languges like Java to see the overall effectivness and efficiency of this approach.


## References
[1] Automated Web Application Testing Using Search Based Software Engineering
Nadia Alshahwan and Mark Harman CREST Centre
University College London
London, UK

### Group Members

##### Sakthi Sambasivam
##### Nakul Shukla
##### Nitin Sharma
