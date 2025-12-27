"""
K-Means Clustering for Gene Expression Data (Manual Implementation)

Description:
This script performs one iteration of K-means clustering
to group genes based on their expression profiles.

Each data point represents expression values of a gene
across two experimental conditions.
"""

import math


# Gene expression data
# Each tuple = (expression in condition 1, expression in condition 2)
gene_expression_data = [
    (1, 1),   # Gene 1
    (2, 1),   # Gene 2
    (4, 3),   # Gene 3
    (5, 4)    # Gene 4
]


# Initial centroids (chosen manually)
# Represent initial cluster centers
centroids = [
    (1, 1),   # Cluster 1
    (2, 1)    # Cluster 2
]

print("Initial Centroids:", centroids)
print("\nGene\tDistances to Centroids\tAssigned Cluster")


# Assignment step
for gene_index, gene in enumerate(gene_expression_data, start=1):
    x, y = gene
    distances = []

    print(f"Gene{gene_index} {gene}", end="\t")

    # Compute distance to each centroid
    for cx, cy in centroids:
        dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        dist = round(dist, 2)
        distances.append(dist)
        print(dist, end="\t")

    # Assign gene to nearest centroid
    assigned_cluster = distances.index(min(distances)) + 1
    print(f"Cluster {assigned_cluster}")

