# -*- coding: utf-8 -*-
"""
Code for generating plot to answer Question 1 of module 1 
"""
import degrees_distribution as degdis
import load_graph as graph
import matplotlib.pyplot as plt
import numpy as np


# calculate the unnormalized distribution of citation_graph
in_deg_dist = degdis.in_degree_distribution(graph.citation_graph)
# normalize the distribution
norm_in_deg_dist = degdis.normalize(in_deg_dist, 27770)


cg_out_degree_average = degdis.out_degree_average(graph.citation_graph)
print '\nCitation graph out-degree average: ', cg_out_degree_average

X = norm_in_deg_dist.keys()
Y = norm_in_deg_dist.values()

plt.plot(X, Y, '.', color = 'lime') 
plt.yscale('log')
plt.xscale('log')
fig = plt.gcf()
fig.suptitle('In-degrees normalized distribution (log/log)', fontsize=14)
ax = fig.add_subplot(111)
ax.set_xlabel('in-degrees (log)', fontsize = 12)
ax.set_ylabel('relative frequency of in-degrees (log)', fontsize = 12)
fig.set_size_inches(10.7, 8)
fig.savefig('in_degrees_distribution.png', dpi=100)
plt.show()

# linear approximation
m, b = np.polyfit(X, Y, 1)
plt.plot([1, 10000], [b, m*10000 + b], '-', color = 'lime')









