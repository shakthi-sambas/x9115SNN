##Reading Assignment 9
#####Reference
Genetic Programming for Reverse Engineering
Mark Harman, William B. Langdon and Westley Weimery
University College London, CREST centre, UK
yUniversity of Virginia, Virginia, USA

#####Keywords
######ii1 Search Based Software Engineering
The use of computational search as a means of optimising software engineering problems
######ii2 Reverse Engineering
Reverse engineering, also called back engineering, is the processes of extracting knowledge or design information 
from anything man-made and re-producing it or reproducing anything based on the extracted information
######ii3 Genetic Programming
Genetic programming (GP) is an evolutionary algorithm-based methodology inspired by biological evolution to find 
computer programs that perform a user-defined task. Essentially GP is a set of instructions and a fitness function
to measure how well a computer has performed a task.
######ii4 Genetic Improvement Programming
GIP evolves replacement software components that maximise achievement of multiple objectives, while retaining the 
interfaces between the components so-evolved and the surrounding system

#####Brief Notes
######iii1 Motivational Statement
SBSE has been applied to almost every aspect of software engineering activity. A more detailed survey of the entire 
field of SBSE can be found on the Internet.This paper focuses on reverse engineering and the considerable
potential for the development of new forms of Genetic Programming (GP) and Genetic Improvement (GI) to reverse
engineering. It presents a summary of the application of SBSE to reverse engineering.It briefly reviews
the relationship between the SBSE and RE publication venues and trends.
######iii2 Hypothesis
A large number of problems in reverse engineering are amenable to SBSE. This paper overviews the application of Search
Based Software Engineering (SBSE) to reverse engineering with a particular emphasis on the growing importance of recent
developments in genetic programming and genetic improvement for reverse engineering. This includes work on SBSE for 
remodularisation, refactoring, regression testing, syntax-preserving, slicing and dependence analysis, concept 
assignment and feature location, bug fixing, and code migration.
######iii3 Commentary
At a high level, key steps likely to occur in a software transplant algorithm to add feature F from source System D 
(the donor) to destination System H (the host):
1) Localise: Identify and localise the code DF  D that implements F (this might use, for example, concept and
feature location

2) Abstract: Construct an abstraction AF from DF , retaining control and data flow directly related to F in the
donor but abstracting references to D-specific identifiers so that these become parameterised.

3) Target: Find locations HF in the host, H, where code implementing F could be located.

4) Interface: Construct an interface, I and add it to the host, H, allowing the resulting combination H [ I to act as 
a ‘harness’ into which candidate transplants can be inserted and evaluated.

5) Insert: Instantiate and concretise a candidate transplant A0 F (concretised from AF ) at HF .

6) Validate: Validate the resulting transplanted system H[I [ A0 F .

7) Repeat: Repeat the above steps until a suitably well tolerated transplant is found.

######iii4 Tests
In a search based setting, many candidate transplants may be considered before an acceptable one is found. 
We highlight a number of dimensions along which the quality of a transplantmight be evaluated during the validation stage.

1) Passes new feature tests: The transplant implements the new desired behaviour correctly. Ideally, all tests of
the host (System H) for the new feature F should pass after the transplant.

2) Passes regression tests: The transplant does not disrupt existing behaviour by introducing side effects. There are
two cases of side effects:
a) The truth, the whole truth: The transplant retains required existing behaviour of H. Ideally, all tests
(and invariants, contracts, etc.) associated with System H (the host) that do not directly conflict with feature F
from the donor (System D) should pass after transplantation. Standard regression testing might be used to determine
if the transplant sacrifices existing behaviour.
b) ... and nothing but the truth: The transplant does not introduce new undesired behaviour. This might be measured 
in terms of anomaly detection or fuzz testing . Automated test data generation, could be used to augment the host’s 
existing test suite for higher coverage of the changed area HF.

3) Passes quality tests: The transplant is readable, maintainable and/or acceptable. If the post-transplant system
is to be maintained by humans, metrics or user studies of readability , maintainability  or acceptability should be used.

####Improvements
#####iv1) Few Practical examples
The paper mentions very few practical examples of where their tecniques were used and their results.

#####iv2) Lack of direction for Future Work
The paper does not mention open avenues of future work or how this work may be used to advance the study of 
Reverse Engineering

#####iv3) Representation of results
The results have not been collected and tabulated suitably so that they can be analysed and conclusions be drawn

####Contributors

##### Sakthi Sambasivam
##### Nitin Sharma
##### Nakul Shukla
