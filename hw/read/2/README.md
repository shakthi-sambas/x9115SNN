####Key Words:

######Execution Failures: 

These are web app failures that manifest as crashes or warnings. As an example, execution failures may occur when a web application calls an undefined function or reads a nonexistent file. In such cases, the HTML output contains an error message and execution of the application may be halted, depending on the severity of the failure

######HTML Failures: 

These failures occur when application generates malformed HTML. HTML failures occur when output is generated that is not syntactically well-formed HTML (e.g., when an opening tag is not accompanied by a matching closing tag).

######Static Analysis:

######Dynamic Analysis:


######Motivational 

Web script crashes and malformed dynamically-generated web pages are common errors, and they seriously impact the usability of web applications. The paper presents a dynamic test generation technique for the domain of dynamic web applications. The technique utilizes both combined concrete and symbolic execution and explicit-state model checking. The technique generates tests automatically, runs the tests capturing logical constraints on inputs, and minimizes the conditions on the inputs to failing tests, so that the resulting bug reports are small and useful in finding and fixing the underlying faults.

######Tools:
We created a tool, Apollo, that implements our technique in the context of the publicly available PHP interpreter. Apollo first executes the web application under test with an empty input. During each execution, Apollo monitors the program to record the dependence of control-flow on input. Additionally, for each execution Apollo determines whether execution failures or HTML failures occur (for HTML failures, an HTML validator is used as an oracle). Apollo automatically and iteratively creates new inputs using the recorded dependence to create inputs that exercise different control flow.

######Helpful Visualization:
 <img src="/imgs/Read2_img.png" height= 350 width=600>
 
######Related Work:
An earlier version of this paper was presented at ISSTA’08 [2]. The Apollo tool presented there did not handle the problem of automatically simulating user interactions in web applications. Instead, it relied on a manual transformation of the program under test to enable the exploration of a few selected user inputs. The current paper also extends [2] by providing a more extensive evaluation, which includes two new large web applications, and by presenting a detailed classification of the faults found by Apollo. In addition, the Apollo tool presented in [2] did not yet support web server integration
