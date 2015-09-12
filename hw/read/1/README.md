# Reading Assignment 1

## I KeyWords

#### I1. Hill Climbing
Hiil climbing is basically a local search algorithm used in SBSE for testing. A random solution is evualted after that neighbouring solutions of that random solution are evaulated iteratively to find the better solution.

#### I2. Near Miss Seeding (NMS)
During each iteration we collect the input values that are near misses and create near vector. Using this near values instead of random values for inializing search is called Near Miss Seeding.

#### I3. Static Constant Seeding

Instead of using Random values as input we use constant values which are collected  from the source code (by making few modifications the constants)  of the application in the search process. This process is called Static Constant Seeding.

#### I4. Dynamically Mined Value Seeding
The approach of collecting values dynamically from predicated is called Dynamically Mined Value Seeding. It is  very useful because these collected values are not only specific to application, but also specific to predicates, so it can be used in search space when targetting associated branches. 

## II Brief Notes

#### II1. Motivational Statements

The main idea of this paper is to improve automated web application testing by increasing branch coverage with reduction is testing effort. This paper introduces threes algorithms and a tool called "SWAT" and explains the positive impact of these algorithms in efficiency and effectiveness of traditional search based techniques exploiting both static and dynamic analysis.Each improvement is separately evaluated in an empirical study on 6 real world web applications.





## III Areas of Improvement






## References
