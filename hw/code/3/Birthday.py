__author__ = 'Nakul'

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import random


print ("####################")
print ("Solution for Exercise 10.8")
print ("####################")


# This is the solution to 10.8 part 1
def has_duplicates(inpt):
    lst = inpt[:]
    lst.sort()
    for counter in range (len(lst) -1 ):
        if (lst[counter] == lst [counter +1]):
            return True
    return False

# This part contains solution to part 2 which utilizes function from part 1

def rand_bday_generate(num_of_samples):
    bday = []
    for counter in range (num_of_samples):
        date = random.randint(1,365)
        bday.append(date)
    return bday

def birthday_paradox():
    counter = 0
    num_stud = 23
    runs = 5000
    for k in range (runs):
        bday = rand_bday_generate(num_stud)
        if has_duplicates(bday):
            counter += 1
    return counter

count = birthday_paradox()
print "Number of runs = 5000"
print "Number of students per run = 23"
print "Number of runs with atleast 1 match = %d" % count
print 'Chance (number of runs with matches/5000) = %s percent' % (float(count)*100.0/5000.0)

