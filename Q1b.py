import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

n = 5000
nodes = [(random.uniform(0.0,1.0), random.uniform(0.0,1.0), x) for x in xrange(n)]
min_span_tree = [nodes[0]]
not_in_min_span_tree = nodes[1:]
""" nodes are now not indexed but are rather x, y coordinates -- can we still do this? """ 
branches = [(2, (0,0)) for x in xrange(n)]
cost = 0
costs = []


def branch_selector(branches): 
    """ Select lowest weighted branch that doesn't give cycle """  
    min = 2 
    for i, branch in enumerate(branches): 
        weight = branch[0]
        if weight < min: 
            min = weight
            min_pos = i
    """ returns the index of the min, the weight, and the new node connected"""
    return min_pos, branches[min_pos]

def new_branches(node):  
    """ Create new branches for new node in tree """  
    for pot_node in not_in_min_span_tree: 
		pot_weight = np.sqrt((node[0] - pot_node[0])**2 + (node[1] - pot_node[1])**2)
		i = pot_node[2]
		""" how do we insert into the array here? """
		if pot_weight < branches[i][0]:
		    branches[i] = (pot_weight, (pot_node[0], pot_node[1]))

def branch_filter(new_node): 
    """ Removes branch options that would form a cycle """
    branches[new_node] = (2, (0,0),(0,0))

start_time = time.time()
new_branches(min_span_tree[0]) 
count = 2
while (len(min_span_tree) < n):
    new_idx, branch = branch_selector(branches)
    min_span_tree.append(branch[1])
    not_in_min_span_tree.remove((branch[1][0],branch[1][1],new_idx) )
    cost+= branch[0]
    costs.append(branch[0])
    branch_filter(new_idx)
    new_branches(branch[1])
    if count%1000 == 0:
        print "Performed", count, "Iterations"
    count+=1
print "Average Cost:", cost/n
print "Maximum Cost:", max(costs)
print "Minimum Cost:", min(costs)
print("--- %s seconds ---" % (time.time() - start_time))

