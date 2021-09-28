# -*- coding: utf-8 -*-
"""
Code for loading graph
"""

def load_graph(filename):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = open(filename, 'r')
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "\nLoaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

example_graph = load_graph('alg_rf7.txt')

def print_info(graph, name):
    """ prints the number of nodes and edges of a graph """
    print '\n', name, ' is ready!'
    print 'Nodes: ', len(graph)
    edges = 0
    for node in graph.keys():
        edges += len(graph[node])
    print 'Edges: ', edges / 2









