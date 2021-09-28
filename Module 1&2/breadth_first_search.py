# -*- coding: utf-8 -*-
"""
Algorithmic Thinking Part1. Project 2 - Connected components
and graph resilience
"""
import collections
#import bfs_test_suite as test

def bfs_visited(ugraph, start_node):
    """ 
    takes an undirected graph and starting node and
    returns the connected component found by BFS 
    """
    queue = collections.deque()
    visited = set([start_node])
    queue.append(start_node)
    while len(queue) > 0:
        parent = queue.pop()
        for neighbor in ugraph[parent]:
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
    
def cc_visited(ugraph):
    """
    takes an undirected graph and returns a list of sets,
    where each set consists of all the nodes in a connected
    component
    """
    answer = []
    for node in ugraph.keys():
        component = bfs_visited(ugraph, node)
        if component not in answer:
            answer.append(component)
    return answer
    
def largest_cc_size(ugraph):
    """
    takes an undirected graph and returns the size (an integer)
    of the largest connected component
    """
    max_size = 0
    components = cc_visited(ugraph)
    for component in components:
        if len(component) > max_size:
            max_size = len(component)
    return max_size
    
def compute_resilience(ugraph, attack_order):
    """
    takes an undirected graph, a list of nodes and iterates
    in the list of nodes. For each node in the list, the function 
    removes the given node and its edges from the graph and then
    computes the size of the largest component in the resulting graph
    """
    components_size = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node)
        for neighbors in ugraph.values():
            neighbors.discard(node)
        components_size.append(largest_cc_size(ugraph))
    return components_size
    
# Run tests (uncomment to test)
#print '\nTesting bfs_visited'    
#test.bfs_visited_run_suite(bfs_visited)
#print '\nTesting cc_visited'
#test.cc_visited_run_suite(cc_visited)
#print '\nTesting largest_cc_size'
#test.largest_cc_size_run_suite(largest_cc_size)
#print '\nTesting compute_resilience'
#test.compute_resilience_run_suite(compute_resilience)
        
    
    
    
                
    
    
    
    
    


