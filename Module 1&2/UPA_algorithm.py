# -*- coding: utf-8 -*-
"""
UPA algorithm implementation
"""

import random
import degrees_distribution as degdis

def compute_degrees(graph):
    """ returns a list with the degrees of the nodes of a graph"""
    degrees = {}
    for key in graph.keys():
        degrees[key] = len(graph[key])
    return degrees

def upa_graph(n, m):
    """ creates an upa graph with parameters n, m """
    graph = degdis.make_complete_graph(m) # initialize graph
    deg_list = [] # initialize the list of times node i appears as neighbor
    for key in graph.keys():
        deg_list += [key for i in range(m)]

    # UPA algorithm implementation
    for i in range(m, n):
        temp = set()
        for j in range(m):
            temp.add(random.choice(deg_list))
        deg_list += [i for j in range(len(temp) + 1)]
        graph[i] = temp
        for node in temp:
            graph[node].add(i)
        deg_list += list(temp)
    return graph





   
    
    

    
        
    


    
    


    


