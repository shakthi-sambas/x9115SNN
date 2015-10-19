##Reading Assignment 5
####Reference
#####Precise Interface Identification to Improve Testing and Analysis of Web Applications
William G.J. Halfond, Saswat Anand, and Alessandro Orso
Georgia Institute of Technology
Atlanta, GA, USA
{whalfond|saswat|orso}@cc.gatech.edu

#####Keywords
######ii1 Web application
A web application is a software system that is accessed over the web via the HyperText Transport Protocol (HTTP).
######ii2 Interface Invocation
To generate content for the end user, the components of a web application communicate by sending a certain type of 
HTTP request, called an interface invocation, to the interfaces of other components.An interface invocation provides 
arguments in the form of name-value pairs (e.g., login=username).
######ii3 Accepted Interface
The set of input parameters (IP) accessed by a web application during a particular execution is called an accepted 
interface of the web application.
######ii4 Domain Constraining
Certain types of operations called domain-constraining operations, implicitly constrain the domain of an IP. Exam-
ples of these operations are functions that convert an IP value into a numeric value or comparisons of the IP value
against a specific value.

####Brief Notes
#####iii1 Motivational Statements
As web applications become more widespread, sophisticated,and complex, automated quality assurance techniques for
such applications have grown in importance. Accurate interface identification is fundamental for many of these tech-
niques, as the components of a web application communicate extensively via implicitly-dened interfaces to generate cus-
tomized and dynamic content. However, current techniques for identifying web application interfaces can be incomplete
or imprecise, which hinders the effectiveness of quality assurance techniques. To address these limitations, we present a
new approach for identifying web application interfaces that is based on a specialized form of symbolic execution.

#####iii2 Related Work
There are many approaches for interface identification.Several of these rely on developer-provided interface 
specifications: work by Ricca and Tonella uses developer-provided UML models [1], Jian and Liu use a formal 
specification [2],and Andrews, Offutt, and Alexander [3] use finite state machines. As compared to this approach, 
the drawback of these approaches is that they are not automated and are susceptible to developer errors. Another group 
of approaches uses dynamic analysis and web crawling to identify an application's interfaces. An approach by Elbaum and 
colleagues [4]uses a series of requests to an application to identify its interfaces and infer constraints on the IPs 
of the interfaces by analyzing responses to the request.

#####iii3 Delivery Tools
To evaluate their approach, the authors developed a prototype tool called wam-se (Web Application Modeling with Symbolic
Execution). wam-se is written in Java and implements their technique for web applications written in the Java Enterprise
Edition (JEE) framework. The implementation consists of three modules: transform, se engine, and pc analysis,which 
correspond to the three steps of their approach.

Transform: The input to this moduleis the bytecode of the web application and the specification of program entities to 
be considered symbolic(in this case,symbolic strings).

SE Engine:The input to this module is the bytecode of the transformed web application, and the output is the set of all 
Path Conditions (PC) and corresponding symbolic states for each component in the application.

PC Analysis:The input to this module is the set of PCs and symbolic states for each component in the application, and 
the output is the set of Interface Domain Constraints and accepted interfaces. The module iterates over every PC and 
symbolic state, identifies the accepted interfaces, and associates the constraints on each IP with its corresponding 
accepted interface.

#####iii4 Baseline Results
1) Efficiency

            Total Time (s)
Subject         Wdf     Wse     dfw      Spi.
Bookstore       4,093   1,479   1,138   2,774
Classifields      1,985   766     377     239
Employee Dir.   741     905     253     101
Events          333     586     231     15

Table 1: Analysis time.

2)Precision

            Identified Interfaces
Subject         Wse     Wdf
Bookstore       70      338 (268)
Classifields      41      222 (181)
Employee Dir.   18      88 (70)
Events          25      118 (93)

Table 2: Precision of wam-se and wam-df.

3)Usefulness

             Verification Results
Approach        Ok      Error
spider          3 (0)   23 (9)
wam-df          24 (12) 2 (0)
wam-se          12 (0)  14 (0)

Table 3: Invocation Verification for Bookstore.
####References:
[1] F. Ricca and P. Tonella. Analysis and Testing of Web Applications. In International Conference on Software
Engineering, pages 25-34, May 2001.

[2] X. Jia and H. Liu. Rigorous and Automatic Testing of Web Applications. In 6th IASTED International Conference on 
Software Engineering and Applications,pages 280-285, November 2002.

[3] A. A. Andrews, J. Offutt, and R. T. Alexander. Testing Web Applications by Modeling with FSMs. In Software Systems 
and Modeling, pages 326-345, July 2005.

[4] S. Elbaum, K.-R. Chilakamarri, M. F. II, and G. Rothermel. Web Application Characterization Through Directed 
Requests. In International Workshop on Dynamic Analysis, pages 49-56, May 2006.


 