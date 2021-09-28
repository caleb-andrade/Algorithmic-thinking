# -*- coding: utf-8 -*-
"""
Algorithmic Thinking Part1. Application 2 - Connected components
and graph resilience
"""

import load_graph_2
import ER_undirected_graph as er
import UPA_algorithm as upa
import random
import breadth_first_search as bfs
import matplotlib.pyplot as plt

# Let's start by loading the graphs
e_graph = load_graph_2.example_graph 
load_graph_2.print_info(e_graph, 'Example_graph')

er_graph = er.er_graph(1239, 0.004)
load_graph_2.print_info(er_graph, 'er_graph')

upa_graph = upa.upa_graph(1239, 3)
load_graph_2.print_info(upa_graph, 'upa_graph')


def random_order(graph):
    """
    Takes a graph and returns a list of the nodes in some 
    random order
    """
    temp = graph.keys()  
    random.shuffle(temp)
      
    return temp

# Compute the resilience of the three graphs    
attack_e_graph = random_order(e_graph)
attack_er_graph = random_order(er_graph)
attack_upa_graph = random_order(upa_graph)

X = bfs.compute_resilience(e_graph, attack_e_graph)
Y = bfs.compute_resilience(er_graph, attack_er_graph)
Z = bfs.compute_resilience(upa_graph, attack_upa_graph)

plt.plot(X, '-', color = 'b', label = 'example_graph')
plt.plot(Y, '-', color = 'r', label = 'er_graph, n = 1239 , p = 0.004') 
plt.plot(Z, '-', color = 'lime', label = 'upa_graph, n = 1239, m = 3' )

fig = plt.gcf()
fig.suptitle('Resilience comparison of three networks under attack', fontsize=14)
ax = fig.add_subplot(111)
ax.set_xlabel('Nodes removed', fontsize = 12)
ax.set_ylabel('Size of largest connected component', fontsize = 12)
fig.set_size_inches(8, 8)
fig.savefig('resilience.png', dpi=100)
plt.show()

text_file1 = open("e_graph_resilience.txt", "w")
text_file2 = open("er_graph_resilience.txt", "w")
text_file3 = open("upa_graph_resilience.txt", "w")

for i in range(1239):
    text_file1.write(str(X[i])+'\n')
    text_file2.write(str(Y[i])+'\n')
    text_file3.write(str(Z[i])+'\n')

text_file1.close()
text_file2.close()
text_file3.close()








