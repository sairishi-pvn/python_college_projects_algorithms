import math

"""
Dynamic Time Warping (DTW) applied to Gene Expression Analysis

This code compares gene expression profiles of two biological samples

using Dynamic Time Warping to measure similarity.

Each list represents expression values of the same genes
measured in two different samples or conditions.
"""

# Gene expression values (example subset of genes)
# Sample A: Tumor sample
# Sample B: Normal control
sample_A_expression = [1.2, 2.4, 3.1, 5.0, 4.8, 6.2]
sample_B_expression = [1.0, 1.8, 2.9, 3.5, 4.1, 5.6]

# Initialize DTW matrix
n = len(sample_A_expression)
m = len(sample_B_expression)

DTW = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# Set boundaries to infinity
for i in range(1, n + 1):
    DTW[i][0] = math.inf
for j in range(1, m + 1):
    DTW[0][j] = math.inf

# Compute DTW distance matrix
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = abs(
            sample_A_expression[i - 1] -
            sample_B_expression[j - 1]
        )
        DTW[i][j] = cost + min(
            DTW[i - 1][j],      # insertion
            DTW[i][j - 1],      # deletion
            DTW[i - 1][j - 1]   # match
        )

print("DTW Distance Matrix:")
for row in DTW:
    print(row)

# Backtracking to find optimal alignment path
i, j = n, m
alignment_path = [DTW[i][j]]

while i > 0 and j > 0:
    choices = {
        DTW[i - 1][j - 1]: "Diagonal",
        DTW[i - 1][j]: "Up",
        DTW[i][j - 1]: "Left"
    }

    min_cost = min(choices)
    move = choices[min_cost]

    if move == "Diagonal":
        i -= 1
        j -= 1
    elif move == "Up":
        i -= 1
    else:
        j -= 1

    alignment_path.append(DTW[i][j])

alignment_path.reverse()

# Final DTW score
dtw_score = DTW[n][m]

print("\nOptimal alignment path costs:")
print(alignment_path)

print("\nFinal DTW similarity score:", dtw_score)
