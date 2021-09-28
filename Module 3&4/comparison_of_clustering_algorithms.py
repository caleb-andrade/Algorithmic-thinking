# -*- coding: utf-8 -*-
"""
@author: Caleb Andrade
Created on Thu Jul 23 18:21 2015
Last Modified: Jul 23 18:42 2015

This is Application 3 - Comparison of clustering algorithms
Algorithmic Thinking Module 3

"""

import random
import closest_pairs_clustering_algorithms as cpc
import alg_cluster as alc
import time
import matplotlib.pyplot as plt

def gen_random_clusters(num_clusters):
    """
    creates a list of randomly generated clusters, where
    each cluster represents a point in the unit square.
    """
    clusters = []
    for idx in range(num_clusters):
        x = random.random()
        y = random.random()
        clusters.append(alc.Cluster(set([]), x, y, 1, 0))
    return clusters
        
# initialize running time lists
Y = []
Z = []

# let's calculate running times
for idx in range(2, 200):
    cluster_list = gen_random_clusters(idx)
    start = time.clock() # start timer
    cpc.slow_closest_pair(cluster_list) # compute slow closest pair
    stop = time.clock() # stop timer
    running_time = stop - start # measure running time
    Y.append(running_time)
    
    start = time.clock() # start timer
    cpc.fast_closest_pair(cluster_list) # compute fast closest pair
    stop = time.clock()
    running_time = stop - start
    Z.append(running_time)

X = [idx for idx in range(2, 200)] # x-axis values

plt.plot(X, Y, '-', color = 'b')
plt.plot(X, Z, '-', color = 'r') 
#plt.plot(X, Y_it, '-', color = 'b')
#plt.plot(X, Z_it, '-', color = 'r')

fig = plt.gcf()
fig.suptitle('Efficiency: slow_closest_pair vs fast_closest_pair (desktop Python)', fontsize=13)
ax = fig.add_subplot(111)
ax.set_xlabel('Number of initial clusters', fontsize = 12)
ax.set_ylabel('Running time (seconds)', fontsize = 12)
fig.set_size_inches(8, 8)
fig.savefig('closest_pair_rt.png', dpi=100)
plt.show()

