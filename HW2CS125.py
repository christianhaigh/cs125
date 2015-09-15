
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time
# In[ ]:

n =  65356
""" Have correct format with 4 args """
""" CHANGE TO SOME ARBITRARILY LOW NUMBER """ 
first_cost = 0.0 
cost = first_cost
min_span_tree = [0, 1]
not_in_min_span_tree = [x for x in xrange(2,n)]
costs = []
start_time = time.time()
""" ADD TO ALREADY CREATED LIST """
def new_branches(node):  
    """ Create new branches for new node """ 
    pot_branches = []
    for pot_node in not_in_min_span_tree: 
            pot_weight = random.uniform(0.0, 1.0)
            if pot_weight <= 1/(0.10*n):
                pot_branches.append((pot_weight, pot_node, node))
    return pot_branches

def branch_selector(branches): 
    """ Selects lowest weighted branch """  
    min = 1.1 
    min_pos = 0
    pos = 0
    for branch in branches: 
        weight = branch[0]
        if weight < min: 
            min = weight
            min_pos = pos
        pos += 1
    return branches[min_pos]

def branch_filter(new_node, branches): 
    """ Removes branch options that would form a cycle """
    new_branches = []
    for branch in branches: 
        if new_node != branch[1]: 
            new_branches.append(branch)
    return new_branches

branches = new_branches(0) + new_branches(1)
while (len(min_span_tree) < n):
    new_branch = branch_selector(branches)
    min_span_tree.append(new_branch[1])
    not_in_min_span_tree.remove(new_branch[1])
    cost+= new_branch[0]
    costs.append(new_branch[0])
    branches = branch_filter(new_branch[1], branches)
    branches = branches + new_branches(new_branch[1])

print "Average Cost:", cost/n
print max(costs)
print("--- %s seconds ---" % (time.time() - start_time))

