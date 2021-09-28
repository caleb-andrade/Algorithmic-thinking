# -*- coding: utf-8 -*-
"""
Algorithmic Thinking. Module 1. Application 2: Graph Resilience
Question 3
"""
import UPA_algorithm as upa
import graph_resilience_helper_functions as grhf
import fast_targeted_order as fto
import matplotlib.pyplot as plt
import time 

# initialize running time lists
Y = []
Y_it = []
Z = []
Z_it = []

# let's calculate running times
for idx in range(10, 1000, 10):
    graph = upa.upa_graph(idx, 5)
    start = time.clock() # start timer
    Y_it.append(grhf.targeted_order(graph)) # compute targeted_order for graph
    stop = time.clock() # stop timer
    running_time = stop - start # measure running time
    Y.append(running_time)
    
    start = time.clock() # start timer
    Z_it.append(fto.fast_targeted_order(graph)) # compute fast_targeted_order for graph
    stop = time.clock()
    running_time = stop - start
    Z.append(running_time)

X = [idx for idx in range(10, 1000, 10)] # x-axis values

plt.plot(X, Y, '.', color = 'b')
plt.plot(X, Z, '.', color = 'r') 
#plt.plot(X, Y_it, '-', color = 'b')
#plt.plot(X, Z_it, '-', color = 'r')

fig = plt.gcf()
fig.suptitle('Running time: targeted_order vs fast_targeted_order (desktop Python)', fontsize=13)
ax = fig.add_subplot(111)
ax.set_xlabel('UPA graph values for n', fontsize = 12)
ax.set_ylabel('Running time (sec)', fontsize = 12)
fig.set_size_inches(8, 8)
fig.savefig('targeted_order.png', dpi=100)
plt.show()
