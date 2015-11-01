from __future__ import division
import random
import math


variable_upper_bound = [10,10,5,6,5,10]
variable_lower_bound = [0,0,1,0,1,0]

def f1(x):
    return (-((25*((x[0]-2)**2)) + ((x[1] - 2)**2) + (((x[2]-1)**2) * ((x[3]-4)**2)) + ((x[4]-1)**2)))

def f2(x):
    return x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2 +x[5]**2

def combined_osyczka_values (x):
    # print x
    combined_value = f1(x) + f2(x)
    # print combined_value
    return combined_value

def f1(x):
    return -((25 * ((x[0] - 2) ** 2)) + ((x[1] - 2) ** 2) + ((x[2] - 1) ** 2) * ((x[3] - 4) ** 2) + ((x[4] - 1) ** 2))


def f2(x):
    return x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2 + x[5] ** 2


def combined_maxwalksat_values(x, normalize=False, min_val=None, max_val=None):
    combined_value = f1(x) + f2(x)
    if normalize:
        return abs((combined_value - min_val) / (max_val - min_val))
    else:
        return combined_value


def check_constraints(x):
    if (x[0] + x[1] - 2) >= 0:
        flag = 1
    else:
        return False

    if (6 - x[0] - x[1]) >= 0:
        flag = 1
    else:
        return False
    if (2 - x[1] + x[0]) >= 0:
        flag = 1
    else:
        return False
    if (2 - x[0] + 3 * x[1]) >= 0:
        flag = 1
    else:
        return False
    if (4 - (x[2] - 3) ** 2 - x[3]) >= 0:
        flag = 1
    else:
        return False
    if ((x[4] - 3) ** 3 + x[5] - 4) >= 0:
        flag = 1
    else:
        return False
    return flag

def generate_random_solution():
    while True:
        random_solution = []
        for low, high in zip(variable_lower_bound, variable_upper_bound):
            random_num = random.randrange(low, high)
            random_solution.append(random_num)
        if check_constraints(random_solution):
            # print random_solution
            return random_solution
            
def base_mws():
    min_base_mws_value = 10000000 ** 2
    max_base_mws_value = -10000000
    
    for i in range(0, 10**5):
        while True:
            current_solution = generate_random_solution()
            if check_constraints(current_solution):
                break
        current_value = combined_osyczka_values(current_solution)
        if current_value < min_base_mws_value:
            min_base_mws_value = current_value
        if current_value > max_base_mws_value:
            max_base_mws_value = current_value
    # print min_base_mws_value, max_base_mws_value
    return min_base_mws_value, max_base_mws_value

def energy(sol, min_base, max_base):
    value = combined_osyczka_values(sol)
    # print value
    en =  ( abs(value - min_base )) / (3*( max_base - min_base )) 
    # print en 
    return en
    
def choose_max( sol, index, steps, min_base_mws_value, max_base_mws_value):
    sub_counter = 0 
    bs = copy = sol
    diff_bw_two_sol = (variable_upper_bound[index] - variable_lower_bound[index]) / steps
    for step in range(0, steps):
        sub_counter = sub_counter + 1
        copy[index] = variable_lower_bound[index] + diff_bw_two_sol*step
        if check_constraints(copy):
            if energy(copy, min_base_mws_value, max_base_mws_value) > energy(bs, min_base_mws_value, max_base_mws_value):
                bs = copy
    return [bs, sub_counter]
        

def mws(trials, max_changes, p = 0.5, threshold = 5.0, step=10):
    counter = sub_counter = 0
    min_base_mws_value, max_base_mws_value = base_mws()
    bl = []
    bs = generate_random_solution()
    be = energy(bs, min_base_mws_value, max_base_mws_value)
    ls, le = bs, be  # Previous state.
    for i in range (0, trials):
        print_string = ''
        cs =  generate_random_solution()
        
        for j in range (0, max_changes):
            trial_outcome = ''
            if energy(cs, min_base_mws_value, max_base_mws_value) > threshold:
                print 'Threshold reached'
                return cs
            random_index = random.randint(0, 5)
            if p < random.random():
                ds = cs  #duplicate solution
                ds[random_index] = random.randrange(variable_lower_bound[random_index], variable_upper_bound[random_index])
                counter +=1
                if check_constraints(ds):
                    cs = ds
                    trial_outcome = '?'
                    # print "not here"
                else:
                    trial_outcome = '.'
                    
                # print trial_outcome
            
            else:
                
                cs, sub_counter = choose_max(cs, random_index, step, min_base_mws_value, max_base_mws_value) 
                # cs = bl[1]
                ce = energy(cs, min_base_mws_value, max_base_mws_value)
                # counter += sub_counter
                counter +=1
                if ce > be: # Found a better solution
                    trial_outcome = '!'
                    bs, be = cs, ce
                elif ce > le: # Found better solution than previous solution
                    trial_outcome = '+'
                else:
                    trial_outcome = '.'
                ls, le = cs, ce
            print_string = print_string + ' ' + trial_outcome
        
        # print str(counter) +'  ' + str(energy(cs, min_base_mws_value, max_base_mws_value)) + ' ' + print_string
        print str(counter) +'  ' + str(be) + ' ' + print_string    
    print "Best Energy: " + str(be)
    print "Best Solution: " + str(bs)            
    
    
    
print mws(100, 30)


