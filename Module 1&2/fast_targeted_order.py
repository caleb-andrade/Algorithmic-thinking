# -*- coding: utf-8 -*-
"""
Algorithm 1: FastTargetedOrder
"""
import graph_resilience_helper_functions as grhf

def fast_targeted_order(attack_graph):
    """ 
    takes a undirected graph and returns a list of
    nodes to attack the graph in decreasing order of
    highest degree
    """
    graph = grhf.copy_graph(attack_graph)
    degree_sets = {} # dict with sets of nodes for each degree
    num_nodes = len(graph) # nodes set size
    for idx in range(num_nodes): # initialize empty sets
        degree_sets[idx] = set()
    for node in graph.keys(): # place nodes in their degree sets
        node_deg = len(graph[node])
        degree_sets[node_deg].add(node)
    attack_list = []
    counter = 0
    for idx in range (num_nodes-1, -1, -1):
        while len(degree_sets[idx]) != 0: # if the degree set is non-empty...
            node = degree_sets[idx].pop() # ...select any node
            for neighbor in graph[node]: # for each node's neighbor...
                deg = len(graph[neighbor])                
                degree_sets[deg].remove(neighbor) # ...decrease its degree
                degree_sets[deg-1].add(neighbor) # place it in the degree set
                counter += 1            
            attack_list.append(node) # put node in the attack list
            grhf.delete_node(graph, node) # erase node from graph
            counter += 1
    return attack_list # uncomment to use graph_resilience_targeted_order
 #   return counter # uncomment to use targeted_order_plot
    
   

                
            
        
        
        
        
