# -*- coding: utf-8 -*-
"""
DPA algorithm implementation
"""

import random
import degrees_distribution as degdis
import matplotlib.pyplot as plt

n = 27770
m = 12

graph = degdis.make_complete_graph(m) # initialize graph
indeg_graph = degdis.compute_in_degrees(graph) # compute in-degrees 
indeg_list = [] # initialize the list of times node i appears as endpoint
for key in indeg_graph.keys():
    indeg_list += [key for i in range(m)]

# DPA algorithm implementation
for i in range(m, n):
    temp = set()
    for j in range(m):
        temp.add(random.choice(indeg_list))
    indeg_list.append(i)
    indeg_list += list(temp)
    graph[i] = temp

print 'DPA-graph is complete!'

# calculate the unnormalized distribution of DPA_graph
in_deg_dist = degdis.in_degree_distribution(graph)
# normalize the distribution
norm_in_deg_dist = degdis.normalize(in_deg_dist, n)

X = norm_in_deg_dist.keys()
Y = norm_in_deg_dist.values()

plt.plot(X, Y, '.', color = 'purple') 
plt.yscale('log')
plt.xscale('log')
fig = plt.gcf()
fig.suptitle('In-degrees normalized distribution (log/log)', fontsize=14)
ax = fig.add_subplot(111)
ax.set_xlabel('in-degrees (log)', fontsize = 12)
ax.set_ylabel('relative frequency of in-degrees (log)', fontsize = 12)
fig.set_size_inches(10.7, 8)
fig.savefig('DPA_in_degrees_dist.png', dpi=100)
plt.show()

   
    
    

    
        
    


    
    


    


