# -*- coding: utf-8 -*-
"""
Algorithmic Thinking Module 1. Project #1: degrees distribution
"""

def make_complete_graph(num_nodes):
    """ returns a complete directed graph as a dictionary """
    complete_digraph = {}
    if num_nodes > 0 and type(num_nodes) == int:
        neighbors = set([idx for idx in range(num_nodes)])
        for idx in range(num_nodes):
            complete_digraph[idx] = neighbors.copy() #creates adjacency set
            complete_digraph[idx].remove(idx) # pop out self-loop 
    return complete_digraph

def compute_in_degrees(digraph):
    """ computes in-degrees for the nodes in the graph """
    in_degrees = {}
    temp = []
    for key in digraph.keys():
        temp += list(digraph[key]) # extract values for each key as a list
        in_degrees[key] = 0 # initialize a dictionary with 0's
    for idx in range(len(temp)):
        in_degrees[temp[idx]] += 1
    return in_degrees        

def in_degree_distribution(digraph):
    """ computes unnormalized distribution of the in-degrees of graph """
    in_degrees = compute_in_degrees(digraph)
    in_deg_dist = {}
    for key in in_degrees.keys():
        if in_deg_dist.has_key(in_degrees[key]):
            in_deg_dist[in_degrees[key]] += 1
        else:
            in_deg_dist[in_degrees[key]] = 1
    return in_deg_dist

def normalize(dictionary, num):
    """ normalizes distribution of in-degrees saved as a dictionary """
    for key in dictionary.keys():
        dictionary[key] = float(dictionary[key])/num
    return dictionary
    
def out_degree_average(digraph):
    """ computes the out-degree average of a digraph """
    count = 0
    for key in digraph.keys():
        count += len(digraph[key])
    return float(count)/len(digraph)
    


      
            
         
        
    

