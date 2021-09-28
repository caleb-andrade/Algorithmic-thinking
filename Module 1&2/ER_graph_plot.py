# -*- coding: utf-8 -*-
"""
ER graph
"""
import random

# import module with the functions to calculate degree distribution
import degrees_distribution as degdis
# import module to draw plot
import matplotlib.pyplot as plt

def er_graph(n, p):
    """ creates a digraph randomly choosing edge (i,j) with
    probability p """
    graph = {}
    for i in range(n):
        graph[i] = set([])
        for j in range(n):
            if random.random() <= p and i!=j:
                graph[i].add(j)
    return graph

def binomial_coef(n, k):
    """ computes the binomial coefficient n choose k """
    coef = 1    
    if k <= n/2:
        for i in range (k):
            coef *= float(n-i)/(i+1)
    else:
        for i in range (n-k):
            coef *= float(n-i)/(i+1)
    return coef
    
    
def binomial_dist(n, p):
    """ computes the values of  the binomial distribution """
    y_values = {}
    for k in range(n):
        value = 1 
        if k <= n/2:
            for i in range (k):
                value *= (1-p)*p*float(n-i)/(i+1)
            value *= (1-p)**(n-2*k)
        else:
            for i in range (n-k):
                value *= (1-p)*p*float(n-i)/(i+1)
            value *= p**(2*k-n)
        y_values[k] = value
    return y_values
 
n = 20000
p = 0.01
   
binomial_values = binomial_dist(n, p)
W = binomial_values.keys()
Z = binomial_values.values()

graph = er_graph(n, p)
# calculate the unnormalized distribution of graph
in_deg_dist = degdis.in_degree_distribution(graph)
# normalize the distribution
norm_in_deg_dist = degdis.normalize(in_deg_dist, n)
X = norm_in_deg_dist.keys()
Y = norm_in_deg_dist.values()

plt.plot(W, Z, '.', color = 'b')
plt.plot(X, Y, '.', color = 'r') 

plt.yscale('log')
plt.xscale('log')

plt.ylim([0.00001, 1])
plt.xlim([0, 1000])

fig = plt.gcf()
fig.suptitle('In-degrees normalized distribution (log/log)', fontsize=14)
ax = fig.add_subplot(111)
ax.set_xlabel('in-degrees (log)', fontsize = 12)
ax.set_ylabel('relative frequency of in-degrees (log)', fontsize = 12)
fig.set_size_inches(8, 8)
fig.savefig('ER_plot.png', dpi=100)
plt.show()
            
            

