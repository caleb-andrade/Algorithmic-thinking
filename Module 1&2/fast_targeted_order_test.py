# -*- coding: utf-8 -*-
"""
Algorithm 1: FastTargetedOrder
"""

import UPA_algorithm as upa
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
#    print '\ndegree_sets: '
#    for item in degree_sets.keys():
#        print item, ':', degree_sets[item]
    attack_list = []
    counter = 0
    for idx in range (num_nodes-1, -1, -1):
        while len(degree_sets[idx]) != 0: # if the degree set is non-empty...
#            print '\ndegree_sets[', idx, ']: ', degree_sets[idx]
            node = degree_sets[idx].pop() # ...select any node
#            print 'node to delete: ', node
#            print 'neighbors: ', graph[node]
            for neighbor in graph[node]: # for each node's neighbor...
                deg = len(graph[neighbor])                
#                print '\nselect a neighbor: ', neighbor, 'with deg: ', deg
                degree_sets[deg].remove(neighbor) # ...decrease its degree
#                print 'updated degree_sets[', deg, ']: ', degree_sets[deg]
                degree_sets[deg-1].add(neighbor) # place it in the degree set
#                print 'updated degree_sets[', deg-1, ']: ', degree_sets[deg-1]
                counter += 1            
            attack_list.append(node) # put node in the attack list
#            print '\nattack list: ', attack_list
            grhf.delete_node(graph, node) # erase node from graph
            counter += 1
            
    print '\niterations: ', counter
    return attack_list
    
    
    
#graph = upa.upa_graph(20, 4)
graph = {0:set([1, 2, 3, 4]),
         1:set([0, 5, 6, 7]),
         2:set([0, 8, 9]),
         3:set([0, 10]),
         4:set([0]), 
         5:set([1]), 
         6:set([1]), 
         7:set([1]), 
         8:set([2]), 
         9:set([2]), 
         10:set([3])}

print '\ngraph: '
for node in graph.keys():
    print node, ':', graph[node] 
print '\nfast_targeted_order: '
print fast_targeted_order(graph)
print '\ntargeted_order: '
print grhf.targeted_order(graph)



                
            
        
        
        
        
