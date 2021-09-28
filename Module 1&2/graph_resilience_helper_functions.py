# -*- coding: utf-8 -*-
"""
Algorithmic Thinking Part1. Application 2 - Connected components
and graph resilience
"""

# Following, some helper functions provided by Algorithmic Thinking
def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    counter = 0
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            counter += 1
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
                
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            counter += 1
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order # uncomment to use graph_resilience_targeted_order
#    return counter # uncomment to use targeted_order_plot


