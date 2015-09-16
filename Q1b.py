import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5: 
        print "USAGE: randmst 0 numpoints numtrials dimension"
        sys.exit()

    n = int(sys.argv[2])
    k = int(sys.argv[3])
    dim = int(sys.argv[4])
    debugger = int(sys.argv[1])

    for i in xrange(k):
        cost = 0 
        costs = []

        """ 1a Weights are assigned randomly """
        if dim == 0:   
            """ Redefine cost in terms of n """ 
            cost = 1.48267346282e-05
            min_span_tree = [0, 1]
            not_in_min_span_tree = [x for x in xrange(2, n)]
            branches = [(2, 0) for x in xrange(n)]

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
                
                if debugger == 1: 
                    if count%1000 == 0:
                        print "Performed", count, "Iterations"
                    count+=1

        elif dim == 2:
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

            nodes = [(random.uniform(0.0,1.0), random.uniform(0.0,1.0), x) for x in xrange(n)]
            min_span_tree = [nodes[0]]
            not_in_min_span_tree = nodes[1:]
            branches = [(2, (0,0)) for x in xrange(n)]
            cost = 0
            costs = []
            start_time = time.time()
            new_branches(min_span_tree[0]) 
            count = 2
            while (len(min_span_tree) < n):
                new_idx, branch = branch_selector(branches)
                min_span_tree.append(branch[1])
                not_in_min_span_tree.remove((branch[1][0],branch[1][1],new_idx))
                cost+= branch[0]
                costs.append(branch[0])
                branch_filter(new_idx)
                new_branches(branch[1])

                if debugger == 1: 
                    if count%1000 == 0:
                        print "Performed", count, "Iterations"
                    count+=1

        elif dim == 3:
            nodes = [(random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0), x) for x in xrange(n)]
            min_span_tree = [nodes[0]]
            not_in_min_span_tree = nodes[1:]
            branches = [(2, (0,0,0)) for x in xrange(n)]

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
                    pot_weight = np.sqrt((node[0] - pot_node[0])**2 + (node[1] - pot_node[1])**2 + (node[2] - pot_node[2])**2)
                    i = pot_node[3]
                    """ how do we insert into the array here? """
                    if pot_weight < branches[i][0]:
                        branches[i] = (pot_weight, (pot_node[0], pot_node[1], pot_node[2]))

            def branch_filter(new_node): 
                """ Removes branch options that would form a cycle """
                branches[new_node] = (2, (0,0,0),(0,0,0))

            start_time = time.time()
            new_branches(min_span_tree[0]) 
            count = 2
            while (len(min_span_tree) < n):
                new_idx, branch = branch_selector(branches)
                min_span_tree.append(branch[1])
                not_in_min_span_tree.remove((branch[1][0],branch[1][1],branch[1][2],new_idx) )
                cost+= branch[0]
                costs.append(branch[0])
                branch_filter(new_idx)
                new_branches(branch[1])

                if debugger == 1: 
                    if count%1000 == 0:
                        print "Performed", count, "Iterations"
                    count+=1
        elif dim == 4:
            nodes = [(random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0), x) for x in xrange(n)]
            min_span_tree = [nodes[0]]
            not_in_min_span_tree = nodes[1:]
            """ nodes are now not indexed but are rather x, y coordinates -- can we still do this? """ 
            branches = [(2, (0,0,0,0)) for x in xrange(n)]

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
                    pot_weight = np.sqrt((node[0] - pot_node[0])**2 + (node[1] - pot_node[1])**2 + (node[2] - pot_node[2])**2 + (node[3] - pot_node[3])**2)
                    i = pot_node[4]
                    """ how do we insert into the array here? """
                    if pot_weight < branches[i][0]:
                        branches[i] = (pot_weight, (pot_node[0], pot_node[1], pot_node[2], pot_node[3]))

            def branch_filter(new_node): 
                """ Removes branch options that would form a cycle """
                branches[new_node] = (2, (0,0,0,0),(0,0,0,0))

            start_time = time.time()
            new_branches(min_span_tree[0]) 
            count = 2
            while (len(min_span_tree) < n):
                new_idx, branch = branch_selector(branches)
                min_span_tree.append(branch[1])
                not_in_min_span_tree.remove((branch[1][0],branch[1][1],branch[1][2],branch[1][3],new_idx) )
                cost+= branch[0]
                costs.append(branch[0])
                branch_filter(new_idx)
                new_branches(branch[1])

                if debugger == 1: 
                    if count%1000 == 0:
                        print "Performed", count, "Iterations"
                    count+=1
        else: 
            print "That is not a valid dimension, please choose 0,2,3 or 4."
            sys.exit()

        if debugger == 1: 
            print "Iteration:",i + 1,"of",k,"with", n,"nodes"
            print "Average Cost:", cost/n
            print "Maximum Cost:", max(costs)
            print "Minimum Cost:", min(costs)
            print("--- %s seconds ---" % (time.time() - start_time)) 
        else: 
            print cost/n, n, k, dim
