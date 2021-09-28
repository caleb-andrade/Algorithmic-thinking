# -*- coding: utf-8 -*-
"""
ER undirected graph implementation
"""

import random

def er_graph(n, p):
    """ creates a graph randomly choosing edge (i,j) with
    probability p """
    graph = {}
    for i in range(n):
        if not graph.has_key(i):
            graph[i] = set([])
        for j in range(i+1, n):
            if random.random() <= p:
                graph[i].add(j)
                if not graph.has_key(j):
                    graph[j] = set([])
                graph[j].add(i)
    return graph

