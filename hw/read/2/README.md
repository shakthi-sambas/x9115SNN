###Reference

####Finding Bugs in Web Applications Using Dynamic Test Generation and Explicit State Model Checking

Shay Artzi† 
Adam Kiezun Julian Dolby‡
Frank Tip‡ 
Danny Dig∗ 
Amit Paradkar‡ 
Michael D. Ernst⋆

†MIT CSAIL, {artzi,akiezun}@csail.mit.edu   
‡IBM T.J. Watson Research Center, {dolby,ftip,paradkar}@us.ibm.com   
∗University of Illinois at Urbana-Champaign, dig@illinois.edu   
⋆University of Washington,mernst@cs.washington.edu

###Key Words:

######ii1 Execution Failures: 

These are web app failures that manifest as crashes or warnings. As an example, execution failures may occur when a web application calls an undefined function or reads a nonexistent file. In such cases, the HTML output contains an error message and execution of the application may be halted, depending on the severity of the failure

######ii2 HTML Failures: 

These failures occur when application generates malformed HTML. HTML failures occur when output is generated that is not syntactically well-formed HTML (e.g., when an opening tag is not accompanied by a matching closing tag).

######ii3 Static Analysis:

Static analysis, also called static code analysis, is a method of computer program debugging that is done by examining the code without executing the program. The process provides an understanding of the code structure, and can help to ensure that the code adheres to industry standards

######ii4 Dynamic Analysis:

Dynamic analysis is the testing and evaluation of a program by executing data in real-time. The objective is to find errors in a program while it is running, rather than by repeatedly examining the code offline

### Brief Notes
######iii1 Motivation 

Web script crashes and malformed dynamically-generated web pages are common errors, and they seriously impact the usability of web applications. The paper presents a dynamic test generation technique for the domain of dynamic web applications. The technique utilizes both combined concrete and symbolic execution and explicit-state model checking. The technique generates tests automatically, runs the tests capturing logical constraints on inputs, and minimizes the conditions on the inputs to failing tests, so that the resulting bug reports are small and useful in finding and fixing the underlying faults.

######iii2 Tools:
We created a tool, Apollo, that implements our technique in the context of the publicly available PHP interpreter. Apollo first executes the web application under test with an empty input. During each execution, Apollo monitors the program to record the dependence of control-flow on input. Additionally, for each execution Apollo determines whether execution failures or HTML failures occur (for HTML failures, an HTML validator is used as an oracle). Apollo automatically and iteratively creates new inputs using the recorded dependence to create inputs that exercise different control flow.

######iii3 Helpful Visualization:
 <img src="/imgs/Read2_img.png" height= 350 width=600>
 
######iii4 Related Work:
An earlier version of this paper was presented at ISSTA’08 [1]. The Apollo tool presented there did not handle the problem of automatically simulating user interactions in web applications. Instead, it relied on a manual transformation of the program under test to enable the exploration of a few selected user inputs. The current paper also extends [2] by providing a more extensive evaluation, which includes two new large web applications, and by presenting a detailed classification of the faults found by Apollo. In addition, the Apollo tool presented in [1] did not yet support web server integration

###Improvement:

######iv1 Simulating user inputs based locally executed JavaScript

The HTML output of a PHP script might contain buttons and arbitrary snippets of JavaScript code that are executed when the user presses the corresponding button. The actions that the JavaScript might perform were not analyzed by Apollo

######iv2 Limited tracking in native methods 
Apollo had limited tracking of input parameters through PHP native methods.
PHP native methods are implemented in C, which make it difficult to automatically track how input parameters are
transformed into output parameters.

######iv3 Limited sources of input parameters 
Apollo considers as parameters only inputs coming from the global arrays POST, GET and REQUEST.

### Relation to previous Paper
The sample applications used here were also used to test the SWAT mentioned in the previous paper

### Reference

[1] S. Artzi, A. Kiezun, J. Dolby, F. Tip, D. Dig, A. Paradkar, and M. D. Ernst. Finding bugs in dynamic web applications. 
In ISSTA, pages
261–272, 2008.
