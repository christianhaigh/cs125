import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

n =  5000
""" TODO: Have correct format with 4 args """

""" Cost is plugged in from formula below """ 

cost = 1.48267346282e-05
min_span_tree = [0, 1]
not_in_min_span_tree = [x for x in xrange(2, n)]
branches = [(2, 0) for x in xrange(n)]
costs = []

def new_branches(node):  
    """ Create new branches for new node in tree """ 
    for pot_node in not_in_min_span_tree: 
            pot_weight = random.uniform(0.0, 1.0)
            if pot_weight < branches[pot_node][0]:
                branches[pot_node] = (pot_weight, node)

def branch_selector(branches): 
    """ Select lowest weighted branch that doesn't give cycle """  
    min = 2 
    min_pos = 0
    pos = 0
    for branch in branches: 
        weight = branch[0]
        if weight < min: 
            min = weight
            min_pos = pos
        pos += 1
    return min_pos, branches[min_pos]

def branch_filter(new_node): 
    """ Removes branch options that would form a cycle """
    branches[new_node] = (2, 0)


start_time = time.time()

new_branches(0) 
new_branches(1)
count = 2
while (len(min_span_tree) < n):
    new_node, new_branch = branch_selector(branches)
    min_span_tree.append(new_node)
    not_in_min_span_tree.remove(new_node)
    cost+= new_branch[0]
    costs.append(new_branch[0])
    branch_filter(new_node)
    new_branches(new_node)
    if count%1000 == 0:
        print "Performed", count, "Iterations" 
    count+=1

print "Average Cost:", cost/n
print "Maximum Cost:", max(costs)
print("--- %s seconds ---" % (time.time() - start_time))


def lowest_weighting(n): 
    weights = [random.uniform(0.0, 1.0) for x in xrange(0,n)]
    return min(weights)

"""
def lowest_weighting_avg(n, k):
    lowest_weightings = [lowest_weighting(n) for x in xrange(0,k)]
    average = np.sum(lowest_weightings)/k
    return average 
print lowest_weighting_avg(65356, 100) """





