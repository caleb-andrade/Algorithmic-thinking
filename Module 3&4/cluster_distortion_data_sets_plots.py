# -*- coding: utf-8 -*-
"""
@author: Caleb Andrade
Created on Thu Jul 24 2015
Last Modified: Jul 24 2015

This is Application 3 - Plotting of cluster distortion
Algorithmic Thinking Module 3

"""
import alg_cluster
import compute_distortion as dis
import closest_pairs_clustering_algorithms as cpc
import matplotlib.pyplot as plt
import alg_project3_viz

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"

# initialize table data set
#data_table = alg_project3_viz.load_data_table(DATA_111_URL)
#data_table = alg_project3_viz.load_data_table(DATA_290_URL)
data_table = alg_project3_viz.load_data_table(DATA_896_URL)

# initialize distortion values list
Y = []
Z = []

# format data table and create initial cluster list
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    

# let's calculate for different number of output clusters
print "\n\nkmeans_clustering distortion: "
for idx in range(6, 21):
    cluster_list = cpc.kmeans_clustering(singleton_list, idx, 5)
    Z.append(dis.compute_distortion(cluster_list, data_table))
    print "\noutput clusters: ", idx
    print "distortion:  ", Z[idx - 6]

print "\n\nhierarchical_clustering distortion: "
for idx in range(6, 21):
    cluster_list = cpc.hierarchical_clustering(singleton_list, 26 - idx)
    Y.append(dis.compute_distortion(cluster_list, data_table))
    print "\noutput clusters: ", 26 - idx
    print "distortion:  ", Y[idx - 6]

Y.reverse()
   
X = [idx for idx in range(6, 21)] # x-axis values

plt.plot(X, Y, '-', color = 'b') # hierarchical clustering
plt.plot(X, Z, '-', color = 'r') # kmeans clustering

fig = plt.gcf()
fig.suptitle('Quality (cluster distortion): hierarchical vs kmeans clustering', fontsize=13)
ax = fig.add_subplot(111)
ax.set_xlabel('Number of output clusters', fontsize = 12)
ax.set_ylabel('Distortion', fontsize = 12)
fig.set_size_inches(8, 8)
#fig.savefig('cluster_distortion_111.png', dpi=100)
#fig.savefig('cluster_distortion_290.png', dpi=100)
fig.savefig('cluster_distortion_896.png', dpi=100)
plt.show()

