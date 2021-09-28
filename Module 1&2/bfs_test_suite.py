# -*- coding: utf-8 -*-
"""
Test Suite for 
Project 2 - Connected components and graph resilience

"""

import simpletest

# some global variables to use

GRAPH1 = {1: set([2]),
          2: set([1]),
          3: set([4]),
          4: set([3, 5]),
          5: set([4]),
          6: set([7, 8]),
          7: set([6, 8]),
          8: set([6, 7]),
          9: set([10]),
          10: set([9]),
          11: set([]),
          12: set([13, 14]),
          13: set([12, 14, 15]),
          14: set([13, 15]),
          15: set([13, 14])}

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}
          
GRAPH3 = {0: set([]),
          1: set([2]),
          2: set([1]),
          3: set([4]),
          4: set([3])}

def  bfs_visited_run_suite(bfs_visited):
    suite = simpletest.TestSuite() # create a TestSuite object
    
    # test bfs_visited on various inputs
    out = {}
    out[1] = set([1, 2])
    out[2] = set([1, 2])
    out[3] = set([3, 4, 5])
    out[4] = set([3, 4, 5])
    out[5] = set([3, 4, 5])
    out[6] = set([6, 7, 8])
    out[7] = set([6, 7, 8])
    out[8] = set([6, 7, 8])
    out[9] = set([9, 10])
    out[10] = set([9, 10])
    out[11] = set([11])
    out[12] = set([12, 13, 14, 15])
    out[13] = set([12, 13, 14, 15])
    out[14] = set([12, 13, 14, 15])
    out[15] = set([12, 13, 14, 15])
    
    for key in out.keys():
        suite.run_test(bfs_visited(GRAPH1, key), out[key], 'Test #'+str(key)+': ')
    
    suite.report_results()

def cc_visited_run_suite(cc_visited):
    suite = simpletest.TestSuite() # create a TestSuite object
    
    # test cc_visited on various inputs
    out = {}
    out[1] = [set([1, 2]), 
              set([3, 4, 5]), 
              set([6, 7, 8]),
              set([9, 10]),
              set([11]),
              set([12, 13, 14, 15])]
    out[2] = [set([1, 2, 3, 4, 5, 6, 7, 8])]
    
    suite.run_test(cc_visited(GRAPH1), out[1], 'Test #1: ')
    suite.run_test(cc_visited(GRAPH2), out[2], 'Test #2: ')
    
    suite.report_results()
    
def largest_cc_size_run_suite(largest_cc_size):
    suite = simpletest.TestSuite()
    
    # test largest_cc_visited on various inputs
    suite.run_test(largest_cc_size(GRAPH1), 4, 'Test #1: ')
    suite.run_test(largest_cc_size(GRAPH2), 8, 'Test #2: ')
    suite.run_test(largest_cc_size(GRAPH3), 2, 'Test #3: ')
    
    suite.report_results()
    
def compute_resilience_run_suite(compute_resilience):
    suite = simpletest.TestSuite()
    
    # test compute_resilience on various inputs
    inp = {}
    inp[0] = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11]
    inp[1] = [12, 13, 14, 15]
    inp[2] = [12, 13, 7, 5]
    inp[3] = [1, 3, 4, 6, 7, 9, 12, 13, 14]
    
    out = {}
    out[0] = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    out[1] = [4, 3, 3, 3, 3]
    out[2] = [4, 3, 3, 3, 2]
    out[3] = [4, 4, 4, 4, 4, 4, 4, 3, 2, 1]

    suite.run_test(compute_resilience(dict(GRAPH1), inp[0]), out[0], 'Test #1: ')
    suite.run_test(compute_resilience(dict(GRAPH1), inp[1]), out[1], 'Test #2: ')
    suite.run_test(compute_resilience(dict(GRAPH1), inp[2]), out[2], 'Test #3: ')
    
    suite.report_results()
    
    
             
    


