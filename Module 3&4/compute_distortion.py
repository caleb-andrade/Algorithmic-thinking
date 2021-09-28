# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:05:07 2015

@author: Caleb Andrade
"""


def compute_distortion(cluster_list, data_table):
    distor = 0
    for cluster in cluster_list:
        distor += cluster.cluster_error(data_table)
    return distor
        