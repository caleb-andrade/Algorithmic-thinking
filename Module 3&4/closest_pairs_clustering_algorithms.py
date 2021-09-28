"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane

All code implemented in five functios is authored by Caleb Andrade.
Template and description was provided by Luay Nakhleh, Scott Rixner, Joe Warren.
"""

import alg_cluster

######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))

def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    answer = (float('inf'), -1, -1)
    for idx1 in range(len(cluster_list)):
        for idx2 in range(idx1 + 1, len(cluster_list)):
            temp = pair_distance(cluster_list, idx1, idx2)
            if temp[0] < answer[0]:
                answer = temp
    return answer

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    size = len(cluster_list)
    if size < 4:
        return slow_closest_pair(cluster_list)
    half = size / 2
    lcl = [] # left cluster list
    rcl = [] # right cluster list
    for idx in range(half):
        lcl.append(cluster_list[idx])
    for idx in range(half, size):
        rcl.append(cluster_list[idx])
    left_ans = fast_closest_pair(lcl)
    right_ans = fast_closest_pair(rcl)
    if left_ans[0] < right_ans[0]:
        temp_ans = left_ans
    else:
        temp_ans = (right_ans[0], right_ans[1] + half, right_ans[2] + half)
    mid = 0.5*(cluster_list[half - 1].horiz_center() + cluster_list[half].horiz_center())
    cps_ans = closest_pair_strip(cluster_list, mid, temp_ans[0])
    if cps_ans[0] < temp_ans[0]:
        return cps_ans
    else:
        return temp_ans

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    temp_list = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) <= half_width:
            temp_list.append([cluster_list[idx], idx])
    temp_list.sort(key = lambda item: item[0].vert_center()) # sort list by vert. center
    size = len(temp_list)
    ans = (float('inf'), -1, -1)
    for idx1 in range(size - 1):
        temp_ans = (float('inf'), -1, -1)
        for idx2 in range(idx1 + 1, min(idx1 + 4, size)):
            temp = temp_list[idx1][0].distance(temp_list[idx2][0])
            if temp < temp_ans[0]:
                temp_ans = (temp, idx1, idx2)
        if temp_ans[0] < ans[0]:
            ans = temp_ans
    if len(temp_list) > 0:
        ind = [temp_list[ans[1]][1], temp_list[ans[2]][1]]
    else:
        return (float('inf'), -1, -1)
    return (ans[0], min(ind), max(ind))            
        
######################################################################
# Code for hierarchical clustering

def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    cluster_list.sort(key = lambda cluster: cluster.horiz_center()) # sort list by horiz. center
    while len(cluster_list) > num_clusters:
        temp = fast_closest_pair(cluster_list)
        clust2 = cluster_list.pop(temp[2])
        clust1 = cluster_list.pop(temp[1])
        clust1.merge_clusters(clust2)
        binary_insert(cluster_list, clust1)
    return cluster_list
        
def binary_insert(cluster_list, cluster):
    """
    inserts cluster in cluster_list according to its horiz_center, 
    using binary search.
    """
    top = len(cluster_list)
    low = 0
    if cluster.horiz_center() < cluster_list[0].horiz_center():
        cluster_list.insert(0, cluster)
        return       
    while top != low + 1:
        mid = (low + top) /2
        if cluster.horiz_center() < cluster_list[mid].horiz_center():
            top = mid
        else:
            low = mid            
    cluster_list.insert(top, cluster)
        

######################################################################
# Code for k-means clustering

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    ans = [] # this list to store clusters with highest population (sorted)
    cen = [] # this list to store the initial centers as tuples
    temp = list(cluster_list)
    temp.sort(key = lambda cluster: cluster.total_population())
    temp.reverse()
    for idx in range(num_clusters):
        ans.append(temp[idx].copy())
        cen.append((ans[idx].horiz_center(), ans[idx].vert_center()))
   
    for dummy_i in range(num_iterations):
        clusters = [alg_cluster.Cluster(set([]), cen[idx][0], cen[idx][1], 0, 0) for idx in range(num_clusters)]
        for num in range(len(cluster_list)):
            best = (float('inf'), -1)
            for idx in range(num_clusters):
                temp = cluster_list[num].distance(ans[idx])
                if temp < best[0]:
                    best = (temp, idx)
            clusters[best[1]].merge_clusters(cluster_list[num])
        for idx in range(num_clusters):
            ans[idx] = clusters[idx].copy()
            cen[idx] = (clusters[idx].horiz_center(), clusters[idx].vert_center())
    return ans







































