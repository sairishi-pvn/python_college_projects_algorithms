"""
Nussinov Algorithm for RNA Secondary Structure Prediction

This script predicts RNA secondary structure by maximizing
the number of valid base pairs using dynamic programming.

Valid pairs:
- A–U, U–A
- G–C, C–G
- G–U, U–G (wobble)

Minimum loop length = 3
"""

# RNA sequence
rna = "GAGACUU"
n = len(rna)

# Allowed base pairs (Watson–Crick + wobble)
valid_pairs = {
    ("A", "U"), ("U", "A"),
    ("G", "C"), ("C", "G"),
    ("G", "U"), ("U", "G")
}

def can_pair(i, j):
    """Check if two bases can form a valid pair"""
    return 1 if (rna[i], rna[j]) in valid_pairs else 0

# Initialize DP table
dp = [[0 for _ in range(n)] for _ in range(n)]

# Fill DP table
for length in range(4, n):  # minimum loop length = 3
    for i in range(n - length):
        j = i + length

        # Case 1: j unpaired
        best = dp[i][j - 1]

        # Case 2: i pairs with j
        best = max(best, dp[i + 1][j - 1] + can_pair(i, j))

        # Case 3: bifurcation
        for k in range(i + 1, j):
            best = max(best, dp[i][k - 1] + dp[k + 1][j - 1] + can_pair(k, j))

        dp[i][j] = best

# Output DP matrix
print("DP Matrix:")
for row in dp:
    print(row)

print("\nMaximum number of base pairs:", dp[0][n - 1])
