import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster

def run_clustering(df, method='ward'):
    # Performs the actual math
    Z = linkage(df, method=method)
    return Z

def get_cluster_labels(Z, threshold):
    # Returns which cuisine belongs to which group
    return fcluster(Z, t=threshold, criterion='distance')