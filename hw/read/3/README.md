#Reading Assignment 3

###Reference

####Search-Based Testing of Ajax Web Applications.

Alessandro Marchetto and Paolo Tonella  
Fondazione Bruno Kessler-IRST  
38050 Povo, Trento, Italy  
marchetto|tonella @fbk.eu  

###Key Words

######ii1 Semantically Interacting Events:
Events e<sub>1</sub> and e<sub>2</sub> interact semantically if there exists a state S<sub>0</sub> such that their execution in S<sub>0</sub>
 does not commute, i.e., the following conditions hold:  
          &nbsp;&nbsp;&nbsp;&nbsp;  S<sub>0</sub> =><sub>e<sub>1</sub>; e<sub>2</sub></sub> S<sub>1</sub>  
          &nbsp;&nbsp;&nbsp;&nbsp;  S<sub>0</sub> =><sub>e<sub>2</sub>; e<sub>1</sub></sub> S<sub>2</sub>  
          &nbsp;&nbsp;&nbsp;&nbsp;  S<sub>1</sub> ≠ S<sub>2</sub>
            
######ii2 AJAX:  
Ajax (Asynchronous Javascript And XML) is a bundle of technologies used to simplify the implementation of rich and dynamic 
Web Applications. It employs HTML and CSS for information presentation. The DOM is used to access and modify the displaye dinformation. 
The XMLHttpRequest object is exploited to retrieve data from the Web Server asynchronously. XML is used to wrap data and Javascript
code, is executed upon callback activation. With AJAX, developers can implement asynchronous communications between client and server.

######ii3 Hill Climbing Testing:  
The paper proposes a search-based test case derivation technique for Ajax called HILL. It is based on the hill climbing algorithm.
It uses an a fitness function to evolve an initial population of test cases with the aim of producing eventually a test suite which maximizes the fitness.

######ii4 Fitness Function:  
There are three fitnesses based on the notion of test diversity defined in the paper: 
  *  EDiv: Test suite diversity based on the execution frequency of each event that labels a transition in the FSM exercised by the test cases of the suite
  *  PDiv: Test suite diversity based on the execution frequency of each pair of semantically interacting events labeling FSM contiguous transitions exercised by each test case of the suite.
  *  TCov: Test suite diversity based on the FSM coverage reached by the test cases in the suite.

### Brief Notes
######iii1 Motivational Statements:
Ajax improves the functionalities and interaction offered to the users. But it also poses novel problems. 
  * Asynchronous requests and responses may interleave in an unexpected way, so Ajax programmers need to carefully program the concurrency provided by Ajax.
  * Dynamic page update is another potential source of faults that are specific of Ajax applications. 
  * The code maybe written according to wrong assumptions about the DOM state.
Paper discusses technique based on dynamic extraction of a finite state machine for an Ajax application and its
analysis with the aim of identifying sets of test cases based on emantically interacting events.
This paper also investigates the use of a search-based approach to address the problem of generating long semantically interacting
event sequences while keeping the test suite size reasonably small.

######iii2 Tools:
There are three tools that were developed to support the proposed testing technique: 
  *  FSMInstrumentor: A Javascript module able to trace the execution of the Web application under test,
  *  FSMExtractor: A Java module to analyze the execution traces and build the application FSM, 
  *  FSMTest CaseGenerator: A Java module to analyze the built FSM and generate test suites according to SEM, ALT, and HILL

######iii3 Related Work:
Several techniques and a few tools have been presented in the literature to support testing of Web applications.
  *  Functional testing tools of Web applications record the interactions that a user has with the graphical interface and repeat them during regression testing.
  *  Model-based testing of Web applications:Two ways namely, Coverage criteria are defined with reference to the navigational model
     and navigational model is a finite state machine with constraints recovered by hand by the test engineers directly from the Web application.

######iii4 Future Work:
The future work described in the paper will be devoted to the improvement of the FSM recovery step, in order to automatically infer
proper abstraction functions. Also experiment with alternative search based algorithms and we will apply them
to a larger benchmark of Ajax applications. And also investigate the role of input selection and infeasible paths in
the FSM during test case generation.

### Improvements
######iv1 Improvement of Finite State Machine recovery step:
Making improvements to the Finite State Machine recovery step can help automatically infer proper abstraction functions.

######iv2 Testing with different Applications to check scalability:
The experiments in the paper are done on two applications only. So the results cannot be generalized to arbitrary Ajax Web Applications.
So the experiments should be done to get a more general result.

######iv3 Increase scope for input selection:
The scope for input selection should be increased to get better quality test cases that can cover large portions of the application, and 
expose more bugs.

### Relation to Previous Paper:

This is the only paper in the Reference papers that mentions web application testing issues. But this paper lacks search based test data generation to 
automate web application testing as proposed by the initial paper we reviewed.

###Contributors
Sakthi Sambasivam  
Nitin Sharma  
Nakul Shukla
